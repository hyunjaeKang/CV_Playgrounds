import math
import os
import time
from pathlib import Path
from typing import Literal, Optional

import numpy as np
import torch
import tyro
from PIL import Image
from torch import Tensor, optim
import torchcodec
import torchvision.io as io

from gsplat import rasterization, rasterization_2dgs


class SimpleTrainer:
    """Trains random gaussians to fit an image."""

    def __init__(
        self,
        gt_image: Tensor,
        num_points: int = 2000
    ):
        self.device = torch.device("cuda:0")
        self.gt_image = gt_image.to(device=self.device)
        self.num_points = num_points

        fov_x = math.pi / 2.0
        self.H, self.W = gt_image.shape[0], gt_image.shape[1]
        self.focal = 0.5 * float(self.W) / math.tan(0.5 * fov_x)
        self.img_size = torch.tensor([self.W, self.H, 1], device=self.device)

        self._init_gaussians()

    def _init_gaussians(self):
        """Random gaussians"""
        bd = 2

        self.means = bd * (torch.rand(self.num_points, 3, device=self.device) - 0.5)
        self.scales = torch.rand(self.num_points, 3, device=self.device)
        d = 3
        self.rgbs = torch.rand(self.num_points, d, device=self.device)

        u = torch.rand(self.num_points, 1, device=self.device)
        v = torch.rand(self.num_points, 1, device=self.device)
        w = torch.rand(self.num_points, 1, device=self.device)

        self.quats = torch.cat(
            [
                torch.sqrt(1.0 - u) * torch.sin(2.0 * math.pi * v),
                torch.sqrt(1.0 - u) * torch.cos(2.0 * math.pi * v),
                torch.sqrt(u) * torch.sin(2.0 * math.pi * w),
                torch.sqrt(u) * torch.cos(2.0 * math.pi * w),
            ],
            -1,
        )
        self.opacities = torch.ones((self.num_points), device=self.device)

        self.viewmat = torch.tensor(
            [
                [1.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 8.0],
                [0.0, 0.0, 0.0, 1.0],
            ],
            device=self.device,
        )
        self.background = torch.zeros(d, device=self.device)

        self.means.requires_grad = True
        self.scales.requires_grad = True
        self.quats.requires_grad = True
        self.rgbs.requires_grad = True
        self.opacities.requires_grad = True
        self.viewmat.requires_grad = False

    def train(
        self,
        iterations: int = 1000,
        lr: float = 0.01,
        model_type: Literal["3dgs", "2dgs"] = "3dgs",
        save_imgs: bool = True,
        output_fname = "training",
        output_dir: str = "", 
        save_max_frames = 500,
        save_fps = 10,
    ):
        _save_frame = min(iterations, save_max_frames)
        _step = iterations // _save_frame
        optimizer = optim.Adam(
            [self.rgbs, self.means, self.scales, self.opacities, self.quats], lr
        )
        mse_loss = torch.nn.MSELoss()
        frames = []
        times = [0] * 2  # rasterization, backward
        K = torch.tensor(
            [
                [self.focal, 0, self.W / 2],
                [0, self.focal, self.H / 2],
                [0, 0, 1],
            ],
            device=self.device,
        )

        if model_type == "3dgs":
            rasterize_fnc = rasterization
            output_fname += "_3dgs"
        elif model_type == "2dgs":
            rasterize_fnc = rasterization_2dgs
            output_fname += "_2dgs"
            
        for iter in range(iterations):
            start = time.time()

            renders = rasterize_fnc(
                self.means,
                self.quats / self.quats.norm(dim=-1, keepdim=True),
                self.scales,
                torch.sigmoid(self.opacities),
                torch.sigmoid(self.rgbs),
                self.viewmat[None],
                K[None],
                self.W,
                self.H,
                packed=False,
            )[0]
            out_img = renders[0]
            torch.cuda.synchronize()
            times[0] += time.time() - start
            loss = mse_loss(out_img, self.gt_image)
            optimizer.zero_grad()
            start = time.time()
            loss.backward()
            torch.cuda.synchronize()
            times[1] += time.time() - start
            optimizer.step()
            print(f"Iteration {iter + 1}/{iterations}, Loss: {loss.item()}")

            if save_imgs and (iter % _step == 0 or iter == iterations - 1):
                frames.append((out_img.detach().cpu()*255).to(torch.uint8))
        if save_imgs:
            if output_dir == "":
                output_dir = os.path.join(os.getcwd(), "temp_results")
            Path(output_dir).mkdir(exist_ok=True, parents=True)

            frames = torch.stack(frames).to(torch.uint8)
            o_fpath = f"{output_dir}/{output_fname}.mp4"
            video_codec = "libx264"
            io.write_video(o_fpath, frames, save_fps, video_codec=video_codec)

        print(f"Total(s):\nRasterization: {times[0]:.3f}, Backward: {times[1]:.3f}")
        print(
            f"Per step(s):\nRasterization: {times[0]/iterations:.5f}, Backward: {times[1]/iterations:.5f}"
        )


def image_path_to_tensor(image_path: Path):
    import torchvision.transforms as transforms

    img = Image.open(image_path)
    transform = transforms.ToTensor()
    img_tensor = transform(img).permute(1, 2, 0)[..., :3]
    return img_tensor


def fit(
    img_path: Optional[Path] = None,
    height: int = 256,
    width: int = 256,
    num_points: int = 100000,
    iterations: int = 1000,
    lr: float = 0.01,
    model_type: Literal["3dgs", "2dgs"] = "3dgs",
    save_imgs: bool = True,
    output_dir: str = "", 
    save_max_frames = 200,
    save_fps = 30,
) -> None:
    if img_path:
        gt_image = image_path_to_tensor(img_path)
        output_fname = os.path.splitext(os.path.basename(img_path))[0]
    else:
        gt_image = torch.ones((height, width, 3)) * 1.0
        # make top left and bottom right red, blue
        gt_image[: height // 2, : width // 2, :] = torch.tensor([1.0, 0.0, 0.0])
        gt_image[height // 2 :, width // 2 :, :] = torch.tensor([0.0, 0.0, 1.0])
        output_fname = "training"

    output_fname = f"{output_fname}_{num_points}_{iterations}"

    trainer = SimpleTrainer(gt_image=gt_image, num_points=num_points)
    trainer.train(
        iterations=iterations,
        lr=lr,
        model_type=model_type,
        save_imgs=save_imgs,
        output_fname = output_fname,
        output_dir = output_dir,
        save_max_frames = save_max_frames,
        save_fps = save_fps,
    )

if __name__ == "__main__":
    tyro.cli(fit)

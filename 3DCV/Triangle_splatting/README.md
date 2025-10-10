# Triangle Splatting Playgrounds

---
## Setup a conda environment

```

# pwd ~/CV_Playgrounds/3DCV/triangle_splatting
# nvcc --version
#   nvcc: NVIDIA (R) Cuda compiler driver
#   Copyright (c) 2005-2025 NVIDIA Corporation
#   Built on Tue_May_27_02:21:03_PDT_2025
#   Cuda compilation tools, release 12.9, V12.9.86
#   Build cuda_12.9.r12.9/compiler.36037853_0

git clone https://github.com/trianglesplatting/triangle-splatting temp_triangle-splatting --recursive
cd temp_triangle-splatting

conda create -y -n triangle_splatting python=3.11
conda activate triangle_splatting

pip install ipykernel ipywidgets
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
pip install tqdm plyfile open3d lpips mediapy opencv-python gdown

bash compile.sh
cd submodules/simple-knn
pip install .

```

---

### Notebooks for triangle-splatting

<table border="1">
<thead>
    <tr>
      <th style="text-align:center;padding:10px;">Notebook</th>
      <th style="text-align:center;padding:10px;">Source Video</th>
      <th style="text-align:center;padding:10px;">Rendered Video (Indoor)</th>
      <th style="text-align:center;padding:10px;">Rendered Video (Outdoor)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td style="text-align:center;padding:10px;">
          <a href="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/Triangle_splatting/custom_data_00.ipynb" target="_blank">
            Statue1
          </a>
        </td>
        <td style="text-align:center;padding:10px;">
          <a href="https://drive.google.com/file/d/1v_r7gjiomJNwemsXKaaJNpcTCFKl-Nbj/preview" target="_blank">
            <img src="https://drive.google.com/thumbnail?id=1v_r7gjiomJNwemsXKaaJNpcTCFKl-Nbj" width="150" height="130" alt="Source Video 1">
          </a>
        </td>
        <td style="text-align:center;padding:10px;">
          <a href="https://drive.google.com/file/d/1ED1hpp6oZw6eQXaPApc9cQVxcFtOhQj1/preview" target="_blank">
            <img src="https://drive.google.com/thumbnail?id=1ED1hpp6oZw6eQXaPApc9cQVxcFtOhQj1" width="150" height="130" alt="Rendered Indoor Video 1">
          </a>
        </td>
        <td style="text-align:center;padding:10px;">
          <a href="https://drive.google.com/file/d/1pHegA8MXzwpE2OBtenGnxNVLy3XmyyLu/preview" target="_blank">
            <img src="https://drive.google.com/thumbnail?id=1pHegA8MXzwpE2OBtenGnxNVLy3XmyyLu" width="150" height="130" alt="Rendered Outdoor Video 1">
          </a>
        </td>
    </tr>
    <tr>
      <td style="text-align:center;padding:10px;">
        <a href="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/Triangle_splatting/custom_data_01.ipynb" target="_blank">
          Statue2
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1fFvegLaEc_pGmputDUD6InIQFf8auEC1/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1fFvegLaEc_pGmputDUD6InIQFf8auEC1" width="150" height="130" alt="Source Video 2">
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1G0HtqfI5HKtdrb78hlmc20PXKLk_jehf/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1G0HtqfI5HKtdrb78hlmc20PXKLk_jehf" width="150" height="130" alt="Rendered Indoor Video 2">
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1WLTYK7O37-FUQSBfK2qsitquw29ocT-T/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1WLTYK7O37-FUQSBfK2qsitquw29ocT-T" width="150" height="130" alt="Rendered Outdoor Video 2">
        </a>
      </td>
    </tr>
    <tr>
      <td style="text-align:center;padding:10px;">
        <a href="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/Triangle_splatting/custom_data_02.ipynb" target="_blank">
          Bay
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1eNb_GkkOKUSq_6cS8g4_cuPJ9CZvPBkQ/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1eNb_GkkOKUSq_6cS8g4_cuPJ9CZvPBkQ" width="150" height="130" alt="Source Video 3">
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1BS_rwY6760t8MMJpw4biG-Nhx9ZkUxMu/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1BS_rwY6760t8MMJpw4biG-Nhx9ZkUxMu" width="150" height="130" alt="Rendered Indoor Video 3">
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1shNBwf1wTEG5zkBBHHyCZAnfndKgmegI/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1shNBwf1wTEG5zkBBHHyCZAnfndKgmegI" width="150" height="130" alt="Rendered Outdoor Video 3">
        </a>
      </td>
    </tr>
    <tr>
      <td style="text-align:center;padding:10px;">
        <a href="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/Triangle_splatting/custom_data_03.ipynb" target="_blank">
          Gym
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1jx1jtZQnxe1lmzzKQTBKuffmic4Did62/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1jx1jtZQnxe1lmzzKQTBKuffmic4Did62" width="150" height="130" alt="Source Video 4">
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1AJvv9YRf1LUzohfpJDP00A5upeq_Vd5_/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1AJvv9YRf1LUzohfpJDP00A5upeq_Vd5_" width="150" height="130" alt="Rendered Indoor Video 4">
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1BR_nfmDHIWrbpHdJKLFmqfTlLAt38o4W/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1BR_nfmDHIWrbpHdJKLFmqfTlLAt38o4W" width="150" height="130" alt="Rendered Outdoor Video 4">
        </a>
      </td>
    </tr>
    <tr>
      <td style="text-align:center;padding:10px;">
        <a href="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/Triangle_splatting/custom_data_04.ipynb" target="_blank">
          GrandPlaza
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1T6naoj4bNRZOdoKjLmI3WAd1cp-NBCTR/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1T6naoj4bNRZOdoKjLmI3WAd1cp-NBCTR" width="150" height="130" alt="Source Video 5">
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/18XKK-AzypP9W5YkdsW7gnY5tb9orl8XF/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=18XKK-AzypP9W5YkdsW7gnY5tb9orl8XF" width="150" height="130" alt="Rendered Indoor Video 5">
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1U0NnnCVJQUrftQpbzkQvm8NFqrmP4dew/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1U0NnnCVJQUrftQpbzkQvm8NFqrmP4dew" width="150" height="130" alt="Rendered Outdoor Video 5">
        </a>
      </td>
    </tr>
    <tr>
      <td style="text-align:center;padding:10px;">
        <a href="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/Triangle_splatting/custom_data_05.ipynb" target="_blank">
          GrandPlaza2
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1SnKE3e-2EDU1ocYfDes3GIC4Zmmd4rSI/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1SnKE3e-2EDU1ocYfDes3GIC4Zmmd4rSI" width="150" height="130" alt="Source Video 6">
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1ToQJFVUGHC1Q42-2e0W7VZMlvNjd6NFu/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1ToQJFVUGHC1Q42-2e0W7VZMlvNjd6NFu" width="150" height="130" alt="Rendered Indoor Video 6">
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1vbFwpr0DiyyqjV9K9l9cYY4VjhIkRSKF/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1vbFwpr0DiyyqjV9K9l9cYY4VjhIkRSKF" width="150" height="130" alt="Rendered Outdoor Video 6">
        </a>
      </td>
    </tr>
    <tr>
      <td style="text-align:center;padding:10px;">
        <a href="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/Triangle_splatting/custom_data_06.ipynb" target="_blank">
          WhitePass
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1LdXaVkme3egIwiMMevApDnwZcMUv0VvK/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1LdXaVkme3egIwiMMevApDnwZcMUv0VvK" width="150" height="130" alt="Source Video 7">
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1qLg9Hl9JeuInJYsreOEqLvFdQ_z5-lJi/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1qLg9Hl9JeuInJYsreOEqLvFdQ_z5-lJi" width="150" height="130" alt="Rendered Indoor Video 7">
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1Ukg3uMMSklBXvrOwZhh4IFgccBeZKaC9/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1Ukg3uMMSklBXvrOwZhh4IFgccBeZKaC9" width="150" height="130" alt="Rendered Outdoor Video 7">
        </a>
      </td>
    </tr>
    <tr>
      <td style="text-align:center;padding:10px;">
        <a href="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/Triangle_splatting/custom_data_07.ipynb" target="_blank">
          Alaska
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1LCjjapYzev3hbvaiOY28EIU53OkEvNqt/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1LCjjapYzev3hbvaiOY28EIU53OkEvNqt" width="150" height="130" alt="Source Video 8">
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1SFAdpZ-7Q-AzknCVGb1RMo1MvanS18c4/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1SFAdpZ-7Q-AzknCVGb1RMo1MvanS18c4" width="150" height="130" alt="Rendered Indoor Video 8">
        </a>
      </td>
      <td style="text-align:center;padding:10px;">
        <a href="https://drive.google.com/file/d/1K50nF9B0kjF3RkFQQmiZltiT-4xb4XYC/preview" target="_blank">
          <img src="https://drive.google.com/thumbnail?id=1K50nF9B0kjF3RkFQQmiZltiT-4xb4XYC" width="150" height="130" alt="Rendered Outdoor Video 8">
        </a>
      </td>
    </tr>
  </tbody>
</table>


---
### References:

- ***Paper***:
    - [Triangle Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2505.19175)

- ***Blog***:
    - https://trianglesplatting.github.io/
    - [The Future of 3D Is… Triangles?!](https://youtu.be/F0H3NAHP9r0?si=_yGrimHZyHQvA2Cn)

- ***Github***:
    - https://github.com/trianglesplatting/triangle-splatting

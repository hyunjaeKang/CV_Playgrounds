# 3DCV_Playgrounds


---
## Setup a conda environment

 ```
 conda create -y -n 3dcv_playgrounds python=3.10.12
 conda activate 3dcv_playgrounds

 pip install ipykernel ipywidgets
 pip install matplotlib opencv-python imageio scikit-learn gdown
 pip install -U torch torchvision torchao pytorchvideo torchcodec torchshow
 pip install PyOpenGL glfw laspy plyfile imgui open3d pyquaternion

 conda install bioconda::pangolin
 ```


----

## Playgrounds


<table>
  <thead>
    <tr>
      <th>Playground</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th align="left" rowspan="1"><a href="./Cookbooks/">Cookbooks</a></th>
      <th align="left" rowspan="1">A collection of notebook for 3D Computer vision</i></th>
    </tr>
    <tr>
      <th align="left" rowspan="1"><a href="./Monocular_slam_front_end/">Monocular_slam_front_end</a></th>
      <th align="left" rowspan="1">Exploratory code for Monocular SLAM Front End</i></th>
    </tr>
    <tr>
      <th align="left" rowspan="1"><a href="./TinyNeRF/">TinyNeRF</a></th>
      <th align="left" rowspan="1">Experimental notebooks for NeRF models</i></th>
    </tr>
    <tr>
      <th align="left" rowspan="1"><a href="./GSPLAT/">GSPLAT</a></th>
      <th align="left" rowspan="1">Evaluation notebooks for Gaussian Splatting methods with various datasets</th>
    </tr>
    <tr>
      <th align="left" rowspan="1"><a href="./Triangle_splatting/">Triangle_splatting</a></th>
      <th align="left" rowspan="1">Demo notebooks for Triangle Splatting with various datasets</th>
    </tr>
  </tbody>
</table>

-----


### References:

- ***Paper***:

    - **NeRF**: Representing Scenes as Neural Radiance Fields for View Synthesis [[arXiv]](https://arxiv.org/abs/2003.08934)
    - **FastNeRF**: High-Fidelity Neural Rendering at 200FPS [[arXiv]](https://arxiv.org/abs/2103.10380)
    - **KiloNeRF**: Speeding up Neural Radiance Fields with Thousands of Tiny MLPs [[arXiv]](https://arxiv.org/abs/2103.13744)
    - **PlenOctrees** for Real-time Rendering of Neural Radiance Fields [[arXiv]](https://arxiv.org/abs/2103.14024)
    - **Plenoxels**: Radiance Fields without Neural Networks [[arXiv]](https://arxiv.org/abs/2112.05131)
    - **InfoNeRF**: Ray Entropy Minimization for Few-Shot Neural Volume Rendering [[arXiv]](https://arxiv.org/abs/2112.15399)
    - **Instant** Neural Graphics Primitives with a Multiresolution Hash Encoding [[arXiv]](https://arxiv.org/abs/2201.05989)
    - **K-Planes**: Explicit Radiance Fields in Space, Time, and Appearance [[arXiv]](https://arxiv.org/abs/2301.10241)
    - **FreeNeRF**: Improving Few-shot Neural Rendering with Free Frequency Regularization [[arXiv]](https://arxiv.org/abs/2303.07418)
    - [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_high.pdf)
    - [3D Gaussian Splatting as Markov Chain Monte Carlo](https://arxiv.org/abs/2404.09591?utm_source=chatgpt.com)
    - [3D Gaussian Splatting as Markov Chain Monte Carlo - NIPS papers](https://proceedings.neurips.cc/paper_files/paper/2024/file/93be245fce00a9bb2333c17ceae4b732-Paper-Conference.pdf?utm_source=chatgpt.com)
    - [3D Gaussian Splatting as Markov Chain Monte Carlo - OpenReview](https://openreview.net/forum?id=UCSt4gk6iX&utm_source=chatgpt.com)
    - [2D Gaussian Splatting for Geometrically Accurate Radiance Fields](https://arxiv.org/abs/2403.17888?utm_source=chatgpt.com)
    - [2D Gaussian Splatting for Geometrically Accurate Radiance Fields](https://surfsplatting.github.io/assets/paper/paper.pdf?utm_source=chatgpt.com)
    - [Anti-Aliased 2D Gaussian Splatting](https://arxiv.org/abs/2506.11252?utm_source=chatgpt.com )
    - [3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507?utm_source=chatgpt.com )
    - [Triangle Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2505.19175)

- ***Blog***:
    - https://learnopencv.com/iterative-closest-point-icp-explained/
    - https://learnopencv.com/3d-lidar-visualization/
    - https://learnopencv.com/monocular-slam-in-python/
    - [3D Gaussian Splatting Introduction – Paper Explanation & Training on Custom Datasets with NeRF Studio Gsplats](https://learnopencv.com/3d-gaussian-splatting/)
    - [gsplat documentation](https://docs.gsplat.studio/main/index.html)
    - https://trianglesplatting.github.io/
    - [The Future of 3D Is… Triangles?!](https://youtu.be/F0H3NAHP9r0?si=_yGrimHZyHQvA2Cn)

- ***Github***:
    - https://github.com/OmarJItani/Iterative-Closest-Point-Algorithm/tree/main
    - https://github.com/spmallick/learnopencv/tree/master/Monocular%20SLAM%20for%20Robotics%20implementation%20in%20python
    - [Papers-in-100-Lines-of-Code](https://github.com/MaximeVandegar/Papers-in-100-Lines-of-Code/tree/main)
    - [gsplat](https://github.com/nerfstudio-project/gsplat/tree/main)
    - https://github.com/trianglesplatting/triangle-splatting


# 3DCV_Playgrounds

---
## Playgrounds
- Experiments
- gsplat
- TinyNeRF
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



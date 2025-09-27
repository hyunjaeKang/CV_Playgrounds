# GSplat



### Setup a conda environment

 ```
 # pwd : ~/CV_Playgrounds/3DCG/gsplat

 sudo apt install colmap

 conda create -y -n gsplat python=3.10.12
 conda activate gsplat
 
 
 pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
 
 git clone https://github.com/nerfstudio-project/gsplat.git temp_gsplat
 pip install -e ./temp_gsplat

 pip install -r ./temp_gsplat/examples/requirements.txt
 pip install ipykernel ipywidgets gdown torchcodec av
 ```



 ---
### Reference:


- ***Papers***:
    - ...

- ***Blog***:
    - [3D Gaussian Splatting Introduction – Paper Explanation & Training on Custom Datasets with NeRF Studio Gsplats](https://learnopencv.com/3d-gaussian-splatting/)
    - [gsplat documentation](https://docs.gsplat.studio/main/index.html)

- ***Github***:
    - [gsplat](https://github.com/nerfstudio-project/gsplat/tree/main)
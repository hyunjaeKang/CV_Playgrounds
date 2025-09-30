# CV_Playgrounds

---
## Playgrounds
- 2DCV : 2D Computer vision
- 3DCG : 3D Computer Graphics
- 3DCV : 3D Computer vision
- VLM : Visual Language Model

---
## Setup a conda environment

 ```
 conda create -y -n cv_playgrounds python=3.10.12
 conda activate cv_playgrounds

 pip install -U torch torchvision torchao pytorchvideo torchcodec
 pip install -U transformers transformers_stream_generator datasets evaluate accelerate timm
 pip install ipykernel ipywidgets
 pip install matplotlib opencv-python faiss-cpu imageio scikit-learn gradio==3.50
 pip install tiktoken num2words kaggle kagglehub einops qwen_vl_utils loadimg
 ```


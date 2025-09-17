# CV_Drills



### Setup a conda environment

 ```
 conda create -y -n cv_playgrounds python=3.10.12
 conda activate cv_playgrounds
 
 pip install -U torch torchvision torchao pytorchvideo torchcodec
 pip install -U transformers datasets evaluate accelerate timm kagglehub
 pip install ipykernel ipywidgets 
 pip install matplotlib opencv-python faiss-cpu imageio kaggle scikit-learn gradio==3.50
 ```
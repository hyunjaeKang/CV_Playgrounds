# 2D CV Playgrounds

---
## Setup a conda environment

 ```
 conda create -y -n cv_playgrounds python=3.10.12
 conda activate cv_playgrounds

 pip install -U torch torchvision torchao pytorchvideo torchcodec torchsummary torchshow torchmetrics
 pip install -U transformers transformers_stream_generator diffusers
 pip install datasets evaluate accelerate timm insightface onnxruntime peft
 pip install ipykernel ipywidgets
 pip install matplotlib opencv-python faiss-cpu imageio scikit-learn gradio==3.50 mediapy
 pip install tiktoken num2words kaggle kagglehub einops qwen_vl_utils loadimg lovely_tensors
 pip install tensorflow==2.19.0 tf_keras==2.19.0 tensorflow_probability
 pip install "transformers[sentencepiece]"

 # For MacOS
 pip install tensorflow-metal
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
      <th align="left" rowspan="1">A collection of notebook for 2D Computer vision</i></th>
    </tr>
    <tr>
      <th align="left" rowspan="1"><a href="./Book_deep_learning_from_scratch_5/">Book_deep_learning_from_scratch_5</a></th>
      <th align="left" rowspan="1">Demo notebooks for <i>Deep learning from Scratch 5</i></th>
    </tr>
    <tr>
      <th align="left" rowspan="1"><a href="./Book_generative_deep_learning_2nd/">Book_generative_deep_learning_2nd</a></th>
      <th align="left" rowspan="1">Test notebooks for <i>Generative Deep Learning, 2nd Eidtion</i></th>
    </tr>
    <tr>
      <th align="left" rowspan="1"><a href="./TinyDiffusion/">TinyDiffusion</a></th>
      <th align="left" rowspan="1">Experimental notebooks for Diffusion models</th>
    </tr>
    <tr>
      <th align="left" rowspan="1"><a href="./HF_Transformers/">HF_Transformers</a></th>
      <th align="left" rowspan="1">Tutorial notebooks for <i>Hugging Face Transformers</i></th>
    </tr>
    <tr>
      <th align="left" rowspan="1"><a href="./HF_Diffusion/">HF_Diffusion</a></th>
      <th align="left" rowspan="1">A collection of Jupyter notebooks for the Hugging Face Diffusion library.</th>
    </tr>
    <tr>
      <th align="left" rowspan="1"><a href="./DINOv3/">DINOv3</a></th>
      <th align="left" rowspan="1">Demo Jupyter notebooks for DINOv3 model</th>
    </tr>
  </tbody>
</table>

-----


### References :

- ***Paper***:
    - [DINOv3](https://arxiv.org/abs/2508.10104)


- ***Blog***:
    - [Flow Matching vs Diffusion](https://harshm121.medium.com/flow-matching-vs-diffusion-79578a16c510)
    - [Hugging Face :: Transformers](https://huggingface.co/docs/transformers/main/en/index)
    - [Hugging Face Diffusers](https://huggingface.co/docs/diffusers/v0.34.0/en/index)
    - [DINOV3](https://ai.meta.com/dinov3/)
    - [Request access to Meta DINOv3](https://ai.meta.com/resources/models-and-libraries/dinov3-downloads/)
    - [Training CLIP Model from Scratch for an Fashion Image Retrieval App](https://learnopencv.com/clip-model/)
    - [Understanding CLIP for vision language models](https://medium.com/self-supervised-learning/understanding-clip-for-vision-language-models-43b700a4aa2b)
    - [CLIP Model and The Importance of Multimodal Embeddings](https://towardsdatascience.com/clip-model-and-the-importance-of-multimodal-embeddings-1c8f6b13bf72/)
    - [CLIP, Intuitively and Exhaustively Explained](https://towardsdatascience.com/clip-intuitively-and-exhaustively-explained-1d02c07dbf40/)

- ***Github***:
    - [Papers-in-100-Lines-of-Code](https://github.com/MaximeVandegar/Papers-in-100-Lines-of-Code)
    - DDPM: https://github.com/MaximeVandegar/Papers-in-100-Lines-of-Code/tree/main/Denoising_Diffusion_Probabilistic_Models
    - https://medium.com/@adityanutakki/sr3-explained-and-implemented-in-pytorch-from-scratch-b43b9742c232
    - https://github.com/aditya-nutakki/pfs/tree/master/sr3
    - https://github.com/CodingVillainKor/SimpleDeepLearning/blob/main/flowmatching.ipynb
    - https://github.com/harshm121/Diffusion-v-FlowMatching/
    - https://github.com/huggingface/transformers/tree/main/notebooks
    - https://github.com/huggingface/notebooks/tree/main
    - [DINOv3](https://github.com/facebookresearch/dinov3)
    - https://github.com/spmallick/learnopencv/tree/master/Training-CLIP-from-Scratch-for-Image-Retrieval
    - https://github.com/metamath1/pytorch-stable-diffusion-fine-tuning
    - https://github.com/davidADSP/Generative_Deep_Learning_2nd_Edition
    - https://github.com/oreilly-japan/deep-learning-from-scratch-5



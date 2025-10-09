# DINOV3 Playground

-----

### Setup environment

### conda env
- [cv_playgrounds](../../README.md#setup-a-conda-environment)

---

### Download github

```
# pwd
# ~/CV_Playgrounds/2DCV/DINOV3

git clone https://github.com/facebookresearch/dinov3.git ./temp_dinov3

```

- Download the pre-trained DINOV3 model with the following page:
https://ai.meta.com/resources/models-and-libraries/dinov3-downloads/

----

### Manual download a pre-trained model

- Request access to the weights
    - Navigate to the official DINOv3 download page on Meta AI's website.
    - Fill out the license agreement form.
    - Wait for an email from Meta providing access to the weights download links.

- Download the dinotxt (e.g. ***dinov3_vitl16_dinotxt_tet1280d20h24l***) weights
    - Use the download link for the ***dinov3_vitl16_dinotxt_tet1280d20h24l*** model weights from the email you receive.
    - Save the .pth file to a local directory  : ***./temp_dinov3_model***


- Folder structure:
```
-CV_Playgrounds
  |- 2DCV
  |   |...
  |   |-DINOv3
  |   |    |- temp_dinov3_model
  |   |    |   |- dinov3_vitl16_pretrain_lvd1689m-8aa4cbdd.pth
  |   |    |   |- dinov3_vitl16_dinotxt_vision_head_and_text_encoder-a442d8f5.pth
  |   |...

```

---

### Jupyter Notebooks

| Demo | Notebook |
| ---- | ---- |
| Dense And Sparse Correspondence | [dense_sparse_matching.ipynb](./dense_sparse_matching.ipynb) |
| DINO TXT Interference | [dinotxt_inference.ipynb](./dinotxt_inference.ipynb) |
| Training a Foreground Segmentation Tool with DINOv3 | [foreground_segmentation.ipynb](./foreground_segmentation.ipynb) |
| Computing the PCA of a Foreground Object | [pca.ipynb](./pca.ipynb) |
| Segmentation Tracking with DINOv3 | [./segmentation_tracking.ipynb](./segmentation_tracking.ipynb) |


---
### Reference:

- ***Papers***:
    - [DINOv3](https://arxiv.org/abs/2508.10104)

- ***Blog***:
    - [DINOV3](https://ai.meta.com/dinov3/)
    - [Request access to Meta DINOv3](https://ai.meta.com/resources/models-and-libraries/dinov3-downloads/)

- ***Github***:
    - [DINOv3](https://github.com/facebookresearch/dinov3)

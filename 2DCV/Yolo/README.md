# Yolo Playgrounds

----

### Setup a conda environment

- [cv_playgrounds](../README.md#setup-a-conda-environment)

----


### Contents


* **YOLO family** – real-time object *detectors* (YOLOv8–12, YOLO-World, YOLOE)
* **SAM family** – “segment anything” *segmenters* (SAM1, SAM2, FastSAM, MobileSAM)
* **RT-DETR** – a DETR-style real-time *detector*


---

## 1. YOLO family (v8–v12, YOLO-World, YOLOE)

All YOLOs are **single-stage real-time detectors**; differences are architecture, training tricks, and whether they support open-vocabulary/prompting.

### [YOLOv8](./yolov8_custom_data.ipynb) – strong CNN baseline

From Ultralytics (2023), still widely used and very stable. ([Ultralytics Docs][1])

* **Architecture:** pure CNN backbone + FPN/PAN neck, modern **anchor-free decoupled head**.
* **Tasks:** detection, instance segmentation, classification, pose, oriented boxes.
* **Performance:** on COCO, v8m (640) ≈ *50 mAP* with ~26M params. ([Ultralytics Docs][1])

Use it as: **older but very battle-tested baseline**; huge ecosystem of tutorials and tools.

---

### [YOLOv9](./yolov9.ipynb) – PGI + GELAN (accuracy-driven)

Research model with a focus on **information preservation**. ([arXiv][2])

* **Programmable Gradient Information (PGI):** extra gradient paths designed to counter information loss across layers (information bottleneck).
* **GELAN backbone:** “Generalized Efficient Layer Aggregation Network” – more efficient feature reuse than older CSP-style nets. ([arXiv][2])
* **Effect:** better **accuracy vs parameters** than v8 for many sizes, at the cost of more complex training. ([Ultralytics Docs][3])

Use it when: you want a **research-grade CNN YOLO** that squeezes out accuracy and you don’t mind more training complexity.

---

### [YOLOv10](./yolov10.ipynb) – NMS-free, efficiency-obsessed

From Tsinghua; integrated into Ultralytics. Main idea: **end-to-end, NMS-free YOLO** that pushes speed/accuracy frontier. ([Ultralytics Docs][4])

Key ideas:

* **Consistent dual assignments:**

  * one head uses one-to-many assignment (rich supervision),
  * one head uses one-to-one assignment → **at inference you keep only those predictions, no NMS needed.** ([arXiv][5])
* **Holistic efficiency-driven design:** CSP-like backbone with tweaks (light heads, spatial-channel decoupled downsampling, large kernels, partial self-attention) to maximize mAP per FLOP. ([Ultralytics Docs][4])
* **Result:** SOTA or near-SOTA mAP for given latency; significantly less post-processing overhead than v8/9. ([Ultralytics Docs][4])

Use it when: **latency and deployability** are critical and NMS-free pipelines are attractive.

---

### [YOLO11](./yolo11.ipynb) – Ultralytics’ current “default workhorse”

Ultralytics’ latest mainstream YOLO, positioned as a **direct successor to v8** for real-world tasks. ([Ultralytics Docs][6])

* **Architecture:** refined CNN backbone/neck vs v8, but no radical redesign – just more efficient feature aggregation.
* **Tasks:** detection, seg, classification, pose, tracking, OBB. ([Ultralytics Docs][6])
* **Efficiency:** YOLO11m gets higher COCO mAP than YOLOv8m with **~22% fewer params**, and the family is generally faster at a given accuracy. ([Ultralytics][7])

Use it as: **go-to closed-set YOLO** today unless you have a special reason to pick something else.

---

### [YOLO12](./yolo12.ipynb) – attention-centric YOLO

Newer, attention-heavy YOLO with an explicit focus on **large receptive fields via attention** while still being real-time. ([Ultralytics Docs][8])

* **Area Attention:** partitions feature maps into regions and applies self-attention over them → large effective receptive field at lower cost than vanilla global attention. ([Ultralytics Docs][8])
* **R-ELAN (Residual ELAN):** improved layer aggregation to keep big attention models trainable. ([Ultralytics Docs][8])
* **Trade-off:** modest mAP gains over YOLO11 at the same scale, but higher memory usage and some training/inference overhead; Ultralytics warns it’s more “researchy” and suggests YOLO11 for production. ([Ultralytics Docs][8])

Use it when: you’re experimenting with **attention-heavy detectors** and can afford extra VRAM / complexity for small accuracy bumps.

---

### [YOLO-World](./yolo_world.ipynb) – open-vocabulary YOLO

“Detect anything you can name in text,” built on YOLOv8 with a vision–language head. ([Ultralytics Docs][9])

* **Base:** YOLOv8-style CNN backbone & neck.
* **Text encoder:** CLIP-like module encodes category names or phrases into embeddings.
* **Prompt-then-detect:** a set of text prompts (“motorcycle”, “crack in wall”, “hard hat”) is encoded *once* into an offline vocabulary; detection is done by matching visual features to that embedding set, keeping it real-time. ([arXiv][10])
* **Zero-shot:** good open-vocabulary mAP on COCO and other benchmarks while running close to YOLOv8 speed. ([arXiv][10])

Use it when: you need **open-vocabulary detection** (categories defined at inference via text), but still want YOLO-like speed.

---

### [YOLOE](./yoloe.ipynb) – “Real-Time Seeing Anything”

From THU-MIG (same group as YOLOv10), and also in Ultralytics. It generalizes YOLO-World: **a promptable detector+segmenter** that supports multiple prompt types. ([arXiv][11])

* **Prompts:**

  * **text prompts** (like YOLO-World),
  * **visual prompts** (boxes, masks, reference images),
  * **prompt-free** mode → behaves like a normal detector. ([GitHub][12])
* **Detection + segmentation:** unified architecture for open-vocabulary detection *and* segmentation.
* **RepRTA (Re-parameterizable Region-Text Alignment):** small auxiliary module that refines text embeddings during training to align better with visual features, but gets “folded” away at inference → **no speed hit vs closed-set YOLOs.** ([arXiv][11])
* **Base design:** conceptually built on YOLOv10 ideas, aiming for real-time performance. ([GitHub][13])

Use it when: you want a **single real-time model** that can be closed-set, open-vocabulary, and do segmentation, all with minimal overhead.

---

## 2. SAM family (SAM1, SAM2, FastSAM, MobileSAM)

All SAM variants are **promptable segmenters**: given points/boxes/masks (and sometimes text), they produce segmentation masks. The differences are capacity (foundation vs light), modality (image vs video), and architecture (ViT vs CNN).

### [SAM1](./sam2.ipynb) – original Segment Anything Model

Meta’s 2023 foundation segmentation model. ([arXiv][14])

* **Training:** on SA-1B – 11M images, 1.1B masks; one of the largest seg datasets. ([arXiv][14])
* **Architecture:**

  * heavy **ViT image encoder**,
  * prompt encoder (points/boxes/masks),
  * mask decoder that outputs high-quality masks for any prompt. ([arXiv][14])
* **Strength:** fantastic **zero-shot segmentation** on many domains.
* **Weakness:** encoder is big → relatively **slow and heavy** for real-time or edge use.

Use it when: you want **top-tier zero-shot segmentation quality** and have decent compute (GPU/server).

---

### [SAM2](./sam2.ipynb) – unified image + video SAM with streaming memory

SAM2 extends SAM to **videos** and makes both image & video segmentation faster and more interactive. ([arXiv][15])

* **Data:** introduces SA-V, the largest video segmentation dataset to date, collected in a model-in-the-loop pipeline. ([arXiv][15])
* **Architecture:** a transformer model with **streaming memory**:

  * frames are processed sequentially,
  * object-aware memory stores embeddings from previous frames to refine masks in later frames, enabling **real-time tracking and segmentation**. ([arXiv][15])
* **Performance:**

  * improved video segmentation with far fewer interactions (≈3× fewer clicks needed),
  * more accurate image segmentation and **≈6× faster** than SAM1 in many setups. ([arXiv][15])

Use it when: you need **interactive segmentation in videos** (or images) and can afford a powerful GPU. It’s the **current flagship** in the SAM family.

---

### [FastSAM](./fast_sam.ipynb) – CNN alternative to SAM

Designed to mimic the “segment anything” capability with a **lightweight CNN** instead of a huge ViT. ([Ultralytics Docs][16])

* **Architecture:** YOLO-like CNN encoder + simple mask head; no giant ViT.
* **Training:** uses a subset (~2%) of SA-1B; trades some accuracy for speed. ([Roboflow Blog][17])
* **Pros:**

  * **real-time on modest hardware**,
  * much lower memory/compute than SAM1. ([Ultralytics Docs][16])
* **Cons:**

  * weaker zero-shot generalization vs SAM1/2,
  * mask quality generally lower.

Use it when: you want **fast, approximate “segment anything”** and classic SAM is too heavy.

---

### [MobileSAM](./mobile_sam.ipynb) – lightweight, distillation-based SAM

MobileSAM specifically targets **mobile/edge devices**, distilling SAM’s encoder into a much smaller model. ([Ultralytics Docs][18])

* **Idea:**

  * replace SAM’s heavy image encoder with a **lightweight encoder**,
  * train it to mimic SAM via **knowledge distillation**; decoder is compatible with the original SAM pipeline. ([GitHub][19])
* **Efficiency:** MobileSAM is reported to be **~5× faster than FastSAM and ~7× smaller**, while retaining quality close to SAM1 for many tasks. ([kornia.readthedocs.io][20])
* **Latency:** ~10 ms per image on a single GPU (≈8 ms encoder + 4 ms decoder) in the authors’ benchmarks. ([kornia.readthedocs.io][20])

Use it when: you need **near-SAM quality but truly lightweight**, especially for **mobile / embedded / CPU-heavy** scenarios.

---

## 3. [RT-DETR](./rt_detr.ipynb) – DETR-style real-time detector

RT-DETR (“Real-Time DEtection TRansformer”) is *not* a YOLO; it’s a DETR-style **transformer detector** that aims to be **end-to-end and real-time**. ([arXiv][21])

* **Architecture:**

  * conv backbone + **efficient hybrid encoder** (decouples intra-scale interaction and cross-scale fusion) to process multi-scale features,
  * transformer decoder with a **fixed number of object queries**,
  * **NMS-free** by design (DETR paradigm). ([Ultralytics Docs][22])
* **Tricks:**

  * **IoU-aware query selection** for good query initialization,
  * adjustable number of decoder layers to trade speed vs accuracy *without retraining*. ([Ultralytics Docs][22])
* **Claim:** “DETRs beat YOLOs on real-time object detection” – i.e., RT-DETR can match or surpass many YOLOs in speed+accuracy on GPUs. ([arXiv][21])

Use it when: you want an **end-to-end transformer detector**, especially on GPU/TensorRT, and you’re okay with DETR-style training.

---

## 4. How they compare (big picture)

### 4.1 Task & output

| Model family | Primary task                          | NMS?             | Open-vocab / prompts?                          | Video-native?    |
| ------------ | ------------------------------------- | ---------------- | ---------------------------------------------- | ---------------- |
| YOLOv8–12    | Object detection (+seg/pose variants) | Usually yes      | **No**, fixed label set                        | No               |
| YOLO-World   | Object detection                      | Yes              | **Text open-vocab**                            | No               |
| YOLOE        | Det + seg                             | No extra vs YOLO | **Text + visual prompts, open-vocab or fixed** | No (image-based) |
| SAM1         | Image segmentation                    | N/A (seg)        | Promptable (points/boxes/masks)                | No               |
| SAM2         | Image + **video** segmentation        | N/A              | Promptable, with **streaming memory**          | **Yes**          |
| FastSAM      | Image segmentation                    | N/A              | Promptable                                     | No               |
| MobileSAM    | Image segmentation                    | N/A              | Promptable                                     | No               |
| RT-DETR      | Object detection                      | **No** (DETR)    | No (closed-set; though can be adapted)         | No               |

---

### 4.2 Architecture style

* **CNN-centric detectors:** YOLOv8, YOLOv9 (with GELAN), YOLO11; YOLOv10 adds small self-attention but is still largely CNN. ([Ultralytics Docs][1])
* **Attention-heavy detectors:** YOLO12 (Area Attention + R-ELAN), RT-DETR (transformer encoder–decoder). ([Ultralytics Docs][8])
* **Vision–language hybrids:** YOLO-World, YOLOE (detection/seg + text/visual prompts). ([arXiv][10])
* **Large ViT segmenters:** SAM1, SAM2. ([arXiv][14])
* **Efficient SAM derivatives:** FastSAM (CNN), MobileSAM (distilled encoder). ([Ultralytics Docs][16])

---

### 4.3 Speed vs quality (very rough intuition)

* **Highest per-image segmentation quality:** SAM2 ≥ SAM1 ≫ FastSAM / MobileSAM (though MobileSAM is surprisingly close for many tasks while being much lighter). ([arXiv][15])
* **Most efficient closed-set detectors (real-time):** YOLOv10, YOLO11, RT-DETR; YOLO12 trades a bit of speed for extra accuracy; YOLOv8 is a bit older but still good. ([Ultralytics Docs][4])
* **Open-vocabulary:** YOLO-World & YOLOE give strong zero-shot mAP while staying close to YOLOv8/10 speed; SAM2 can also act like open-vocab if you wrap it with CLIP/text prompts, but that’s not its native interface. ([Ultralytics Docs][9])

---

## 5. “Which one should I use?” (practical cheat-sheet)

### If your main task is **object detection** (bounding boxes)

* **Simple closed-set, real-time, production:**
  → **YOLO11** (pick `n/s/m/l/x` based on your compute).

* **You want NMS-free, ultra-low latency:**
  → **YOLOv10** or **RT-DETR**

  * YOLOv10 is closer to traditional YOLO;
  * RT-DETR is transformer-style and shines on GPU/TensorRT.

* **Chasing CNN accuracy / theory:**
  → **YOLOv9** (PGI + GELAN) or **YOLO12** (attention-centric).

* **Need open-vocabulary detection (classes defined at runtime via text):**
  → **YOLO-World** (det only) or **YOLOE** (det + seg + prompts).

---

### If your main task is **segmentation**

* **Image + video, high quality, interactive tools:**
  → **SAM2** (current top-dog, with streaming memory for videos).

* **Image-only, maximum zero-shot quality, okay with heavy model:**
  → **SAM1** (original Segment Anything).

* **Need “segment anything” but must run fast on modest GPU / CPU:**
  → **MobileSAM** if you can; if not available, **FastSAM** as a simpler CNN alternative.

* **Need *detection + segmentation* in one promptable model:**
  → **YOLOE** (open-prompt det + seg)
  → or a combination like **YOLO-World + SAM(2)** if you prefer to separate detection and segmentation.

---

- Powered by ChatGPT

[1]: https://docs.ultralytics.com/models/yolov8/?utm_source=chatgpt.com "Explore Ultralytics YOLOv8"
[2]: https://arxiv.org/abs/2402.13616?utm_source=chatgpt.com "YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information"
[3]: https://docs.ultralytics.com/models/yolov9/?utm_source=chatgpt.com "YOLOv9: A Leap Forward in Object Detection Technology"
[4]: https://docs.ultralytics.com/models/yolov10/?utm_source=chatgpt.com "YOLOv10: Real-Time End-to-End Object Detection"
[5]: https://arxiv.org/abs/2405.14458?utm_source=chatgpt.com "YOLOv10: Real-Time End-to-End Object Detection"
[6]: https://docs.ultralytics.com/models/yolo11/?utm_source=chatgpt.com "Ultralytics YOLO11"
[7]: https://www.ultralytics.com/blog/all-you-need-to-know-about-ultralytics-yolo11-and-its-applications?utm_source=chatgpt.com "Ultralytics YOLO11: Fast & Accurate Vision AI"
[8]: https://docs.ultralytics.com/models/yolo12/?utm_source=chatgpt.com "YOLO12: Attention-Centric Object Detection"
[9]: https://docs.ultralytics.com/models/yolo-world/?utm_source=chatgpt.com "YOLO-World Model"
[10]: https://arxiv.org/abs/2401.17270?utm_source=chatgpt.com "YOLO-World: Real-Time Open-Vocabulary Object Detection"
[11]: https://arxiv.org/abs/2503.07465?utm_source=chatgpt.com "[2503.07465] YOLOE: Real-Time Seeing Anything"
[12]: https://github.com/THU-MIG/yoloe?utm_source=chatgpt.com "YOLOE: Real-Time Seeing Anything [ICCV 2025]"
[13]: https://github.com/THU-MIG/yolov10?utm_source=chatgpt.com "THU-MIG/yolov10"
[14]: https://arxiv.org/abs/2304.02643?utm_source=chatgpt.com "[2304.02643] Segment Anything"
[15]: https://arxiv.org/abs/2408.00714?utm_source=chatgpt.com "SAM 2: Segment Anything in Images and Videos"
[16]: https://docs.ultralytics.com/models/fast-sam/?utm_source=chatgpt.com "Fast Segment Anything Model (FastSAM)"
[17]: https://blog.roboflow.com/how-to-use-segment-anything-model-sam/?utm_source=chatgpt.com "How to Use the Segment Anything Model (SAM)"
[18]: https://docs.ultralytics.com/models/mobile-sam/?utm_source=chatgpt.com "Mobile Segment Anything (MobileSAM)"
[19]: https://github.com/ChaoningZhang/MobileSAM?utm_source=chatgpt.com "ChaoningZhang/MobileSAM: This is the official code for ..."
[20]: https://kornia.readthedocs.io/en/latest/models/mobile_sam.html?utm_source=chatgpt.com "Faster Segment Anything (MobileSAM) - Kornia"
[21]: https://arxiv.org/abs/2304.08069?utm_source=chatgpt.com "DETRs Beat YOLOs on Real-time Object Detection"
[22]: https://docs.ultralytics.com/models/rtdetr/?utm_source=chatgpt.com "Baidu's RT-DETR: A Vision Transformer-Based Real-Time ..."


----

### References:


- ***Blog***:
  - ....

- ***Github***:
  - ....
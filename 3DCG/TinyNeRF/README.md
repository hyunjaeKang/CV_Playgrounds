# TinyNeRF

### Setup a conda environment

- Conda env : [gsplat](../gsplat/README.md#setup-a-conda-environment)

---

## 1. Overview of Methods

### [**NeRF (Original, 2020)**](00_NERF.ipynb)
- Core idea: Neural network mapping (3D coords + viewing direction → color + density).
- Pros: Very high-quality novel view synthesis.
- Cons: Training takes days, rendering seconds per frame.

### [**FastNeRF (2021)**](01_FastNeRF.ipynb)
- Goal: Accelerate NeRF rendering.
- Technique: Decomposes MLP into two functions (position, view), caches results in lookup tables.
- Pros: Real-time rendering.
- Cons: High memory usage.

### [**KiloNeRF (2021)**](02_KiloNeRF.ipynb)
- Goal: Speed up NeRF.
- Technique: Thousands of small MLPs (local regions).
- Pros: Parallelized fast rendering.
- Cons: Training complexity.

### [**PlenOctrees (2021)**](03_PlenOctreesNeRF.ipynb)
- Goal: Real-time rendering post-training.
- Technique: Converts NeRF into sparse octree with spherical harmonics.
- Pros: Extremely fast rendering.
- Cons: Needs conversion, not fully differentiable.

### [**Plenoxels (2022)**](04_PlenoxelsNeRF.ipynb)
- Goal: Fast training.
- Technique: Sparse voxel grid with spherical harmonics (no MLP).
- Pros: Training in minutes, competitive rendering.
- Cons: Memory-heavy.

### [**InfoNeRF (2022)**](05_InfoNeRF.ipynb)
- Goal: Few-shot / sparse input NeRF.
- Technique: Info-theoretic regularization (mutual information).
- Pros: Works with few images.
- Cons: Slower training.

### [**Instant-NGP / Instant NeRF (2022)**](06_InstantNERF.ipynb)
- Goal: Drastically accelerate.
- Technique: Multi-resolution hash encoding + tiny CUDA MLP.
- Pros: Training in seconds-minutes, real-time rendering.
- Cons: Specialized GPU implementation.

### [**K-Planes / K-Plan NeRF (2023)**](07_K-plan_NERF.ipynb)
- Goal: Scale to large / dynamic scenes.
- Technique: Scene partitioning with shared priors.
- Pros: Works for bigger, complex scenes.
- Cons: Pipeline complexity.

### [**FreeNeRF (2023)**](08_FreeNERF.ipynb)
- Goal: Sparse input robustness.
- Technique: Geometry regularization + self-distillation.
- Pros: Better with few input views.
- Cons: Not as high fidelity as dense NeRF.


---

## 2. Comparison Table

| Variant             | Focus                | Speed | Memory | Training data needs | Notes |
|---------------------|----------------------|-------|--------|---------------------|-------|
| **NeRF (original)** | Quality baseline     | Slow  | Low    | Moderate            | Benchmark |
| **FastNeRF**        | Fast rendering       | Fast  | High   | Same as NeRF        | Lookup-heavy |
| **KiloNeRF**        | Fast rendering       | Fast  | Medium | Same as NeRF        | Many small MLPs |
| **PlenOctrees**     | Real-time rendering  | Very fast | Medium | Same as NeRF | Conversion needed |
| **Plenoxels**       | Fast training        | Fast  | High   | Same as NeRF        | No MLP |
| **InfoNeRF**        | Sparse input         | Slow  | Medium | Few-shot            | Info regularization |
| **Instant NeRF**    | Speed (train+render) | Very fast | Low   | Same as NeRF        | Hash encoding |
| **K-Planes**        | Large-scale scenes   | Medium| Medium | Many inputs         | Scene partitioning |
| **FreeNeRF**        | Sparse input         | Medium| Medium | Few-shot            | Self-distillation |


---

## 3. Timeline of Methods

- **2020** — NeRF (original) published. Baseline high-quality results, very slow.  
- **2021** — FastNeRF, KiloNeRF, PlenOctrees introduce **acceleration** methods.  
- **2022** — Plenoxels, InfoNeRF, Instant-NGP: focus on **faster training** and **sparse input robustness**.  
- **2023** — K-Planes, FreeNeRF, MM-NeRF: scaling to **larger scenes, sparse input, and multi-modal data**.  

---

## 4. Speed vs Quality Trade-off Visualization

The following scatter plot (from the accompanying notebook) shows approximate **relative trade-offs (1–10 scale)**:

- **X-axis = Speed (training+rendering).**
- **Y-axis = Quality (photorealism).**

![NeRF Trade-off Plot](nerf_tradeoff.png)

---


*Note:* The numeric values for speed and quality are **relative approximations** for visualization purposes only, based on reported trends in the literature, not measured benchmarks.

 
---
### Reference:


- ***Papers***:
    - ...

- ***Blog***:
    - ...

- ***Github***:
    - [Papers-in-100-Lines-of-Code](https://github.com/MaximeVandegar/Papers-in-100-Lines-of-Code/tree/main)
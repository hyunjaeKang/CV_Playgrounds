
# Image Generation Metrics: PSNR, SSIM, LPIPS

This document explains and compares three commonly used metrics for evaluating image generation or restoration quality.

---

## **1. PSNR (Peak Signal-to-Noise Ratio)**
- **What it measures:**
  Pixel-level fidelity between the generated image and the reference image.
  It measures the ratio of maximum possible signal (pixel value range) to the noise (MSE between two images).

- **Formula:**
  \[
  \text{PSNR} = 10 \cdot \log_{10} \left(\frac{MAX_I^2}{MSE}\right)
  \]
  where \( MAX_I \) is the maximum possible pixel value (e.g., 255 for 8-bit images).

- **Interpretation:**
  - **Higher PSNR = better pixel-wise match.**
  - Sensitive to small pixel differences, even if imperceptible to the human eye.
  - Doesn’t reflect perceptual quality well (e.g., a blurry image may have higher PSNR than a sharp one).

- **Strengths:** Simple, fast, mathematically interpretable.
- **Weaknesses:** Poor correlation with human perception.

---

## **2. SSIM (Structural Similarity Index Measure)**
- **What it measures:**
  Perceptual similarity based on *luminance, contrast, and structure* of local image patches.

- **Formula (simplified):**
  \[
  SSIM(x, y) = \frac{(2\mu_x\mu_y + C_1)(2\sigma_{xy} + C_2)}{(\mu_x^2 + \mu_y^2 + C_1)(\sigma_x^2 + \sigma_y^2 + C_2)}
  \]
  where \(\mu\), \(\sigma\), and \(\sigma_{xy}\) represent local means, variances, and covariance.

- **Interpretation:**
  - Range: \([-1, 1]\), often normalized to [0, 1].
  - **Higher SSIM = images have more similar structure.**
  - Better aligned with human perception than PSNR.

- **Strengths:** Captures structural and perceptual similarity.
- **Weaknesses:** Still limited — struggles with perceptual realism.

---

## **3. LPIPS (Learned Perceptual Image Patch Similarity)**
- **What it measures:**
  *Perceptual similarity* using deep neural network features.
  Instead of comparing pixels, it compares deep feature activations (from networks like AlexNet, VGG, etc.).

- **How it works:**
  - Pass both images through a pretrained network.
  - Extract intermediate feature maps.
  - Compute distance between features (weighted by learned parameters).

- **Interpretation:**
  - Range: [0, ∞), where **lower LPIPS = more perceptually similar**.
  - Strongly correlates with human judgments of image quality.

- **Strengths:** Closest to human perception, captures semantics and texture.
- **Weaknesses:** Heavier to compute, depends on pretrained models.

---

## **Comparison Table**

| Metric | Type | Measures | Pros | Cons | Best Use Case |
|--------|------|----------|------|------|---------------|
| **PSNR** | Pixel-level | Signal fidelity (MSE-based) | Simple, fast, interpretable | Poor perceptual correlation | Compression, noise removal |
| **SSIM** | Perceptual (handcrafted) | Structure, luminance, contrast | Better than PSNR, patch-based | Limited realism perception | Image restoration, quality assessment |
| **LPIPS** | Perceptual (learned) | Feature-level perceptual similarity | Strong correlation with human judgment, semantic awareness | More costly, model-dependent | GAN evaluation, generative models, perceptual tasks |

---

## **Visual Example**

We compare three images:

<img src="./data/PNR_SNR.png>
1. **Blurry Image** – looks perceptually worse, but PSNR/SSIM report good similarity.
2. **Shifted Image** – looks perceptually fine, but PSNR/SSIM report poor similarity due to misalignment.

| Image | PSNR | SSIM | Human Perception | LPIPS (expected) |
|-------|------|------|------------------|------------------|
| Blurry | High | Decent | Bad (loss of detail) | High (bad) |
| Shifted | Low | Low | Okay (just shifted) | Low (good) |

This shows why **LPIPS** is valuable: it judges similarity more like humans, penalizing blur and texture loss while being tolerant to shifts.

---

## **Key Takeaways**
- **PSNR/SSIM**: Good for pixel-accurate tasks (compression, medical imaging).
- **LPIPS**: Better for generative/perceptual tasks (GANs, super-resolution, inpainting).


---

Powered by ChatGPT
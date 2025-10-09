# Diffusion vs Flowmatching

----
## Summary 

### Key Concepts

#### Diffusion Models

-   Work by **adding noise gradually** to data via a forward process until the data becomes pure noise (often Gaussian).
-   Then learn to **reverse** this noising process to generate new data ("denoising").
-   This reversal can be expressed via stochastic differential equations (SDEs), and models like DDPM predict the noise component at each step.
-   Training is often via a variant of variational bound (negative log likelihood), often simplified to mean-squared error (MSE) of predicted noise vs true noise.

#### Flow Matching

-   Builds on **continuous normalizing flows (CNFs)**: instead of stochastic noise addition, it defines a continuous velocity field that transforms one distribution into another.
-   A velocity field vθ(x, t) gives at each point in space/time a direction and speed ("how a particle should move"). If you follow it from t=0 to t=1, you map noise to data.
-   It ensures certain properties: deterministic paths (no randomness in the transformation once you specify the velocity field), invertibility (you can reverse the flow), and conservation of probability mass (via continuity equation).
-   Training involves supervising the model to match a *reference path* or *reference velocity field* between the noise distribution and the data distribution. The loss is often based on MSE between predicted velocities and target velocities along this path.

### Comparison: Similarities & Differences

|   Feature           |  Diffusion Models       |Flow Matching|
| --- | --- | --- |
| **Path / Process** | Fixed, stochastic path (noise schedule). | Flexible paths defined ahead of time (could be linear, curved, or learned)
| **Training Objective** | Estimate densities or noise; often involves estimating scores / reverse process; sometimes complex training dynamics. | Directly supervise velocity field; simpler MSE objectives; often more stable. |
| **Sampling Efficiency** | Lots of steps, many function evaluations (e.g. 1000+ steps) unless optimized (e.g. DDIM). | Can often use fewer steps (10–100) especially with higher-order ODE solvers.|
| **Theoretical Guarantees** | Strong connections to score-based models; likelihood bounds etc. | Under certain conditions, exact matching of densities; more direct route via ODEs. |

### Practical Considerations & Examples

-   Simple 1D illustrative experiment shows how each approach works in
    practice.
-   Code‐sketches included for both diffusion and flow matching.
-   Real-world models:
    -   **Diffusion**: DDPM, DDIM, Stable Diffusion, DALL‑E 2, Imagen.
    -   **Flow matching**: Conditional Flow Matching (CFM), Consistency
        Models, SiT (Score in Time).

### Takeaways & Intuition

-   Diffusion models = add noise to data, then learn to reverse the
    process.
-   Flow matching = define velocity field that smoothly maps noise to
    data.
-   Flow matching aims to combine diffusion's expressiveness with
    greater flexibility and efficiency.

----

### Reference:


- ***Papers***:
    - Ho, J., Jain, A., & Abbeel, P. (2020). “Denoising diffusion probabilistic models.”
    - Song, Y., Sohl-Dickstein, J., Kingma, D. P., Kumar, A., Ermon, S., & Poole, B. (2021). “Score-based generative modeling through stochastic differential equations.”
    - Lipman, Y., Cohen-Or, D., & Chen, R. (2022). “Flow matching for generative modeling.”
    - Tong, A., Huang, J., Wolf, G., van dn Driessche, D., & Balasubramanian, K. (2023). “Conditional flow matching: Simulation-free dynamic optimal transport.”
    - Song, Y., Durkan, C., Murray, I., & Ermon, S. (2021). “Maximum likelihood training of score-based diffusion models.”

- ***Blog***:
    - https://harshm121.medium.com/flow-matching-vs-diffusion-79578a16c510

- ***Github***:
    - https://github.com/harshm121/Diffusion-v-FlowMatching

---

Powered by ChatGPT
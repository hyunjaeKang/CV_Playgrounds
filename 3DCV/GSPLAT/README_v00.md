# GSplat


----

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
 pip install ipykernel ipywidgets gdown torchcodec av torchshow
 ```

---


### Notebooks for gsplat
- **3DGS Methods**[[link](../../Docs/3DGS_4Methods.md)] : Default, 3DGUT, MCMC, 2DGS

| Notebook | Data | Rendered Video |
| ------ | -----  | ---- |
|[fit_a_single_image.ipynb](./fit_a_single_image.ipynb) | [sunset](./data/sunset.jpeg) , [swim_pool](./data/swim_pool.jpeg) | [sunset](https://drive.google.com/file/d/1-3fvl3c3ahd9XUBoc-AAahtHR3nrWWh8/view?usp=sharing), [swim_pool](https://drive.google.com/file/d/19tS8uJuz4yjw70IwBvK265d9QmRrAVpL/view?usp=sharing) |
|[fit_a_colmap_capture_garden.ipynb](./fit_a_colmap_capture_garden.ipynb) | 360_V2 (garden) | - |
|[fit_a_colmap_capture_bilarf_data.ipynb](./fit_a_colmap_capture_bilarf_data.ipynb) |bilarf dataset | - |
|[fit_a_colmap_capture_zipnerf.ipynb](./fit_a_colmap_capture_zipnerf.ipynb) | zipnerf dataset | - |
|[fit_a_colmap_capture_custom_data_00.ipynb](./fit_a_colmap_capture_custom_data_00.ipynb) | [waikiki_statue](https://drive.google.com/file/d/1v_r7gjiomJNwemsXKaaJNpcTCFKl-Nbj/view?usp=sharing) | [waikiki_statue](https://drive.google.com/file/d/1uROK8E-OUDMJsjC9elP0-Y_3CspgfvpQ/view?usp=sharing) |
|[fit_a_colmap_capture_custom_data_01.ipynb](./fit_a_colmap_capture_custom_data_01.ipynb) | [duke_statue](https://drive.google.com/file/d/1fFvegLaEc_pGmputDUD6InIQFf8auEC1/view?usp=sharing) | [duke_statue](https://drive.google.com/file/d/11Mhuofe22Z-TigPum_pbRNcPDKooxUrS/view?usp=sharing)|
|[fit_a_colmap_capture_custom_data_02.ipynb](./fit_a_colmap_capture_custom_data_02.ipynb) | [hanauma_bay](https://drive.google.com/file/d/1eNb_GkkOKUSq_6cS8g4_cuPJ9CZvPBkQ/view?usp=sharing) | [hanauma_bay](https://drive.google.com/file/d/1x5Q5YphHqtqVi4GzE_0xyEKhiIqLEwQj/view?usp=sharing) |
|[fit_a_colmap_capture_custom_data_03.ipynb](./fit_a_colmap_capture_custom_data_03.ipynb) | [Celebrity_Gym](https://drive.google.com/file/d/1jx1jtZQnxe1lmzzKQTBKuffmic4Did62/view?usp=sharing) | [Celebrity_Gym](https://drive.google.com/file/d/1UQZVehz2ue7EVPIXWfUKTTBQEIHKEPRj/view?usp=sharing)|
|[fit_a_colmap_capture_custom_data_04.ipynb](./fit_a_colmap_capture_custom_data_04.ipynb) | [Celebrity_Edge_GradPlaza](https://drive.google.com/file/d/1T6naoj4bNRZOdoKjLmI3WAd1cp-NBCTR/view?usp=sharing) |[Celebrity_Edge_GradPlaza](https://drive.google.com/file/d/1ZWzRsRJi6EcpCElUU5sU8gkSCan5XVGF/view?usp=sharing) |
|[fit_a_colmap_capture_custom_data_05.ipynb](./fit_a_colmap_capture_custom_data_05.ipynb) | [Celebrity_Edge_GradPlaza_2](https://drive.google.com/file/d/1SnKE3e-2EDU1ocYfDes3GIC4Zmmd4rSI/view?usp=sharing) |[Celebrity_Edge_GradPlaza_2](https://drive.google.com/file/d/1I8w8KmTyd51QEgVcvMMuB5y5Z5RiqYKe/view?usp=sharing) |
|[fit_a_colmap_capture_custom_data_06.ipynb](./fit_a_colmap_capture_custom_data_06.ipynb) | [WhitePass_Train](https://drive.google.com/file/d/1LdXaVkme3egIwiMMevApDnwZcMUv0VvK/view?usp=sharing) |[WhitePass_Train](https://drive.google.com/file/d/1d97aLz4nj5GwVz94YR11SScAbuDSu44v/view?usp=sharing) |
|[fit_a_colmap_capture_custom_data_07.ipynb](./fit_a_colmap_capture_custom_data_07.ipynb) | [Alaska_00](https://drive.google.com/file/d/1LCjjapYzev3hbvaiOY28EIU53OkEvNqt/view?usp=sharing) |[Alaska_00](https://drive.google.com/file/d/1e4kpLT8xHDGL33naoeTXYEYzUnGWeMbk/view?usp=sharing) |



- **Rendered a video using GSPLAT(3DGS, 3DGUT, 3DGS-MCMC, 2DGS) on custom datasets**

<table border="1">
  <thead>
    <tr>
      <th style="text-align: center;">Source Video</th>
      <th style="text-align: center;">Rendered Video (3DGS, 3DGUT, 3DGS-MCMC, 2DGS)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1v_r7gjiomJNwemsXKaaJNpcTCFKl-Nbj" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1v_r7gjiomJNwemsXKaaJNpcTCFKl-Nbj" width="250" height="200" alt="Source Video 1">
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1uROK8E-OUDMJsjC9elP0-Y_3CspgfvpQ" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1uROK8E-OUDMJsjC9elP0-Y_3CspgfvpQ" width="600" height="200" alt="Rendered Video 1">
      </a>
      </td>
    </tr>
    <tr>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1fFvegLaEc_pGmputDUD6InIQFf8auEC1" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1fFvegLaEc_pGmputDUD6InIQFf8auEC1" width="250" height="200" alt="Source Video 2">
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/11Mhuofe22Z-TigPum_pbRNcPDKooxUrS" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=11Mhuofe22Z-TigPum_pbRNcPDKooxUrS" width="600" height="200" alt="Rendered Video 2">
      </a>
      </td>
    </tr>
    <tr>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1eNb_GkkOKUSq_6cS8g4_cuPJ9CZvPBkQ" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1eNb_GkkOKUSq_6cS8g4_cuPJ9CZvPBkQ" width="250" height="200" alt="Source Video 3">
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1x5Q5YphHqtqVi4GzE_0xyEKhiIqLEwQj" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1x5Q5YphHqtqVi4GzE_0xyEKhiIqLEwQj" width="600" height="200" alt="Rendered Video 3">
      </a>
      </td>
    </tr>
    <tr>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1jx1jtZQnxe1lmzzKQTBKuffmic4Did62" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1jx1jtZQnxe1lmzzKQTBKuffmic4Did62" width="250" height="200" alt="Source Video 4">
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1UQZVehz2ue7EVPIXWfUKTTBQEIHKEPRj" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1UQZVehz2ue7EVPIXWfUKTTBQEIHKEPRj" width="600" height="200" alt="Rendered Video 4">
      </a>
      </td>
    </tr>
    <tr>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1T6naoj4bNRZOdoKjLmI3WAd1cp-NBCTR" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1T6naoj4bNRZOdoKjLmI3WAd1cp-NBCTR" width="250" height="200" alt="Source Video 5">
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1ZWzRsRJi6EcpCElUU5sU8gkSCan5XVGF" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1ZWzRsRJi6EcpCElUU5sU8gkSCan5XVGF" width="600" height="200" alt="Rendered Video 5">
      </a>
      </td>
    </tr>
    <tr>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1SnKE3e-2EDU1ocYfDes3GIC4Zmmd4rSI" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1SnKE3e-2EDU1ocYfDes3GIC4Zmmd4rSI" width="250" height="200" alt="Source Video 6">
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1I8w8KmTyd51QEgVcvMMuB5y5Z5RiqYKe" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1I8w8KmTyd51QEgVcvMMuB5y5Z5RiqYKe" width="600" height="200" alt="Rendered Video 6">
      </a>
      </td>
    </tr>
    <tr>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1LdXaVkme3egIwiMMevApDnwZcMUv0VvK" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1LdXaVkme3egIwiMMevApDnwZcMUv0VvK" width="250" height="200" alt="Source Video 7">
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1d97aLz4nj5GwVz94YR11SScAbuDSu44v" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1d97aLz4nj5GwVz94YR11SScAbuDSu44v" width="600" height="200" alt="Rendered Video 7">
      </a>
      </td>
    </tr>
    <tr>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1LCjjapYzev3hbvaiOY28EIU53OkEvNqt" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1LCjjapYzev3hbvaiOY28EIU53OkEvNqt" width="250" height="200" alt="Source Video 8">
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1e4kpLT8xHDGL33naoeTXYEYzUnGWeMbk" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1e4kpLT8xHDGL33naoeTXYEYzUnGWeMbk" width="600" height="200" alt="Rendered Video 8">
      </a>
      </td>
    </tr>
  </tbody>
</table>


---
### References:


- ***Paper***:
    - [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_high.pdf)
    - [3D Gaussian Splatting as Markov Chain Monte Carlo](https://arxiv.org/abs/2404.09591?utm_source=chatgpt.com)
    - [3D Gaussian Splatting as Markov Chain Monte Carlo - NIPS papers](https://proceedings.neurips.cc/paper_files/paper/2024/file/93be245fce00a9bb2333c17ceae4b732-Paper-Conference.pdf?utm_source=chatgpt.com)
    - [3D Gaussian Splatting as Markov Chain Monte Carlo - OpenReview](https://openreview.net/forum?id=UCSt4gk6iX&utm_source=chatgpt.com)
    - [2D Gaussian Splatting for Geometrically Accurate Radiance Fields](https://arxiv.org/abs/2403.17888?utm_source=chatgpt.com)
    - [2D Gaussian Splatting for Geometrically Accurate Radiance Fields](https://surfsplatting.github.io/assets/paper/paper.pdf?utm_source=chatgpt.com)
    - [Anti-Aliased 2D Gaussian Splatting](https://arxiv.org/abs/2506.11252?utm_source=chatgpt.com )
    - [3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507?utm_source=chatgpt.com )

- ***Blog***:
    - [3D Gaussian Splatting Introduction – Paper Explanation & Training on Custom Datasets with NeRF Studio Gsplats](https://learnopencv.com/3d-gaussian-splatting/)
    - [gsplat documentation](https://docs.gsplat.studio/main/index.html)

- ***Github***:
    - [gsplat](https://github.com/nerfstudio-project/gsplat/tree/main)
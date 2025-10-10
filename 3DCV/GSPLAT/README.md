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

- **Image rendering with 3DGS on custom images** ([Notebook](https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/GSPLAT/fit_a_single_image.ipynb))

<table  border="1">
  <thead>
    <tr>
      <th style="text-align: center;" >Source image</th>
      <th style="text-align: center;" >Image fitting(iteration : 1000)</th>
      <th style="text-align: center;" >Image fitting(iteration : 100000)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
    <th style="text-align: center; padding: 10px;" >
      <img src="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/GSPLAT/data/sunset.jpeg?raw=true" width="200px" height="150px">
    </th>
    <!-- <th style="text-align: center; padding: 10px;">
      <video width="200" height="150" controls><source src="https://github.com/hyunjaeKang/CV_Playgrounds/raw/main/3DCV/GSPLAT/output/sunset_100000_1000_3dgs.mp4" type="video/mp4"></video>
    </th>
    <th style="text-align: center; padding: 10px;">
    <video width="200" height="150" controls><source src="https://github.com/hyunjaeKang/CV_Playgrounds/raw/main/3DCV/GSPLAT/output/sunset_100000_100000_3dgs.mp4" type="video/mp4"></video>
    </th> -->
    <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/18KpAqVANjl0BGcq0x4rwWhGChR7yMC2g" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=18KpAqVANjl0BGcq0x4rwWhGChR7yMC2g" width="200" height="150" alt="Source Video 1">
      </a>
    </td>
    <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1-3fvl3c3ahd9XUBoc-AAahtHR3nrWWh8" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1-3fvl3c3ahd9XUBoc-AAahtHR3nrWWh8" width="200" height="150" alt="Source Video 1">
      </a>
    </td>
    </tr>
  </tbody>
  <tbody>
    <tr>
    <th style="text-align: center; padding: 10px;" >
      <img src="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/GSPLAT/data/swim_pool.jpeg?raw=true" width="200px" height="150px">
    </th>
    <!-- <th style="text-align: center; padding: 10px;">
    <video width="200" height="150" controls><source src="https://github.com/hyunjaeKang/CV_Playgrounds/raw/main/3DCV/GSPLAT/output/swim_pool_100000_1000_3dgs.mp4" type="video/mp4"></video>
    </th>
    <th style="text-align: center; padding: 10px;">
    <video width="200" height="150" controls><source src="https://github.com/hyunjaeKang/CV_Playgrounds/raw/main/3DCV/GSPLAT/output/swim_pool_100000_100000_3dgs.mp4" type="video/mp4"></video>
    </th> -->
    <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1VJ2cKaiCaHWM3d4r2Vf6UiEtBQDQPIjX" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1VJ2cKaiCaHWM3d4r2Vf6UiEtBQDQPIjX" width="200" height="150" alt="Source Video 1">
      </a>
    </td>
    <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/19tS8uJuz4yjw70IwBvK265d9QmRrAVpL" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=19tS8uJuz4yjw70IwBvK265d9QmRrAVpL" width="200" height="150" alt="Source Video 1">
      </a>
    </td>
    </tr>
  </tbody>
</table>


- **Rendered a video using GSPLAT(3DGS, 3DGUT, 3DGS-MCMC, 2DGS) on custom datasets**


<table border="1">
  <thead>
    <tr>
      <th style="text-align:center;padding:10px;">Notebook</th>
      <th style="text-align: center;">Source Video</th>
      <th style="text-align: center;">Rendered Video (3DGS, 3DGUT, 3DGS-MCMC, 2DGS)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:center;padding:10px;">
      <a href="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/GSPLAT/fit_a_colmap_capture_custom_data_00.ipynb" target="_blank">
        Statue1
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1v_r7gjiomJNwemsXKaaJNpcTCFKl-Nbj" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1v_r7gjiomJNwemsXKaaJNpcTCFKl-Nbj" width="150" height="130" alt="Source Video 1">
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1uROK8E-OUDMJsjC9elP0-Y_3CspgfvpQ" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1uROK8E-OUDMJsjC9elP0-Y_3CspgfvpQ" width="600" height="130" alt="Rendered Video 1">
      </a>
      </td>
    </tr>
    <tr>
    <td style="text-align:center;padding:10px;">
      <a href="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/GSPLAT/fit_a_colmap_capture_custom_data_01.ipynb" target="_blank">
        Statue2
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1fFvegLaEc_pGmputDUD6InIQFf8auEC1" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1fFvegLaEc_pGmputDUD6InIQFf8auEC1" width="150" height="130" alt="Source Video 2">
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/11Mhuofe22Z-TigPum_pbRNcPDKooxUrS" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=11Mhuofe22Z-TigPum_pbRNcPDKooxUrS" width="600" height="130" alt="Rendered Video 2">
      </a>
      </td>
    </tr>
    <tr>
    <td style="text-align:center;padding:10px;">
      <a href="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/GSPLAT/fit_a_colmap_capture_custom_data_02.ipynb" target="_blank">
        Bay
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1eNb_GkkOKUSq_6cS8g4_cuPJ9CZvPBkQ" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1eNb_GkkOKUSq_6cS8g4_cuPJ9CZvPBkQ" width="150" height="130" alt="Source Video 3">
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1x5Q5YphHqtqVi4GzE_0xyEKhiIqLEwQj" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1x5Q5YphHqtqVi4GzE_0xyEKhiIqLEwQj" width="600" height="130" alt="Rendered Video 3">
      </a>
      </td>
    </tr>
    <tr>
    <td style="text-align:center;padding:10px;">
      <a href="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/GSPLAT/fit_a_colmap_capture_custom_data_03.ipynb" target="_blank">
        Gym
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1jx1jtZQnxe1lmzzKQTBKuffmic4Did62" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1jx1jtZQnxe1lmzzKQTBKuffmic4Did62" width="150" height="130" alt="Source Video 4">
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1UQZVehz2ue7EVPIXWfUKTTBQEIHKEPRj" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1UQZVehz2ue7EVPIXWfUKTTBQEIHKEPRj" width="600" height="130" alt="Rendered Video 4">
      </a>
      </td>
    </tr>
    <tr>
    <td style="text-align:center;padding:10px;">
      <a href="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/GSPLAT/fit_a_colmap_capture_custom_data_04.ipynb" target="_blank">
        GradPlaza
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1T6naoj4bNRZOdoKjLmI3WAd1cp-NBCTR" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1T6naoj4bNRZOdoKjLmI3WAd1cp-NBCTR" width="150" height="130" alt="Source Video 5">
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1ZWzRsRJi6EcpCElUU5sU8gkSCan5XVGF" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1ZWzRsRJi6EcpCElUU5sU8gkSCan5XVGF" width="600" height="130" alt="Rendered Video 5">
      </a>
      </td>
    </tr>
    <tr>
    <td style="text-align:center;padding:10px;">
      <a href="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/GSPLAT/fit_a_colmap_capture_custom_data_05.ipynb" target="_blank">
        GradPlaza2
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1SnKE3e-2EDU1ocYfDes3GIC4Zmmd4rSI" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1SnKE3e-2EDU1ocYfDes3GIC4Zmmd4rSI" width="150" height="130" alt="Source Video 6">
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1I8w8KmTyd51QEgVcvMMuB5y5Z5RiqYKe" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1I8w8KmTyd51QEgVcvMMuB5y5Z5RiqYKe" width="600" height="130" alt="Rendered Video 6">
      </a>
      </td>
    </tr>
    <tr>
    <td style="text-align:center;padding:10px;">
      <a href="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/GSPLAT/fit_a_colmap_capture_custom_data_06.ipynb" target="_blank">
        WhitePass
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1LdXaVkme3egIwiMMevApDnwZcMUv0VvK" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1LdXaVkme3egIwiMMevApDnwZcMUv0VvK" width="150" height="130" alt="Source Video 7">
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1d97aLz4nj5GwVz94YR11SScAbuDSu44v" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1d97aLz4nj5GwVz94YR11SScAbuDSu44v" width="600" height="130" alt="Rendered Video 7">
      </a>
      </td>
    </tr>
    <tr>
    <td style="text-align:center;padding:10px;">
      <a href="https://github.com/hyunjaeKang/CV_Playgrounds/blob/main/3DCV/GSPLAT/fit_a_colmap_capture_custom_data_07.ipynb" target="_blank">
        Alaska
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1LCjjapYzev3hbvaiOY28EIU53OkEvNqt" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1LCjjapYzev3hbvaiOY28EIU53OkEvNqt" width="150" height="130" alt="Source Video 8">
      </a>
      </td>
      <td style="text-align:center;padding:10px;">
      <a href="https://drive.google.com/file/d/1e4kpLT8xHDGL33naoeTXYEYzUnGWeMbk" target="_blank">
        <img src="https://drive.google.com/thumbnail?id=1e4kpLT8xHDGL33naoeTXYEYzUnGWeMbk" width="600" height="130" alt="Rendered Video 8">
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
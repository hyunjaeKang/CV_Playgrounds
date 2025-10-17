# Triangle Splatting 2 Playgrounds

---
## Setup a conda environment

```

# pwd ~/CV_Playgrounds/3DCV/Triangle_splatting2
# nvcc --version 
#   nvcc: NVIDIA (R) Cuda compiler driver
#   Copyright (c) 2005-2025 NVIDIA Corporation
#   Built on Tue_May_27_02:21:03_PDT_2025
#   Cuda compilation tools, release 12.9, V12.9.86
#   Build cuda_12.9.r12.9/compiler.36037853_0

git clone https://github.com/trianglesplatting2/triangle-splatting2 temp_triangle-splatting2 --recursive
cd temp_triangle-splatting2

conda create -y -n triangle_splatting2 python=3.11
conda activate triangle_splatting2

pip install ipykernel ipywidgets gdown
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
pip install -r requirements.txt
pip install xformers

bash compile.sh
cd submodules/simple-knn
pip install .

CONDA_PREFIX=/usr/local/cuda/ cmake -S . -B build -DCMAKE_INSTALL_PREFIX="$(pwd)/triangulation" -DCMAKE_CUDA_ARCHITECTURES=75 
cmake --build build
cmake --install build
```

---


### Notebooks for triangle-splatting

| Notebook | Data | Rendered Video (Indoor Mode) | Rendered Video (Outdoor Mode) |
| ------ | -----  | ---- | --- |
|[custom_data_00.ipynb](./custom_data_00.ipynb) | [waikiki_statue](https://drive.google.com/file/d/1v_r7gjiomJNwemsXKaaJNpcTCFKl-Nbj/view?usp=sharing) | [waikiki_statue(indoor)](https://drive.google.com/file/d/1WH0_kPK39Ja1iZjJ2jwkXJVXAEN2Z5lb/view?usp=sharing) | [waikiki_statue(outdoor)](https://drive.google.com/file/d/12ANTdAqZEUAQY7YG96lhs6FfpAgZCiLk/view?usp=sharing) |
|[custom_data_01.ipynb](./custom_data_01.ipynb) | [duke_statue](https://drive.google.com/file/d/1fFvegLaEc_pGmputDUD6InIQFf8auEC1/view?usp=sharing) | [duke_statue(indoor)](https://drive.google.com/file/d/1FL6SEqq4blJNYvxZACb3u3PGYXlBh9jM/view?usp=sharing)| [duke_statue(outdoor)](https://drive.google.com/file/d/19YqW4Yfd9SDHcWb-zphkc_gY87iLNHlQ/view?usp=sharing)|
|[custom_data_02.ipynb](./custom_data_02.ipynb) | [hanauma_bay](https://drive.google.com/file/d/1eNb_GkkOKUSq_6cS8g4_cuPJ9CZvPBkQ/view?usp=sharing) | [hanauma_bay(indoor)](https://drive.google.com/file/d/1Vh8TctS-94TusRLFOAQ8fXilyKk7WXTP/view?usp=sharing) | [hanauma_bay(outdoor)](https://drive.google.com/file/d/1Qy_DpZH3YGEEWazKtRx92M46sRc1cmvI/view?usp=sharing) |
|[custom_data_03.ipynb](./custom_data_03.ipynb) | [Celebrity_Gym](https://drive.google.com/file/d/1jx1jtZQnxe1lmzzKQTBKuffmic4Did62/view?usp=sharing) | [Celebrity_Gym(indoor)](https://drive.google.com/file/d/1bEuNBgzFj34Ad2tGoFGA07N0riPO8HNR/view?usp=sharing)| [Celebrity_Gym(outdoor)](https://drive.google.com/file/d/1BR_nfmDHIWrbpHdJKLFmqfTlLAt38o4W/view?usp=sharing)|
|[custom_data_04.ipynb](./custom_data_04.ipynb) | [Celebrity_Edge_GradPlaza](https://drive.google.com/file/d/1T6naoj4bNRZOdoKjLmI3WAd1cp-NBCTR/view?usp=sharing) |~~Celebrity_Edge_GradPlaza(indoor)~~ | ~~Celebrity_Edge_GradPlaza(outdoor)~~|
|[custom_data_05.ipynb](./custom_data_05.ipynb) | [Celebrity_Edge_GradPlaza_2](https://drive.google.com/file/d/1SnKE3e-2EDU1ocYfDes3GIC4Zmmd4rSI/view?usp=sharing) |~~Celebrity_Edge_GradPlaza_2(indoor)~~| ~~Celebrity_Edge_GradPlaza_2(outdoor)~~|
|[custom_data_06.ipynb](./custom_data_06.ipynb) | [WhitePass_Train](https://drive.google.com/file/d/1LdXaVkme3egIwiMMevApDnwZcMUv0VvK/view?usp=sharing) |[WhitePass_Train(indoor)](https://drive.google.com/file/d/1XKGRM8DhulkSONttA1FLs9Ijj5P6Wr8B/view?usp=sharing) | [WhitePass_Train(outdoor)](https://drive.google.com/file/d/1OXXuCDWftfKqlmYzG5zdbckmWwSkvGxJ/view?usp=sharing) |
|[custom_data_07.ipynb](./custom_data_07.ipynb) | [Alaska_00](https://drive.google.com/file/d/1LCjjapYzev3hbvaiOY28EIU53OkEvNqt/view?usp=sharing) |[Alaska_00(indoor)](https://drive.google.com/file/d/1yQKDhrv6zM71f3BPJ6kCJEcwK2KiQBB_/view?usp=sharing) | [Alaska_00(outdoor)](https://drive.google.com/file/d/1utSsoRkDF2M_r64MPS6r1CW8ixDlTwRH/view?usp=drive_link) |


---
### Reference:


- ***Papers***:
    - [Triangle Splatting+: Differentiable Rendering with Opaque Triangles](https://arxiv.org/abs/2509.25122)

- ***Blog***:
    - https://trianglesplatting2.github.io/trianglesplatting2/

- ***Github***:
    - https://github.com/trianglesplatting2/triangle-splatting2
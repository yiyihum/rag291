---
license: cc-by-sa-4.0
task_categories:
- other
language:
- en
tags:
- indoor
- 3dgs
- pretraining
size_categories:
- 1K<n<10K
license_name: scene-splat-7k-license
pretty_name: SceneSplat-7K
configs:
- config_name: ARKitScenesGS
  data_files:
  - split: train
    path: statistics/arkitscenes_3dgs_runs.csv
- config_name: HyperSimGS
  data_files:
  - split: train
    path: statistics/hypersim_mcmc_3dgs_runs.csv
- config_name: Matterport3DGS
  data_files:
  - split: train
    path: statistics/matterport3d_region_mcmc_3dgs_runs.csv
- config_name: ReplicaGS
  data_files:
  - split: train
    path: statistics/replica_mcmc_3dgs_runs.csv
- config_name: ScanNetPPGS-V1
  data_files:
  - split: train
    path: statistics/scannetpp_v1_3dgs_runs.csv
- config_name: ScanNetPPGS-V2
  data_files:
  - split: train
    path: statistics/scannetpp_v2_3dgs_runs.csv
- config_name: ScanNetGS
  data_files:
  - split: train
    path: statistics/scannet_3dgs_runs.csv
- config_name: 3RScanGS
  data_files:
  - split: train
    path: statistics/3rscan_mcmc_3dgs_runs.csv
extra_gated_prompt: "SceneSplat-7K is built upon multiple existing 3D datasets, each\
  \ with their own licensing requirements. We've carefully structured our distribution\
  \ approach to respect all original licenses while making our dataset accessible\
  \ to the research community.\n\nBefore we are able to offer you access to the SceneSplat-7K\
  \ dataset, please agree that you will use the dataset in accordance with the original\
  \ licenses/terms.\n\nIf you find our work helpful, please consider citing our paper.\n\
  \n@inproceedings{li2025scenesplat,\n  title={SceneSplat: Gaussian Splatting-based\
  \ Scene Understanding With Vision-Language Pretraining},\n  author={Li, Yue and\
  \ Ma, Qi and Yang, Runyi and Li, Huapeng and Ma, Mengjiao and Ren, Bin and Popovic,\
  \ Nikola and Sebe, Nicu and Konukoglu, Ender and Gevers, Theo and others},\n  booktitle\
  \ = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},\n\
  \  year={2025}\n}\n"
extra_gated_fields:
  Full name: text
  Current affiliation: text
  Type of Affiliation:
    type: select
    options:
    - Academia
    - Industry
    - label: Other
      value: other
  Institutional email: text
  Please explain your intended research use: text
  I agree to all the terms outlined by original datasets: checkbox
  I agree to use this the data for non-commercial, academic purposes only: checkbox
---
# SceneSplat-7K
We propose SceneSplat-7K dataset, including indoor 3D Gaussian Splatting scenes generated from ScanNet, ScanNet++, ScanNet++ v2, Replica, Hypersim, 3RScan, ARKitScenes, and Matterport3D. The dataset in total contains **7,916 scenes** and **11.27 Billion 3DGS**. Constructing this dataset required computational resources equivalent to **150 GPU-days** on one NVIDIA L4 GPU. SceneSplat-7K achieves high-fidelity reconstruction quality with an average PSNR of **29.64 dB** and depth_l1 loss of **0.035 m**.

Please find here the links to each component of the dataset:
- [ARKitScenesGS](https://huggingface.co/datasets/GaussianWorld/arkitscenes_mcmc_3dgs_new)
- [Matterport3DGS](https://huggingface.co/datasets/GaussianWorld/matterport3d_region_mcmc_3dgs)
- [HyperSimGS](https://huggingface.co/datasets/GaussianWorld/hypersim_mcmc_3dgs)
- [ReplicaGS](https://huggingface.co/datasets/GaussianWorld/replica_mcmc_3dgs)
- [ScanNetPPGS-V1](https://huggingface.co/datasets/GaussianWorld/scannetpp_v1_mcmc_1.5M_3dgs)
- [ScanNetPPGS-V2](https://huggingface.co/datasets/GaussianWorld/scannetpp_v2_mcmc_1.5M_3dgs)
- [ScanNetGS](https://huggingface.co/datasets/GaussianWorld/scannet_mcmc_1.5M_3dgs)
- [3RScanGS](https://huggingface.co/datasets/GaussianWorld/3rscan_mcmc_3dgs)

## Data Statistics
We provide together the statistics of all the 3DGS scenes in the `statistics` folder. The statistics are saved in csv files, and include the metrics of `psnr`,`ssim`,`lpips`,`depth_l1`, and `num_GS`. With this, users could filter the scenes by appearance and geometry quality.

## Frames Metadata
We process the scenes first and obtain the per-scene metadata of all the training frames which is saved in `transforms_train.json`. Please find all the files in the `3dgs_training_views` folder. Each json is in the format of the following example. Note, only for ScanNet++ scenes, the poses are in OpenGL camera convention as in original dataset. 

<details open>
<summary>Contents of transforms_train.json</summary>

```json
{
    "share_intrinsics": false,     // usually true, if not, use per-frame intrinsics in frames
    "fx": 0,                       // placeholder if share_intrinsics is false
    "fy": 0, 
    "cx": 0,  
    "cy": 0,  
    "width": width,                     // original image size
    "height": height,  
    "zipped": false,                    // if zipped, we will load later from zip files
    "crop_edge": 0,                     // crop edge of the image if needed 
    "resize": [960, 720],               // (width, height), resize for optimization
    "frames_num": "len(frames)",        // total frames for 3DGS optimization
    "init_point_num": "init_point_num", // point clouds size used for 3DGS initialization
    "bbox_min": "bbox_min",             // bounding box of the point clouds
    "bbox_max": "bbox_max",             
    "frames": frames,                   // see below
    "test_frames": test_frames          // if not provided by dataset, random select 50

    // frames format: a list of dictionaries, each dict has the format of:
    [
        {
            "file_path": relative_path,           // image path relative to the scene folder
            "transform_matrix": transform_matrix, // 4 x 4, array.tolist(), camera-to-world pose
            "fx": intrinsics["fx"],               // needed if share_intrinsics is False
            "fy": intrinsics["fy"],
            "cx": intrinsics["cx"],
            "cy": intrinsics["cy"],
        },
        ...... // more frames
    ]
}
```
</details>

## Preprocessed Language Pretraining Data
We provide the preprocessed 3DGS vision-language pretraining data used for joint training of SceneSplat for convenience. 

- [Matterport3D](https://huggingface.co/datasets/GaussianWorld/matterport3d_region_mcmc_3dgs_preprocessed)
- [ScanNet++ V2](https://huggingface.co/datasets/GaussianWorld/scannetpp_v2_mcmc_3dgs_preprocessed)
- [ScanNet](https://huggingface.co/datasets/GaussianWorld/scannet_mcmc_3dgs_preprocessed)

For each scene, the 3DGS `*.ply` files are stored in `*.npy` files by parameters, and 3DGS language labels are stored with `lang_feat.npy` and `valid_feat_mask.npy`.

```bash
.
├── color.npy
├── coord.npy
├── opacity.npy
├── quat.npy
├── scale.npy
├── lang_feat.npy
└── valid_feat_mask.npy
```

The following subfolders are required for vision-language pretraining:
```
GaussianWorld/matterport3d_region_mcmc_3dgs_preprocessed: "train_grid1.0cm_chunk6x6_stride3x3_filtered", "val_grid1.0cm_chunk6x6_stride3x3_filtered", "test_grid1.0cm_chunk6x6_stride3x3_filtered", "test"
GaussianWorld/scannetpp_v2_mcmc_3dgs_preprocessed: "train_grid1.0cm_chunk6x6_stride3x3", "test_grid1.0cm_chunk6x6_stride3x3", "val"
GaussianWorld/scannet_mcmc_3dgs_preprocessed: "train_grid1.0cm_chunk6x6_stride3x3", "test_grid1.0cm_chunk6x6_stride3x3", "val"
```

## 2D Language Features
We provide the 2D language features extracted from the training frames of each scene, as detailed in the 3DGS Language Label Collection section in the main paper. The `<frame_id>_f.npy` saves the per-frame SigLIP2 embeddings of shape `(num_segs, 768)`, and the `<frame_id>_s.npy` saves the per-frame segmentation maps of shape `(1, H, W)`.

Released 2D language features:
- [Matterport3D](https://huggingface.co/datasets/GaussianWorld/matterport3d_region_2d_language_features)
- [ScanNet++ V2](https://huggingface.co/datasets/GaussianWorld/scannetpp_2d_language_features)
- [ScanNet](https://huggingface.co/datasets/GaussianWorld/scannet_2d_language_features)

## Data Splits
For the reported benchmark results on full evaluation scenes in the main paper, we use the official splits provided by each dataset, i.e., ScanNet `val` split (312 scenes), ScanNet++ `nvs_sem_val` split (50 scenes), Matterport3D `test` split (370 scenes). The splits files are provided in the `data_splits` folder.


## Dataset License

SceneSplat-7K is built upon multiple existing 3D datasets, each with their own licensing requirements. We've carefully structured our distribution approach to respect all original licenses while making our dataset accessible to the research community.

### Distribution Approaches

Based on each dataset's licensing terms, we employ different distribution strategies:

**Direct Distribution with Attribution**: For datasets that permit redistribution under non-commercial research purposes (ARKitScenes, Hypersim, 3RScan, Replica), we include the original data with proper attribution and license requirements.

**Hosting Through Original Platforms**: For datasets with custom terms that restrict redistribution, we've reached agreements with the original authors to host our processed 3D Gaussian Splatting scenes on their official platforms.

### License Summary

| Dataset | Original License | Allowed Purposes | Our Distribution Method |
|---------|------------------|------------------|------------------------|
| **ARKitScenes** | [Apple Software License](https://github.com/apple/ARKitScenes/blob/main/LICENSE) | Non-commercial use; modification and redistribution permitted | Direct distribution with attribution |
| **Hypersim** | [CC BY-SA 3.0](https://github.com/apple/ml-hypersim/blob/main/README.md#the-hypersim-dataset) | Free to share and adapt under Attribution-ShareAlike terms | Direct distribution with attribution |
| **3RScan** | [3RScan Terms of Use](https://docs.google.com/forms/d/e/1FAIpQLSfl9Xm1qWiGmN2HXzbRIecVns_V-n-4bwrzPEE4ZezEpOKT9Q/viewform) | Non-commercial research and educational purposes only | Direct distribution with attribution |
| **Replica** | [Replica Dataset Research Terms](https://github.com/facebookresearch/Replica-Dataset/blob/main/LICENSE) | Non-commercial research or educational purposes | Direct distribution with attribution |
| **ScanNet** | [ScanNet Terms of Use](https://kaldir.vc.in.tum.de/scannet/ScanNet_TOS.pdf) | Non-commercial research and educational purposes only | Hosted on original platform |
| **ScanNet++** | [ScanNet++ Terms of Use](https://kaldir.vc.in.tum.de/scannetpp/static/scannetpp-terms-of-use.pdf) | Non-commercial research and educational purposes only | Hosted on original platform |
| **Matterport3D** | [Matterport License Agreement for Academic Use](https://matterport.com/legal/matterport-end-user-license-agreement-academic-use-model-data) | Non-commercial academic use only | Direct distribution with attribution |

### Data Usage

When using SceneSplat-7K dataset, please ensure agreement with the following:

1. **License Compatibility**: All component datasets restrict use to non-commercial research and educational purposes.

2. **Attribution**: Proper attribution must be given to both SceneSplat-7K and all original dataset authors.

3. **Data Access**: For datasets hosted on original platforms (ScanNet, ScanNet++), you need to request access directly from those platforms.


The **3D Gaussian Splatting scenes** we provide are governed by the original dataset licenses as detailed above. Our **additional code, processing scripts, and metadata** are made available under **CC BY-SA 4.0**.

If you have any questions about licensing, please reach out to us.

## Citation
If you find our work helpful, please consider citing:
```bibtex
@inproceedings{li2025scenesplat,
  title={SceneSplat: Gaussian Splatting-based Scene Understanding With Vision-Language Pretraining},
  author={Li, Yue and Ma, Qi and Yang, Runyi and Li, Huapeng and Ma, Mengjiao and Ren, Bin and Popovic, Nikola and Sebe, Nicu and Konukoglu, Ender and Gevers, Theo and others},
  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
  year={2025}
}
```

## Acknowledgements
We sincerely thank all the author teams of the original datasets for their contributions and for making their data publicly available. Our 3DGS scenes are optimized using [gsplat](https://github.com/nerfstudio-project/gsplat) repository.
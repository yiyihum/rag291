---
base_model:
- TheDrummer/Cydonia-24B-v4.1
- Doctor-Shotgun/MS3.2-24B-Magnum-Diamond
library_name: transformers
tags:
- mergekit
- merge
license: apache-2.0
---
![Foxgirl on Cydonia](https://huggingface.co/knifeayumu/Cydonia-v4.1-MS3.2-Magnum-Diamond-24B/resolve/main/053335_WAN22_14B_I2V_00001_.webp)

# Cydonia-v4.1-MS3.2-Magnum-Diamond-24B

Recipe based on [knifeayumu/Cydonia-v1.2-Magnum-v4-22B](https://huggingface.co/knifeayumu/Cydonia-v1.2-Magnum-v4-22B). Just an update to those who are interested.

### Image to Video Generation Info

[Wan-AI/Wan2.2-I2V-A14B](https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B) was used to turn this [image from the previous merge](https://huggingface.co/knifeayumu/Cydonia-v4-MS3.2-Magnum-Diamond-24B/resolve/main/FoxGirlonCydonia.png) (slightly cropped) to an animation utilising [lightx2v/Wan2.2-Lightning](https://huggingface.co/lightx2v/Wan2.2-Lightning) for faster generation and [pollockjj/ComfyUI-MultiGPU](https://github.com/pollockjj/ComfyUI-MultiGPU) nodes.

![ComfyUI workflow](20250819_060905_821_vivaldi.png)

---
## Merge Details

This is a merge of pre-trained language models created using [mergekit](https://github.com/arcee-ai/mergekit).

### Merge Method

This model was merged using the [SLERP](https://en.wikipedia.org/wiki/Slerp) merge method.

### Models Merged

The following models were included in the merge:
* TheDrummer/Cydonia-24B-v4.1
* Doctor-Shotgun/MS3.2-24B-Magnum-Diamond

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: TheDrummer/Cydonia-24B-v4.1
  - model: Doctor-Shotgun/MS3.2-24B-Magnum-Diamond
merge_method: slerp
base_model: TheDrummer/Cydonia-24B-v4.1
parameters:
  t: [0.1, 0.3, 0.6, 0.3, 0.1]
dtype: bfloat16
```

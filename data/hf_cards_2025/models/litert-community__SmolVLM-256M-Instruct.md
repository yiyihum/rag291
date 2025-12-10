---
license: apache-2.0
base_model:
- HuggingFaceTB/SmolVLM-256M-Instruct
pipeline_tag: text-generation
tags:
- chat
---

This model provides [HuggingFaceTB/SmolVLM-256M-Instruct](https://huggingface.co/HuggingFaceTB/SmolVLM-256M-Instruct) model in TFLite format.    
You can use this model with [Custom Cpp Pipiline](https://github.com/dragynir/ai-edge-torch-smalvlm/tree/dev/ai_edge_torch/generative/examples/cpp_image) or run with python pipeline (see COLAB example below).  
Please note that, at the moment, [AI Edge Torch](https://github.com/google-ai-edge/ai-edge-torch/tree/main/ai_edge_torch/generative/examples) VLMS not supported
on [MediaPipe LLM Inference API](https://ai.google.dev/edge/mediapipe/solutions/genai/llm_inference),
for example [qwen_vl model](https://github.com/google-ai-edge/ai-edge-torch/tree/main/ai_edge_torch/generative/examples/qwen_vl),  
that was used as reference to write SmolVLM-256M-Instruct convertation scripts.


## Use the models

### Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#fileId=https://huggingface.co/litert-community/SmolVLM-256M-Instruct/blob/main/smalvlm_notebook.ipynb
)

## Cpp inference

```shell
mkdir cache

bazel run --verbose_failures -c opt //ai_edge_torch/generative/examples/cpp_image:text_generator_main -- \
--tflite_model="/home/dragynir/ai_vlm/ai-edge-torch-smalvlm/ai_edge_torch/generative/examples/smalvlm/models/SmolVLM-256M-Instruct-tflite-single/smalvlm-256m-instruct_q8_ekv2048.tflite" \
--sentencepiece_model="/home/dragynir/ai_vlm/ai-edge-torch-smalvlm/ai_edge_torch/generative/examples/smalvlm/models/SmolVLM-256M-Instruct-tflite/tokenizer.model" \
--start_token="<|im_start|>" --stop_token="<end_of_utterance>" --num_threads=16 \
--prompt="User:<image>What in the image?<end_of_utterance>\nAssistant:" --weight_cache_path="/home/dragynir/llm/ai-edge-torch/ai_edge_torch/generative/examples/cpp/cache/model.xnnpack_cache" \
--use_single_image=true --image_path="/home/dragynir/ai_vlm/car.jpg" --max_generated_tokens=64
```


## TFlite convertation

To fine-tune SmolVLM on a specific task, you can follow [the fine-tuning tutorial](https://github.com/huggingface/smollm/blob/main/vision/finetuning/Smol_VLM_FT.ipynb).  
Than, you can convert model to TFlite using custom [smalvlm scripts](https://github.com/dragynir/ai-edge-torch-smalvlm/tree/dev/ai_edge_torch/generative/examples/smalvlm) (see Readme.md).  
You can also check the official documentation [ai-edge-torch generative](https://github.com/google-ai-edge/ai-edge-torch/tree/main/ai_edge_torch/generative).



## Details

The model was converted with the following parameters:

```shell
python convert_to_tflite.py --quantize="dynamic_int8"\
 --checkpoint_path='./models/SmolVLM-256M-Instruct' --output_path="./models/SmolVLM-256M-Instruct-tflite"\
 --mask_as_input=True --prefill_seq_lens=256 --kv_cache_max_len=2048
```
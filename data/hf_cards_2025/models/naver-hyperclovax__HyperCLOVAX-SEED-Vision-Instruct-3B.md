---
license: other
license_name: hyperclovax-seed
license_link: LICENSE
library_name: transformers
---


![image/png](https://cdn-uploads.huggingface.co/production/uploads/6512d9827fccffe1e9e28fa7/Lra7yfdthGdKcNk7vP5RS.png)


## **Overview**

HyperCLOVAX-SEED-Vision-Instruct-3B is a model developed by NAVER, built upon its proprietary backbone model and fine-tuned through post-training. It is capable of understanding both text and images, as well as generating text.

The model is primarily designed with a focus on lightweight architecture, optimizing computational efficiency. In terms of visual understanding, it can handle visual question answering (VQA), chart and diagram interpretation, and even comprehend content. HyperCLOVAX-SEED-Vision-Instruct-3B aims for a Pareto-optimal balance specifically tuned for the Korean language, and it demonstrates competitive performance using fewer visual tokens compared to other models of similar size in inference scenarios.

Particularly, the model shows relative strengths in handling Korean-language inputs and outperforms similarly sized open-source models in related benchmarks. As the first open-source vision-language model in Korea capable of visual understanding, it is expected to significantly contribute to strengthening Korea's sovereign AI capabilities.


## **Updates**
- **(2025.07.25)**: vLLM engine is available with [our repository](https://github.com/NAVER-Cloud-HyperCLOVA-X/vllm/tree/v0.9.2rc2_hyperclovax_vision_seed)
- **(2025.07.08)**: Major code update for supporting vLLM engine ([link - related_discussion](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B/discussions/27))
- **(2025.04.22)**: Initial release of the repository.


## **Basic Information**

- **Model Architecture**: LLaVA-based Vision-Language Model  
    - **LLM Module**: Transformer-based architecture (Dense Model)  
    - **Vision Encoder** : SigLIP-based architecture with 378x378px input resolution per grid.
    - **Vision-Language Connector** : C-Abstractor based architecture with AnyRes mechanism, supporting up to 1.29M total pixels across 9 grids.
- **Parameter Count**: 3.2B (LLM Module) + 0.43B (Vision Module)  
- **Input/Output Format**: Text + Image + Video / Text  
- **Context Length**: 16k  
- **Knowledge Cutoff Date**: The model was trained on data collected before August 2024.  


## **Training**

#### **Text**

Securing high-quality data is essential even during post-training, but having humans manually create or revise large-scale datasets posed significant limitations in terms of both cost and resources. Additionally, tasks requiring domain expertise were difficult to handle, and the risk of human error was high. To overcome these challenges, we utilized an automated validation system powered by HyperCLOVA X, which improved data quality and streamlined the training process — ultimately leading to enhanced overall model performance. As a result, the model showed significant improvements in areas with definitive answers, such as mathematics and coding.

While reducing the cost of data collection is important, finding efficient training strategies is equally critical. HyperCLOVAX-SEED-Vision-Instruct-3B was developed starting from the HyperCLOVAX-SEED-Text-Base-3B and applied both Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF) based on an online reinforcement algorithm called GRPO.

#### **Vision**

The Vision Understanding feature — where the model receives images and questions as input and generates text-based answers — was not part of the initial design of HyperCLOVA X. Therefore, the model architecture was carefully designed to add capabilities for handling vision-related tasks, such as image-based question answering (VQA) and chart/diagram interpretation, without compromising the existing performance of the HCX LLM. Special attention was given to handling auxiliary information within the input, especially considering the context length.

Although HyperCLOVAX-SEED-Vision-Instruct-3B is a lightweight model, it is capable of performing basic image VQA tasks and even supports OCR-free processing. One of the key focus areas for this 3B model was optimizing the efficiency of video input tokens. Since input token length directly affects computational cost, the number of tokens extracted per frame was carefully adjusted to enable efficient video understanding with as few tokens as possible. Additionally, during the RLHF training phase, vision-specific V-RLHF data was used to enhance the model’s learning, just like in the text domain.

## Benchmark
#### Text

| **Model** | **KMMLU (5-shot, acc)** | **HAE-RAE (5-shot, acc)** | **CLiCK (5-shot, acc)** | **KoBEST (5-shot, acc)** |
|----------------------------|--------|---------|---------|-------|
| HyperCLOVAX-SEED-Text-Base-3B  | 0.4847 | 0.7635  | 0.6386  | 0.7792 |
| HyperCLOVAX-SEED-Vision-Instruct-3B| 0.4422 | 0.6499  | 0.5599  | 0.7180 |
| Qwen2.5-3B-instruct        | 0.4451 | 0.6031  | 0.5649  | 0.7053 |
| gemma-3-4b-it              | 0.3895 | 0.6059  | 0.5303  | 0.7262 |

#### Vision

| Model Name                        | Max Token Count per Video      | VideoMME (Ko) | NAVER-TV-CLIP (Ko) | VideoChatGPT (Ko) | PerceptionTest (En) | ActivityNet-QA (En) | KoNet (Ko) | MMBench-Val (En) | TextVQA-Val (En) | Korean VisIT-Bench (Ko) | Image (4 benchmarks) | Video (5 benchmarks) | All (9 benchmarks) |
|-----------------------------------|--------------------------------|----------------|---------------------|--------------------|-----------------------|----------------------|------------|-------------------|-------------------|--------------------------|------------------------|------------------------|----------------------|
| HyperCLOVAX-SEED-Vision-Instruct-3B              | 1856 tokens, 108 frames        | 48.2           | 61.0                | 53.6               | 55.2                  | 50.6                 | 69.2       | 81.8              | 79.2              | 37.0                     | 46.68                  | 53.70                  | 59.54                |
| HyperCLOVAX-SEED-Vision-Instruct-3B (without OCR)| 1856 tokens, 108 frames        | 48.2           | 61.0                | 53.6               | 55.2                  | 50.6                 | 36.6       | 80.7              | 76.0              | 43.5                     | 56.74                  | 53.70                  | 55.05                |
| Qwen-2.5-VL-3B                    | 24576 tokens, 768 frames       | 55.1           | 48.3                | 45.6               | 66.9                  | 55.7                 | 58.3       | 84.3              | 79.6              | 81.5                     | 59.35                  | 54.31                  | 56.55                |
| Qwen-2.5-VL-3B (w/ 2000 tokens)   | 2000 tokens, 128 frames        | 50.3           | 43.9                | 44.3               | 58.3                  | 54.2                 | 58.5       | 84.3              | 79.3              | 15.7                     | 59.50                  | 50.18                  | 54.33                |
| Qwen-2.5-VL-7B                    | 24576 tokens, 768 frames       | 60.6           | 66.7                | 51.8               | 70.5                  | 56.6                 | 68.4       | 88.3              | 84.9              | 85.6                     | 69.34                  | 61.23                  | 64.84                |
| Gemma-3-4B                        | 4096 tokens, 16 frames         | 45.4           | 36.8                | 57.1               | 50.6                  | 46.3                 | 25.0       | 79.2              | 58.9              | 32.3                     | 48.91                  | 47.24                  | 47.98                |
| GPT4V (gpt-4-turbo-2024-04-09)    | Unknown, Original Image , 8 frames | 49.1           | 75.0                | 55.5               | 57.4                  | 45.7                 | 38.7       | 84.2              | 60.4              | 52.0                     | 58.88                  | 51.59                  | 54.83                |
| GPT4o (gpt-4o-2024-08-06)         | Unknown, 512 resize, 128 frames| 61.6           | 66.6                | 61.8               | 50.2                  | 41.7                 | 60.6       | 84.2              | 73.2              | 50.5                     | 67.15                  | 56.42                  | 61.19                |
| InternV-2-2B                      | 4096 tokens, 16 frames         | 28.9           | 21.1                | 40.2               | 50.5                  | 50.3                 | 3.3        | 79.3              | 75.1              | 51.1                     | 39.74                  | 38.19                  | 38.88                |
| InternV-2-4B                      | 4096 tokens, 16 frames         | 33.8           | 36.0                | 22.8               | 54.2                  | 52.0                 | 22.7       | 83.0              | 76.9              | 51.6                     | 46.11                  | 39.75                  | 42.58                |
| InternV-2-8B                      | 4096 tokens, 16 frames         | 43.7           | 41.2                | 32.4               | 58.5                  | 53.2                 | 28.5       | 86.6              | 79.0              | 97.0                     | 50.32                  | 45.79                  | 47.81                |

## Dependencies
- [einops](https://einops.rocks/)
- [timm](https://github.com/huggingface/pytorch-image-models)
- [av](https://github.com/PyAV-Org/PyAV)
- [decord](https://github.com/dmlc/decord)

## Example
**(code & benchmark score) checked with transformers 4.52.4**

```python

from transformers import AutoModelForCausalLM, AutoProcessor, AutoTokenizer

model_name = "naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B"
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True).to(device="cuda")
processor = AutoProcessor.from_pretrained(model_name, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# LLM Example
# It is recommended to use the chat template with HyperCLOVAX models.
# Using the chat template allows you to easily format your input in ChatML style.
llm_chat = [
        {"role": "system", "content": [{"type": "text", "text": "you are helpful assistant!"}]},
        {
                "role": "user", 
                "content": [
                        {"type": "text", "text": "Hello, how are you?"},
                        {"type": "text", "text": "I said. Hello, how are you today?"},
                ]
        },
        {"role": "assistant", "content": [{"type": "text", "text": "I'm doing great. How can I help you today?"}]},
        {"role": "user", "content": [{"type": "text", "text": "I'd like to show off how chat templating works!"}]},
]
model_inputs = processor.apply_chat_template(
        llm_chat, tokenize=True, return_dict=True, return_tensors="pt", add_generation_prompt=True
)
model_inputs = model_inputs.to(device="cuda")

# Please adjust parameters like top_p appropriately for your use case.
output_ids = model.generate(
        **model_inputs,
        max_new_tokens=64,
        do_sample=True,
        top_p=0.6,
        temperature=0.5,
        repetition_penalty=1.0,
)
print("=" * 80)
print("LLM EXAMPLE")
print(processor.batch_decode(output_ids)[0])
print("=" * 80)

# VLM Example
# For images and videos, you can use url, local_path, base64, or bytes as input sources.
vlm_chat = [
        {"role": "system", "content": [{"text": "System Prompt", "type": "text"}]},
        {"role": "user", "content": [{"text": "User Text Prompt 1", "type": "text"}]},
        {
                "role": "user",
                "content": [{
                        "filename": "tradeoff_sota.png",
                        "image": "https://github.com/naver-ai/rdnet/blob/main/resources/images/tradeoff_sota.png?raw=true",
                        "lens_keywords": "Gucci Ophidia, cross bag, Ophidia small, GG, Supreme shoulder bag",
                        "lens_local_keywords": "[0.07, 0.21, 0.92, 0.90] Gucci Ophidia",
                        "ocr": "List the words in the image in raster order. Even if the word order feels unnatural for reading, the model will handle it as long as it follows raster order.",                        "type": "image",
                }],
        },
        {
                "role": "user",
                "content": [{
                        "filename": "tradeoff.png",
                        "image": "https://github.com/naver-ai/rdnet/blob/main/resources/images/tradeoff.png?raw=true",
                        "type": "image",
                }],
        },
        {"role": "assistant", "content": [{"text": "Assistant Text Prompt 1", "type": "text"}]},
        {"role": "user", "content": [{"text": "User Text Prompt 2", "type": "text"}]},
        {
                "role": "user",
                "content": [
                        {
                                "type": "video",
                                "video": "freenaturestock-rolling-mist-clouds.mp4",
                                "lens_keywords": "Prada re-edition, nylon bag, mini cross bag, logo strap, essential shoulder bag",
                                "lens_local_keywords": "[0.12, 0.34, 0.85, 0.76] Prada re-edition",
                                "speech_to_text": "Please enter the dialogue, voice, sound, lines, and words in the video in text format.",
                        },
                        {"text": "User Text Prompt 3", "type": "text"},
                ]
        },
]

model_inputs = processor.apply_chat_template(   
        vlm_chat, tokenize=True, return_dict=True, return_tensors="pt", add_generation_prompt=True,
)
model_inputs = model_inputs.to(device="cuda")
output_ids = model.generate(
        **model_inputs,
        max_new_tokens=64,
        do_sample=True,
        top_p=0.6,
        temperature=0.5,
        repetition_penalty=1.0,
)
print("=" * 80)
print("VLM EXAMPLE")
print(processor.batch_decode(output_ids)[0])
print("=" * 80)

```

## Example for v0.1.0
**(code & benchmark score) checked with transformers 4.45.0**

```python

from transformers import AutoModelForCausalLM, AutoProcessor, AutoTokenizer

model_name = "naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B"
revision="v0.1.0"
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, revision=revision).to(device="cuda")
preprocessor = AutoProcessor.from_pretrained(model_name, trust_remote_code=True, revision=revision)
tokenizer = AutoTokenizer.from_pretrained(model_name, revision=revision)

# LLM Example
# It is recommended to use the chat template with HyperCLOVAX models.
# Using the chat template allows you to easily format your input in ChatML style.
chat = [
        {"role": "system", "content": "you are helpful assistant!"},
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "assistant", "content": "I'm doing great. How can I help you today?"},
        {"role": "user", "content": "I'd like to show off how chat templating works!"},
]
input_ids = tokenizer.apply_chat_template(chat, return_tensors="pt", tokenize=True)
input_ids = input_ids.to(device="cuda")

# Please adjust parameters like top_p appropriately for your use case.
output_ids = model.generate(
        input_ids,
        max_new_tokens=64,
        do_sample=True,
        top_p=0.6,
        temperature=0.5,
        repetition_penalty=1.0,
)
print("=" * 80)
print("LLM EXAMPLE")
print(tokenizer.batch_decode(output_ids)[0])
print("=" * 80)

# VLM Example
# For image and video inputs, you can use url, local_path, base64, or bytes.
vlm_chat = [
        {"role": "system", "content": {"type": "text", "text": "System Prompt"}},
        {"role": "user", "content": {"type": "text", "text": "User Text 1"}},
        {
                "role": "user",
                "content": {
                        "type": "image",
                        "filename": "tradeoff_sota.png",
                        "image": "https://github.com/naver-ai/rdnet/blob/main/resources/images/tradeoff_sota.png?raw=true",
                        "ocr": "List the words in the image in raster order. Even if the word order feels unnatural for reading, the model will handle it as long as it follows raster order.",
                        "lens_keywords": "Gucci Ophidia, cross bag, Ophidia small, GG, Supreme shoulder bag",
                        "lens_local_keywords": "[0.07, 0.21, 0.92, 0.90] Gucci Ophidia",
                }
        },
        {
                "role": "user",
                "content": {
                        "type": "image",
                        "filename": "tradeoff.png",
                        "image": "https://github.com/naver-ai/rdnet/blob/main/resources/images/tradeoff.png?raw=true",
                }
        },
        {"role": "assistant", "content": {"type": "text", "text": "Assistant Text 1"}},
        {"role": "user", "content": {"type": "text", "text": "User Text 2"}},
        {
                "role": "user",
                "content": {
                        "type": "video",
                        "filename": "rolling-mist-clouds.mp4",
                        "video": "freenaturestock-rolling-mist-clouds.mp4",
                }
        },
        {"role": "user", "content": {"type": "text", "text": "User Text 3"}},
]

new_vlm_chat, all_images, is_video_list = preprocessor.load_images_videos(vlm_chat)
preprocessed = preprocessor(all_images, is_video_list=is_video_list)
input_ids = tokenizer.apply_chat_template(
        new_vlm_chat, return_tensors="pt", tokenize=True, add_generation_prompt=True,
)

output_ids = model.generate(
        input_ids=input_ids.to(device="cuda"),
        max_new_tokens=8192,
        do_sample=True,
        top_p=0.6,
        temperature=0.5,
        repetition_penalty=1.0,
        **preprocessed,
)
print("=" * 80)
print("VLM EXAMPLE")
print(tokenizer.batch_decode(output_ids)[0])
print("=" * 80)
```

- To ensure the highest level of image understanding performance, it is recommended to include additional information such as Optical Character Recognition (OCR) results and entity recognition (Lens). The provided usage examples are written under the assumption that OCR and Lens results are available. If you input data in this format, you can expect significantly improved output quality.

## vLLM
To speed up your inference, you can use the vLLM engine from [our repository](https://github.com/NAVER-Cloud-HyperCLOVA-X/vllm/tree/v0.9.2rc2_hyperclovax_vision_seed).  

Make sure to switch to the `v0.9.2rc2_hyperclovax_vision_seed` branch.  

**Launch API server**:

```bash
pyenv virtualenv 3.10.2 .vllm
pyenv activate .vllm
sudo apt-get install -y kmod
pip install --upgrade setuptools wheel pip
pip install setuptools_scm

# install latest commit (e.g. v0.9.0)
VLLM_USE_PRECOMPILED=1 pip install -e .[serve] --cache-dir=/mnt/tmp
pip install -U pynvml
pip install timm av decord

# or install previous commit (e.g. v0.8.4)
pip install -r ./requirements/build.txt
pip install -r ./requirements/common.txt
pip install -r ./requirements/cuda.txt
pip install flash_attn==2.7.4.post1
pip install flashinfer -i https://flashinfer.ai/whl/cu121/torch2.4/
export VLLM_COMMIT=dc1b4a6f1300003ae27f033afbdff5e2683721ce
export VLLM_PRECOMPILED_WHEEL_LOCATION=https://wheels.vllm.ai/${VLLM_COMMIT}/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl
VLLM_USE_PRECOMPILED=1 pip install -e .[serve] --cache-dir=/mnt/tmp
pip install -U pynvml
pip install timm av decord

# Then launch api
MODEL=your/mode/path
export ATTENTION_BACKEND=FLASH_ATTN_VLLM_V1
VLLM_USE_V1=1 VLLM_ATTENTION_BACKEND=${ATTENTION_BACKEND} CUDA_VISIBLE_DEVICES=0,1 python -m vllm.entrypoints.openai.api_server \
    --seed 20250525 \
    --port ${PORT} \
    --allowed-local-media-path $ALLOWED_LOCAL_MEDIA_PATH \
    --max-model-len 8192 \
    --max-num-batched-tokens 8192 \
    --max-num-seqs 128 \
    --max-parallel-loading-workers 128 \
    --limit-mm-per-prompt.image="32" \
    --limit-mm-per-prompt.viedo="32" \
    --max-num-frames 256 \
    --tensor-parallel-size 1 \
    --data-parallel-size 1 \
    --model ${MODEL} \
    --dtype float16 \
    --trust-remote-code \
    --chat-template-content-format "openai" \
    --download-dir $DONWLOAD_DIR
```

**Request Example**:
- https://github.com/vllm-project/vllm/pull/20931#issue-3229161410

**Offline Inference Examples**:
- https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/vision_language.py
- https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/vision_language_multi_image.py
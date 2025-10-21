---
license: apache-2.0
language:
- zh
- en
pipeline_tag: text-generation
library_name: transformers
---
<div align="center">
<img src="https://github.com/OpenBMB/MiniCPM/blob/main/assets/minicpm_logo.png?raw=true" width="500em" ></img> 
</div>

<p align="center">
<a href="https://github.com/OpenBMB/MiniCPM/" target="_blank">GitHub Repo</a> |
<a href="https://arxiv.org/abs/2506.07900" target="_blank">Technical Report</a> |
<a href="https://mp.weixin.qq.com/s/KIhH2nCURBXuFXAtYRpuXg?poc_token=HBIsUWijxino8oJ5s6HcjcfXFRi0Xj2LJlxPYD9c">Join Us</a>
</p>
<p align="center">
👋 Contact us in <a href="https://discord.gg/3cGQn9b3YM" target="_blank">Discord</a> and <a href="https://github.com/OpenBMB/MiniCPM/blob/main/assets/wechat.jpg" target="_blank">WeChat</a>
</p>

## What's New
- [2025.09.29] **[InfLLM-V2 paper](https://arxiv.org/abs/2509.24663) is released!** We can train a sparse attention model with only 5B long-text tokens. 🔥🔥🔥
- [2025.09.05] **MiniCPM4.1** series are released! This series is a hybrid reasoning model with trainable sparse attention, which can be used in both deep reasoning mode and non-reasoning mode. 🔥🔥🔥
- [2025.06.06] **MiniCPM4** series are released! This model achieves ultimate efficiency improvements while maintaining optimal performance at the same scale! It can achieve over 5x generation acceleration on typical end-side chips! You can find technical report [here](https://arxiv.org/abs/2506.07900).🔥🔥🔥

## Highlights
MiniCPM4.1 is highlighted with following features:

✅ Strong Reasoning Capability: Surpasses similar-sized models on 15 tasks!

✅ Fast Generation: 3x decoding speedup for reasoning!

✅ Efficient Architecture: Trainable sparse attention, frequency-ranked speculative decoding!

- [MiniCPM4.1-8B](https://huggingface.co/openbmb/MiniCPM4.1-8B): The latest version of MiniCPM4, with 8B parameters, support fusion thinking. (**<-- you are here**)
- [MiniCPM4.1-8B-GPTQ](https://huggingface.co/openbmb/MiniCPM4.1-8B-GPTQ): MiniCPM4.1-8B in GPTQ format.
- [MiniCPM4.1-8B-AutoAWQ](https://huggingface.co/openbmb/MiniCPM4.1-8B-AutoAWQ): MiniCPM4.1-8B in AutoAWQ format.
- [MiniCPM-4.1-8B-Marlin](https://huggingface.co/openbmb/MiniCPM-4.1-8B-Marlin): MiniCPM4.1-8B in Marlin format.
- [MiniCPM4.1-8B-GGUF](https://huggingface.co/openbmb/MiniCPM4.1-8B-GGUF): MiniCPM4.1-8B in GGUF format.
- [MiniCPM4.1-8B-MLX](https://huggingface.co/openbmb/MiniCPM4.1-8B-MLX): MiniCPM4.1-8B in MLX format.
- [MiniCPM4.1-8B-Eagle3](https://huggingface.co/openbmb/MiniCPM4.1-8B-Eagle3): Eagle3 model for MiniCPM4.1-8B.
- **MiniCPM4 Series**
    <details>
    <summary>Click to expand all MiniCPM4 series models</summary>

    - [**MiniCPM4-8B**](https://huggingface.co/openbmb/MiniCPM4-8B): The flagship model with 8B parameters, trained on 8T tokens
    - [**MiniCPM4-0.5B**](https://huggingface.co/openbmb/MiniCPM4-0.5B): Lightweight version with 0.5B parameters, trained on 1T tokens
    - [**MiniCPM4-8B-Eagle-FRSpec**](https://huggingface.co/openbmb/MiniCPM4-8B-Eagle-FRSpec): Eagle head for FRSpec, accelerating speculative inference
    - [**MiniCPM4-8B-Eagle-FRSpec-QAT-cpmcu**](https://huggingface.co/openbmb/MiniCPM4-8B-Eagle-FRSpec-QAT-cpmcu): Eagle head with QAT for FRSpec, integrating speculation and quantization for ultra acceleration
    - [**MiniCPM4-8B-Eagle-vLLM**](https://huggingface.co/openbmb/MiniCPM4-8B-Eagle-vLLM): Eagle head in vLLM format for speculative inference
    - [**MiniCPM4-8B-marlin-Eagle-vLLM**](https://huggingface.co/openbmb/MiniCPM4-8B-marlin-Eagle-vLLM): Quantized Eagle head for vLLM format
    - [**BitCPM4-0.5B**](https://huggingface.co/openbmb/BitCPM4-0.5B): Extreme ternary quantization of MiniCPM4-0.5B, achieving 90% bit width reduction
    - [**BitCPM4-1B**](https://huggingface.co/openbmb/BitCPM4-1B): Extreme ternary quantization of MiniCPM3-1B, achieving 90% bit width reduction
    - [**MiniCPM4-Survey**](https://huggingface.co/openbmb/MiniCPM4-Survey): Generates trustworthy, long-form survey papers from user queries
    - [**MiniCPM4-MCP**](https://huggingface.co/openbmb/MiniCPM4-MCP): Integrates MCP tools to autonomously satisfy user requirements
    </details>


## Evaluation Results

### Performance Evaluation
MiniCPM4.1 launches end-side versions with 8B parameter scale, both achieving best-in-class performance in their respective categories.

![benchmark](https://github.com/OpenBMB/MiniCPM/blob/main/assets/minicpm4/benchmark4.1.png?raw=true)

### Best Practices
1. It is advisable  to use temperature=0.9, topp=0.95. And we suggest setting max_output_token to 65,536 tokens.
2. For math problems, we recommend using "Please reason step by step, and put your final answer within \boxed{}."
3. And for English multiple-choice questions, we recommend starting with "Answer the following multiple choice question. The last line of your response should be of the following format: 'ANSWER: $LETTER' (without quotes) where LETTER is one of ABCD. Think step by step before answering." And "你回答的最后一行必须是以下格式 '答案：$选项' (不带引号), 其中选项是ABCD之一。请在回答之前一步步思考" for Chinese MCQ.

### Efficiency Evaluation
MiniCPM4.1 adopts sparse attention and speculative decoding to improve the inference efficiency. On RTX 4090, MiniCPM4.1 achieves 3x decoding speed improvement in reasoning.

![benchmark](https://github.com/OpenBMB/MiniCPM/blob/main/assets/minicpm4/minicpm4.1_speed.png?raw=true)

#### Examples
<div align="center">
  <a href="https://www.youtube.com/watch?v=VouXjLHKDUY"><img src="https://img.youtube.com/vi/VouXjLHKDUY/0.jpg", width=70%></a>
</div>



## Usage
MiniCPM 4.1 can be used with following frameworks: Huggingface Transformers, SGLang, vLLM, and CPM.cu. For the ultimate inference speed, we highly recommend CPM.cu.

MiniCPM4/MiniCPM4.1 supports both dense attention inference and sparse attention inference modes, where vLLM and SGLang currently only support dense inference mode. If you want to use sparse inference mode, please use Huggingface Transformers and CPM.cu.

- Dense attention inference: vLLM, SGLang, Huggingface Transformers
- Sparse attention inference: Huggingface Transformers, CPM.cu

**To facilitate researches in sparse attention, we provide [InfLLM-V2 Training Kernels](https://github.com/OpenBMB/infllmv2_cuda_impl) and [InfLLM-V2 Inference Kernels](https://github.com/openbmb/cpm.cu).**

### Inference with Transformers
MiniCPM4.1-8B requires `transformers>=4.56`.

- **Inference with Dense Attention**
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
torch.manual_seed(0)

path = 'openbmb/MiniCPM4.1-8B'
device = "cuda"
tokenizer = AutoTokenizer.from_pretrained(path)
model = AutoModelForCausalLM.from_pretrained(path, torch_dtype=torch.bfloat16, device_map=device, trust_remote_code=True)

# User can directly use the chat interface
# responds, history = model.chat(tokenizer, "Write an article about Artificial Intelligence.", temperature=0.7, top_p=0.7)
# print(responds)

# User can also use the generate interface
messages = [
    {"role": "user", "content": "Write an article about Artificial Intelligence."},
]
prompt_text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([prompt_text], return_tensors="pt").to(device)

model_outputs = model.generate(
    **model_inputs,
    max_new_tokens=32768,
    top_p=0.95,
    temperature=0.6
)
output_token_ids = [
    model_outputs[i][len(model_inputs[i]):] for i in range(len(model_inputs['input_ids']))
]

responses = tokenizer.batch_decode(output_token_ids, skip_special_tokens=True)[0]
print(responses)
```

- **Inference with Sparse Attention**
MiniCPM4.1-8B supports `InfLLM v2`, a sparse attention mechanism designed for efficient long-sequence inference. It requires the [infllmv2_cuda_impl](https://github.com/OpenBMB/infllmv2_cuda_impl) library.

You can install it by running the following command:
```bash
git clone -b feature_infer https://github.com/OpenBMB/infllmv2_cuda_impl.git
cd infllmv2_cuda_impl
git submodule update --init --recursive
pip install -e . # or python setup.py install 
```

To enable InfLLM v2, you need to add the `sparse_config` field in `config.json`:
```json
{
    ...,
    "sparse_config": {
        "kernel_size": 32,
        "kernel_stride": 16,
        "init_blocks": 1,
        "block_size": 64,
        "window_size": 2048,
        "topk": 64,
        "use_nope": false,
        "dense_len": 8192
    }
}
```

These parameters control the behavior of InfLLM v2:
* `kernel_size` (default: 32): The size of semantic kernels.
* `kernel_stride` (default: 16): The stride between adjacent kernels.
* `init_blocks` (default: 1): The number of initial blocks that every query token attends to. This ensures attention to the beginning of the sequence.
* `block_size` (default: 64): The block size for key-value blocks.
* `window_size` (default: 2048): The size of the local sliding window. 
* `topk` (default: 64): The specifies that each token computes attention with only the top-k most relevant key-value blocks.
* `use_nope` (default: false): Whether to use the NOPE technique in block selection for improved performance.
* `dense_len` (default: 8192): Since Sparse Attention offers limited benefits for short sequences, the model can use standard (dense) attention for shorter texts. The model will use dense attention for sequences with a token length below `dense_len` and switch to sparse attention for sequences exceeding this length. Set this to `-1` to always use sparse attention regardless of sequence length.

- **Long Context Extension**
MiniCPM4.1 natively supports context lengths of up to 65,536(64k) tokens. For conversations where the total length (including both input and output) significantly exceeds this limit, we recommend using RoPE scaling techniques for effective handling of long texts. We have validated the model's performance on context lengths of up to 131,072 tokens by modifying the LongRoPE factor.

You can apply the LongRoPE factor modification by modifying the model files. Specifically, in the `config.json` file, adjust the `rope_scaling` fields.
```json
{
    ...,
    "rope_scaling": {
        "rope_type": "longrope", 
        "long_factor": [0.9982316082870437, 1.033048153422584, 1.0749920956484724, 1.1255096879436193, 1.1863348602111476, 1.259543828902579, 1.3476188888731149, 1.4535223827776373, 1.5807816745852985, 1.7335856049489526, 1.9168922912975785, 2.1365471404135326, 2.3994084200118646, 2.713475511863602, 3.0880118452194134, 3.533650295140154, 4.062463396503134, 4.687974098908333, 5.425075306704039, 6.289818967956352, 7.29902962722721, 8.6357018163639, 10.210822723989212, 12.053807765671676, 14.193944598909404, 16.65780676784363, 19.463620727694074, 22.628311203524586, 26.150106147261315, 30.02526691405111, 34.23183327975347, 38.73811934094828, 43.502489489729555, 48.47627117965394, 53.61139491762471, 58.857366522037935, 64.16798299215064, 69.51359464319125, 74.86555458220285, 80.21497790341579, 85.55322183307433, 90.89611806932027, 96.26245306514224, 101.68269304046481, 107.18619510219668, 112.82253283014026, 118.63764063163615, 119.88866203644656, 120.9462882391725, 121.837565139014, 122.58663780572562, 123.2147719894291, 123.74049454862576, 124.17980424685767, 124.54641761955492, 124.85202548028222, 125.10654406389756, 125.31835105170659, 125.49450117164764, 125.64091910903052, 125.76256945356558, 125.86360463815589, 125.94749252260765, 126.01712561287873],
        "short_factor": [0.9982316082870437, 1.033048153422584, 1.0749920956484724, 1.1255096879436193, 1.1863348602111476, 1.259543828902579, 1.3476188888731149, 1.4535223827776373, 1.5807816745852985, 1.7335856049489526, 1.9168922912975785, 2.1365471404135326, 2.3994084200118646, 2.713475511863602, 3.0880118452194134, 3.533650295140154, 4.062463396503134, 4.687974098908333, 5.425075306704039, 6.289818967956352, 7.29902962722721, 8.6357018163639, 10.210822723989212, 12.053807765671676, 14.193944598909404, 16.65780676784363, 19.463620727694074, 22.628311203524586, 26.150106147261315, 30.02526691405111, 34.23183327975347, 38.73811934094828, 43.502489489729555, 48.47627117965394, 53.61139491762471, 58.857366522037935, 64.16798299215064, 69.51359464319125, 74.86555458220285, 80.21497790341579, 85.55322183307433, 90.89611806932027, 96.26245306514224, 101.68269304046481, 107.18619510219668, 112.82253283014026, 118.63764063163615, 119.88866203644656, 120.9462882391725, 121.837565139014, 122.58663780572562, 123.2147719894291, 123.74049454862576, 124.17980424685767, 124.54641761955492, 124.85202548028222, 125.10654406389756, 125.31835105170659, 125.49450117164764, 125.64091910903052, 125.76256945356558, 125.86360463815589, 125.94749252260765, 126.01712561287873],
        "original_max_position_embeddings": 65536
    }
}
```

### Inference with [SGLang](https://github.com/sgl-project/sglang)

You can inference with SGLang using the standard mode and speculative decoding mode.

#### Speculative Decoding

For accelerated inference with speculative decoding, follow these steps:

##### 1. Download MiniCPM4.1 Draft Model

First, download the MiniCPM4.1 draft model:

```bash
cd /your_path
git clone https://huggingface.co/openbmb/MiniCPM4.1-8B-Eagle3
```

##### 2. Install EAGLE3-Compatible SGLang

The EAGLE3 adaptation PR has been submitted. For now, use our repository for installation:

```bash
git clone https://github.com/LDLINGLINGLING/sglang.git
cd sglang
pip install -e "python[all]"
```

##### 3. Launch SGLang Server with Speculative Decoding

Start the SGLang server with speculative decoding enabled:

```bash
python -m sglang.launch_server \
  --model-path "openbmb/MiniCPM4.1-8B" \
  --host "127.0.0.1" \
  --port 30002 \
  --mem-fraction-static 0.9 \
  --speculative-algorithm EAGLE3 \
  --speculative-draft-model-path "your/path/MiniCPM4_1-8B-Eagle3-bf16" \
  --speculative-num-steps 3 \
  --speculative-eagle-topk 1 \
  --speculative-num-draft-tokens 32 \
  --temperature 0.7
```

##### 4. Client Usage

The client usage remains the same for both standard and speculative decoding:

```python
import openai

client = openai.Client(base_url=f"http://localhost:30002/v1", api_key="None")

response = client.chat.completions.create(
    model="openbmb/MiniCPM4.1-8B",
    messages=[
        {"role": "user", "content": "Write an article about Artificial Intelligence."},
    ],
    temperature=0.6,
    max_tokens=32768,
)

print(response.choices[0].message.content)
```

Note: Make sure to update the port number in the client code to match the server port (30002 in the speculative decoding example).

##### Configuration Parameters

- `--speculative-algorithm EAGLE3`: Enables EAGLE3 speculative decoding
- `--speculative-draft-model-path`: Path to the draft model for speculation
- `--speculative-num-steps`: Number of speculative steps (default: 3)
- `--speculative-eagle-topk`: Top-k parameter for EAGLE (default: 1)
- `--speculative-num-draft-tokens`: Number of draft tokens (default: 32)
- `--mem-fraction-static`: Memory fraction for static allocation (default: 0.9)

#### Standard Inference (Without Speculative Decoding)

For now, you need to install our forked version of SGLang.

```bash
git clone -b openbmb https://github.com/OpenBMB/sglang.git
cd sglang

pip install --upgrade pip
pip install -e "python[all]"
```

You can start the inference server by running the following command:

```bash
python -m sglang.launch_server --model openbmb/MiniCPM4.1-8B --trust-remote-code --port 30000 --chat-template chatml
```

Then you can use the chat interface by running the following command:

```python
import openai

client = openai.Client(base_url=f"http://localhost:30000/v1", api_key="None")

response = client.chat.completions.create(
    model="openbmb/MiniCPM4.1-8B",
    messages=[
        {"role": "user", "content": "Write an article about Artificial Intelligence."},
    ],
    temperature=0.6,
    max_tokens=32768,
)

print(response.choices[0].message.content)
```

### Inference with [vLLM](https://github.com/vllm-project/vllm)
You can inference with vLLM using the standard mode and speculative decoding mode.

#### Speculative Decoding

For accelerated inference with speculative decoding using vLLM, follow these steps:

##### 1. Download MiniCPM4.1 Draft Model

First, download the MiniCPM4.1 draft model and change the `architectures` in config.json as `LlamaForCausalLM`.

```bash
cd /your_path
git clone https://huggingface.co/openbmb/MiniCPM4.1-8B-Eagle3
```

##### 2. Install EAGLE3-Compatible vLLM

The EAGLE3 vLLM PR has been submitted. For now, use our repository for installation:

```bash
git clone https://github.com/LDLINGLINGLING/vllm.git
cd vllm 
pip install -e .
```

##### 3. Launch vLLM Server with Speculative Decoding

Start the vLLM inference server with speculative decoding enabled. Make sure to update the model path in the speculative-config to point to your downloaded MiniCPM4_1-8B-Eagle3-bf16 folder:

```bash
VLLM_USE_V1=1 \
vllm serve openbmb/MiniCPM4.1-8B \
--seed 42 \
--trust-remote-code \
--speculative-config '{
  "model": "your/path/MiniCPM4_1-8B-Eagle3-bf16",
  "num_speculative_tokens": 3,
  "method": "eagle3",
  "draft_tensor_parallel_size": 1
}'
```

##### 4. Client Usage Example

The client usage remains the same for both standard and speculative decoding:

```python
import openai

client = openai.Client(base_url="http://localhost:8000/v1", api_key="EMPTY")

response = client.chat.completions.create(
    model="openbmb/MiniCPM4.1-8B",
    messages=[
        {"role": "user", "content": "Write an article about Artificial Intelligence."},
    ],
    temperature=0.6,
    max_tokens=32768,
    extra_body=dict(add_special_tokens=True),  # Ensures special tokens are added for chat template
)

print(response.choices[0].message.content)
```

##### vLLM Configuration Parameters

- `VLLM_USE_V1=1`: Enables vLLM v1 API
- `--speculative-config`: JSON configuration for speculative decoding
  - `model`: Path to the draft model for speculation
  - `num_speculative_tokens`: Number of speculative tokens (default: 3)
  - `method`: Speculative decoding method (eagle3)
  - `draft_tensor_parallel_size`: Tensor parallel size for draft model (default: 1)
- `--seed`: Random seed for reproducibility
- `--trust-remote-code`: Allow execution of remote code for custom models

#### Standard Inference (Without Speculative Decoding)

For now, you need to install the latest version of vLLM.

```bash
pip install -U vllm \
    --pre \
    --extra-index-url https://wheels.vllm.ai/nightly
```

Then you can inference MiniCPM4.1-8B with vLLM:
```python
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams

model_name = "openbmb/MiniCPM4.1-8B"
prompt = [{"role": "user", "content": "Write an article about Artificial Intelligence."}]

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
input_text = tokenizer.apply_chat_template(prompt, tokenize=False, add_generation_prompt=True)

llm = LLM(
    model=model_name,
    trust_remote_code=True,
    max_num_batched_tokens=65536,
    dtype="bfloat16", 
    gpu_memory_utilization=0.8, 
)
sampling_params = SamplingParams(top_p=0.95, temperature=0.6, max_tokens=32768)

outputs = llm.generate(prompts=input_text, sampling_params=sampling_params)

print(outputs[0].outputs[0].text)
```

Also, you can start the inference server by running the following command:
> **Note**: In vLLM's chat API, `add_special_tokens` is `False` by default. This means important special tokens—such as the beginning-of-sequence (BOS) token—will not be added automatically. To ensure the input prompt is correctly formatted for the model, you should explicitly set `extra_body={"add_special_tokens": True}`.

```bash
vllm serve openbmb/MiniCPM4.1-8B --trust-remote-code 
```

Then you can use the chat interface by running the following code:

```python
import openai

client = openai.Client(base_url="http://localhost:8000/v1", api_key="EMPTY")

response = client.chat.completions.create(
    model="openbmb/MiniCPM4.1-8B",
    messages=[
        {"role": "user", "content": "Write an article about Artificial Intelligence."},
    ],
    temperature=0.6,
    max_tokens=32768,
    extra_body=dict(add_special_tokens=True),  # Ensures special tokens are added for chat template
    
)

print(response.choices[0].message.content)
```


### Inference with [CPM.cu](https://github.com/OpenBMB/cpm.cu)

We recommend using [CPM.cu](https://github.com/OpenBMB/cpm.cu) for the inference of MiniCPM4 and MiniCPM4.1. CPM.cu is a CUDA inference framework developed by OpenBMB, which integrates efficient sparse, speculative sampling, and quantization techniques, fully leveraging the efficiency advantages of MiniCPM4 and MiniCPM4.1.

You can install CPM.cu by running the following command:

```bash
git clone https://github.com/OpenBMB/cpm.cu.git --recursive
cd cpm.cu
python3 setup.py install
```

MiniCPM4.1 natively supports context lengths of up to 65,536(64k) tokens. To reproduce the long-text acceleration effect in the paper, we recommend using the LongRoPE factors that have been validated. Change the `rope_scaling` field in the `config.json` file as the following to enable LongRoPE.
```json
{
    ...,
    "rope_scaling": {
        "rope_type": "longrope", 
        "long_factor": [0.9982316082870437, 1.033048153422584, 1.0749920956484724, 1.1255096879436193, 1.1863348602111476, 1.259543828902579, 1.3476188888731149, 1.4535223827776373, 1.5807816745852985, 1.7335856049489526, 1.9168922912975785, 2.1365471404135326, 2.3994084200118646, 2.713475511863602, 3.0880118452194134, 3.533650295140154, 4.062463396503134, 4.687974098908333, 5.425075306704039, 6.289818967956352, 7.29902962722721, 8.6357018163639, 10.210822723989212, 12.053807765671676, 14.193944598909404, 16.65780676784363, 19.463620727694074, 22.628311203524586, 26.150106147261315, 30.02526691405111, 34.23183327975347, 38.73811934094828, 43.502489489729555, 48.47627117965394, 53.61139491762471, 58.857366522037935, 64.16798299215064, 69.51359464319125, 74.86555458220285, 80.21497790341579, 85.55322183307433, 90.89611806932027, 96.26245306514224, 101.68269304046481, 107.18619510219668, 112.82253283014026, 118.63764063163615, 119.88866203644656, 120.9462882391725, 121.837565139014, 122.58663780572562, 123.2147719894291, 123.74049454862576, 124.17980424685767, 124.54641761955492, 124.85202548028222, 125.10654406389756, 125.31835105170659, 125.49450117164764, 125.64091910903052, 125.76256945356558, 125.86360463815589, 125.94749252260765, 126.01712561287873],
        "short_factor": [0.9982316082870437, 1.033048153422584, 1.0749920956484724, 1.1255096879436193, 1.1863348602111476, 1.259543828902579, 1.3476188888731149, 1.4535223827776373, 1.5807816745852985, 1.7335856049489526, 1.9168922912975785, 2.1365471404135326, 2.3994084200118646, 2.713475511863602, 3.0880118452194134, 3.533650295140154, 4.062463396503134, 4.687974098908333, 5.425075306704039, 6.289818967956352, 7.29902962722721, 8.6357018163639, 10.210822723989212, 12.053807765671676, 14.193944598909404, 16.65780676784363, 19.463620727694074, 22.628311203524586, 26.150106147261315, 30.02526691405111, 34.23183327975347, 38.73811934094828, 43.502489489729555, 48.47627117965394, 53.61139491762471, 58.857366522037935, 64.16798299215064, 69.51359464319125, 74.86555458220285, 80.21497790341579, 85.55322183307433, 90.89611806932027, 96.26245306514224, 101.68269304046481, 107.18619510219668, 112.82253283014026, 118.63764063163615, 119.88866203644656, 120.9462882391725, 121.837565139014, 122.58663780572562, 123.2147719894291, 123.74049454862576, 124.17980424685767, 124.54641761955492, 124.85202548028222, 125.10654406389756, 125.31835105170659, 125.49450117164764, 125.64091910903052, 125.76256945356558, 125.86360463815589, 125.94749252260765, 126.01712561287873],
        "original_max_position_embeddings": 65536
    }
}
```

After modification, you can run the following command to reproduce the long-context acceleration effect (the script will automatically download the model weights from HuggingFace)
```bash
python3 tests/test_generate.py
```

You can run the following command to infer with EAGLE3 speculative decoding algorithm.

```bash
python3 -m cpmcu.cli \
    --model-path $BASE_MODEL_PATH \
    --draft-model-path $EAGLE3_DRAFT_MODEL_PATH \
    --prompt-text "Write an article about Artificial Intelligence." \
    --use-eagle3 true
```

For more details about CPM.cu, please refer to [the repo CPM.cu](https://github.com/OpenBMB/cpm.cu).

### Inference with llama.cpp and Ollama

We also support inference with [llama.cpp](https://github.com/ggml-org/llama.cpp) and [Ollama](https://ollama.com/).

##### llama.cpp

You can download the GGUF format of MiniCPM4.1-8B model from [huggingface](https://huggingface.co/openbmb/MiniCPM4.1-8B-GGUF) and run it with llama.cpp for efficient CPU or GPU inference.
```
# case 1: main-cli
./build/bin/llama-cli -m MiniCPM4.1-8B-Q4_K_M.gguf -p "Write an article about Artificial Intelligence." -n 1500

# case 2: server
## launch server
./build/bin/llama-server -m MiniCPM4.1-8B-Q4_K_M.gguf --host 127.0.0.1 --port 8080 -c 4096 -fa on &

## send request
curl -X POST http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Write an article about Artificial Intelligence."}],
    "max_tokens": 1500
  }'
```

##### Ollama
Please refer to [model hub](https://ollama.com/openbmb/minicpm4.1) for model download. After installing ollama package, you can use MiniCPM4.1 with following commands:
```
ollama run openbmb/minicpm4.1
```

### Hybird Reasoning Mode

MiniCPM4.1 supports hybrid reasoning mode, which can be used in both deep reasoning mode and non-reasoning mode. To enable hybrid reasoning mode. User can set `enable_thinking=True` in `tokenizer.apply_chat_template` to enable hybrid reasoning mode, and set `enable_thinking=False` to enable non-reasoning mode. Similarly, user can directly add `/no_think` at the end of the query to enable non-reasoning mode. If not add any special token or add `/think` at the end of the query, the model will enable reasoning mode.

```python
# Enable reasoning mode
prompt_text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True
)
# Enable non-reasoning mode
prompt_text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False
)
```

## Statement
- As a language model, MiniCPM generates content by learning from a vast amount of text. 
- However, it does not possess the ability to comprehend or express personal opinions or value judgments. 
- Any content generated by MiniCPM does not represent the viewpoints or positions of the model developers. 
- Therefore, when using content generated by MiniCPM, users should take full responsibility for evaluating and verifying it on their own.

## LICENSE
- This repository and MiniCPM models are released under the [Apache-2.0](https://github.com/OpenBMB/MiniCPM/blob/main/LICENSE) License. 

## Citation
- Please cite our [paper](https://arxiv.org/abs/2506.07900) if you find our work valuable.

```bibtex
@article{minicpm4,
  title={Minicpm4: Ultra-efficient llms on end devices},
  author={MiniCPM, Team},
  journal={arXiv preprint arXiv:2506.07900},
  year={2025}
}
```
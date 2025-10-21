---
pipeline_tag: text-generation
base_model:
- openai/gpt-oss-120b
license: other
license_name: nvidia-open-model-license
license_link: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license
library_name: Model Optimizer
tags:
- nvidia
- ModelOpt
- gpt-oss-120b
- quantized
- Eagle3
---
# Model Overview

## Description:
The NVIDIA gpt-oss-120b Eagle model is the Eagle head of the OpenAI’s gpt-oss-120b model, which is an auto-regressive language model that uses a mixture-of-experts (MoE) architecture with 5 billion activated parameters and 120 billion total parameters. For more information, please check [here](https://huggingface.co/openai/gpt-oss-120b). The NVIDIA gpt-oss-120b Eagle3 model incorporates Eagle speculative decoding with [TensorRT Model Optimizer](https://github.com/NVIDIA/TensorRT-Model-Optimizer).

This model is ready for commercial/non-commercial use.  <br>

### Note
`nvidia/gpt-oss-120b-Eagle3-v2` is typically better for use cases of less than 8k context length.

### License/Terms of Use:
[nvidia-open-model-license](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/)

### Deployment Geography:
Global <br>

### Use Case: <br>
Developers designing AI Agent systems, chatbots, RAG systems, and other AI-powered applications. Also suitable for typical instruction-following tasks.
<br>

### Release Date:  <br>
Huggingface:  Oct 6th, 2025 via [https://huggingface.co/nvidia/gpt-oss-120b-Eagle3-v2] <br> 

## Model Architecture:
**Architecture Type:** Transformers  <br>
**Network Architecture:** gpt-oss-120b <br>

##Computational Load
**Cumulative Compute: 4.8x10^20
**Estimated Energy and Emissions for Model Training: 
*Total kWh = 2500
*Total Emissions (tCO2e) = 0.8075

## Input:
**Input Type(s):** Text <br>
**Input Format(s):** String <br>
**Input Parameters:** One Dimensional (1D): Sequences <br>

## Output:
**Output Type(s):** Text <br>
**Output Format:** String <br>
**Output Parameters:** One-Dimensional (1D): Sequences <br>

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions. <br>  

## Software Integration:
**Supported Runtime Engine(s):** <br>
* TensorRT-LLM <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Blackwell <br>

**Preferred Operating System(s):** <br>
* Linux <br>

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.


## Training and Evaluation Datasets:

** The total size (in number of data points) 503.3K <br>
** Total number of datasets 2<br>   
** Dataset partition: Training  100%<br>


## Training Dataset:

**Link:** [ultrachat_200k](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k) and [Magpie-Llama-3.1-Pro-300K-Filtered](https://huggingface.co/datasets/Magpie-Align/Magpie-Llama-3.1-Pro-300K-Filtered), only prompts from the datasets were used for data synthesis, (the original responses from GPT were not used) for data synthesis, which is then used to train the Eagle modules. Click the links above for more information regarding the dataset.  <br>

** Data Modality
[Text]

** Data Collection Method by dataset <br>
* Hybrid: Synthetic, Human, Automated<br>

** Labeling Method by dataset <br>
* Hybrid: Synthetic, Human, Automated<br>
**Properties:** 500K samples, majority synthetic, others sourced from commercially-friendly datasets. <br>

## Evaluation Dataset: <br>
**Link:** MTBench, for more details, see [here](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge)  <br>

** Data Collection Method by dataset <br>
* Hybrid: Human, Synthetic<br>

** Labeling Method by dataset <br>
* Hybrid: Human, Synthetic<br>

**Properties:**  3,300 multi-turn dialogue sequences, each annotated with expert preference votes.<br>

## Inference:
**Engine:** TensorRT-LLM 1.2.0rc0 <br>
**Test Hardware:** B200 <br>


## Eagle Speculative Decoding
Synthesized data was obtained from OpenAI's gpt-oss-120b model, which is then used to finetune the Eagle modules. This model is ready for inference with TensorRT-LLM in Eagle speculative decoding mode. Eagle modules are used to predict candidate tokens beyond the next token. In the generation step, each forward Eagle module generates a distribution of tokens beyond the previous. Then, a tree-based attention mechanism samples some candidate sequences for the original model to validate. The longest accepted candidate sequence is selected so that more than 1 token is returned in the generation step. The number of tokens generated in each step is called acceptance rate.

## Usage

To serve the checkpoint with [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM), follow the sample commands below with the TensorRT-LLM GitHub repo:

```sh
trtllm-serve <gpt-oss-120b checkpoint> --host 0.0.0.0 --port 8000 --backend pytorch --max_batch_size 32 --tp_size 8 --extra_llm_api_options extra-llm-api-config.yml
```

`extra-llm-api-config.yml` is like this
```sh
enable_attention_dp: false
enable_autotuner: false

cuda_graph_config:
    max_batch_size: 32
    enable_padding: true

speculative_config:
    decoding_type: Eagle
    max_draft_len: 3
    speculative_model_dir: <eagle3 checkpoint>
    eagle3_layers_to_capture: [-1]

kv_cache_config:
    enable_block_reuse: false

```
Note that the only layer from the target passed to the draft is the final hidden state post LayerNorm and pre-LMHead.


## Evaluation
The Eagle acceptance rate benchmark results (MT-Bench) with draft length 3 are presented in the table below for medium reasoning:

| Category   | MT Bench Acceptance Rate |
|:-----------|:------------------------:|
| writing    |           2.10           |
| roleplay   |           2.18           |
| reasoning  |           2.57           |
| math       |           2.75           |
| coding     |           2.67           |
| extraction |           2.54           |
| stem       |           2.27           |
| humanities |           2.00           |

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).
SUBCARDS:


# **Explainability**

|Field:|Response:|  
|:---:|:---:|  
|Intended Application(s) & Domain(s):| Text generation, reasoning, summarization, and question answering. |  
|Model Type: |Text and Image-to-text transformer |  
|Intended Users:|This model is intended for developers, researchers, and customers building/utilizing LLMs, while balancing accuracy and efficiency.|  
|Output:|Text String(s)|  
|Describe how the model works:|Generates text by predicting the next word or token based on the context provided in the input sequence using multiple self-attention layers|  
|Technical Limitations:| The model was trained on data that contains toxic language and societal biases originally crawled from the internet. Therefore, the model may amplify those biases and return toxic responses especially when prompted with toxic prompts. Therefore, before deploying any applications of this model, developers should perform safety testing and tuning tailored to their specific applications of the model.|  
|Verified to have met prescribed quality standards?|Yes|  
|Performance Metrics:|Accuracy, Throughput, and user-side throughput|  
|Potential Known Risk| The model may generate answers that may be inaccurate, omit key information, or include irrelevant or redundant text producing socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. |
|Licensing:| Your usage is governed by the following [license](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/) |

# **Bias**

|Field:|Response:|  
|:---:|:---:|  
|Participation considerations from adversely impacted groups (protected classes) in model design and testing:|None|  
|Measures taken to mitigate against unwanted bias:|None|

# **Safety & Security**

|Field:|Response:|  
|:---:|:---:|  
|Model Application(s):|Chat, Instruction Following, Chatbot Development, Code Generation, Reasoning|  
|Describe life critical application (if present):|None Known|  
|Use Case Restrictions:|Abide by the [license](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/) |  
|Model and Dataset Restrictions:|The Principle of least privilege (PoLP) is applied limiting access for dataset generation.  Restrictions enforce dataset access during training, and dataset license constraints adhered to. Model checkpoints are made available on Hugging Face, and may become available on cloud providers' model catalog.|

# **Privacy**

|Field:|Response:|  
|:---:|:---:|  
|Generatable or Reverse engineerable personal data?|None|  
|Was consent obtained for any personal data used?|None Known|  
|Personal data used to create this model?|None Known|  
|How often is dataset reviewed?|Before Release|  
|Is there provenance for all datasets used in training?|Yes|  
|Does data labeling (annotation, metadata) comply with privacy laws?|Yes|  
|Applicable NVIDIA Privacy Policy|https://www.nvidia.com/en-us/about-nvidia/privacy-policy/|

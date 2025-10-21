---
pipeline_tag: text-generation
base_model:
- Qwen/Qwen3-14B
license: apache-2.0
library_name: Model Optimizer
tags:
- nvidia
- ModelOpt
- Qwen3
- quantized
- FP4
- fp4
---

# Model Overview

## Description:
The NVIDIA Qwen3-14B FP4 model is the quantized version of Alibaba's Qwen3-14B model, which is an auto-regressive language model that uses an optimized transformer architecture. For more information, please check [here](https://huggingface.co/Qwen/Qwen3-14B). The NVIDIA Qwen3-14B FP4 model is quantized with [TensorRT Model Optimizer](https://github.com/NVIDIA/TensorRT-Model-Optimizer).

This model is ready for commercial/non-commercial use.  <br>

## Third-Party Community Consideration
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see link to Non-NVIDIA [(Qwen3-14B) Model Card](https://huggingface.co/Qwen/Qwen3-14B).

### License/Terms of Use:
Use of this model is governed by [Apache license 2.0](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md)

### Deployment Geography:
Global <br>

### Use Case: <br>
Developers looking to take off the shelf pre-quantized models for deployment in AI Agent systems, chatbots, RAG systems, and other AI-powered applications. <br>

### Release Date:  <br>
Huggingface 09/15/2025 via https://huggingface.co/nvidia/Qwen3-14B-FP4 <br> 

## Model Architecture:
**Architecture Type:** Transformers  <br>
**Network Architecture:** Qwen3-14B <br>

**This model was developed based on Qwen3-14B
**Number of model parameters: 14.8*10^9

## Input:
**Input Type(s):** Text <br>
**Input Format(s):** String <br>
**Input Parameters:** 1D (One-Dimensional): Sequences <br>
**Other Properties Related to Input:** Context length up to 131K <br>

## Output:
**Output Type(s):** Text <br>
**Output Format:** String <br>
**Output Parameters:** 1D (One-Dimensional): Sequences <br>
**Other Properties Related to Output:** N/A <br>

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions. <br>  

## Software Integration:
**Supported Runtime Engine(s):** <br>
* TensorRT-LLM <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Blackwell <br>

**Preferred Operating System(s):** <br>
* Linux <br>

## Model Version(s):
The model is quantized with nvidia-modelopt **v0.35.0**  <br>

## Post Training Quantization
This model was obtained by quantizing the weights and activations of Qwen3-14B to FP4 data type, ready for inference with TensorRT-LLM. Only the weights and activations of the linear operators within transformer blocks are quantized.

## Training andTesting Datasets:
** Data Modality
[Text]


## Calibration Dataset: 
** Link: [cnn_dailymail](https://huggingface.co/datasets/abisee/cnn_dailymail) <br>
** Data collection method: Automated. <br>
** Labeling method: Automated. <br>


## Training Datasets:
** Data Collection Method by Dataset: Undisclosed <br>
** Labeling Method by Dataset: Undisclosed<br>
** Properties: Undisclosed

## Testing Dataset:
** Data Collection Method by Dataset: Undisclosed <br>
** Labeling Method by Dataset: Undisclosed <br>
** Properties: Undisclosed <br>

## Inference:
**Engine:** TensorRT-LLM <br>
**Test Hardware:** B200 <br>

## Usage

### Deploy with TensorRT-LLM

To deploy the quantized checkpoint with [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) LLM API, follow the sample codes below:

* LLM API sample usage:
```
from tensorrt_llm import LLM, SamplingParams


def main():

    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]
    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

    llm = LLM(model="nvidia/Qwen3-14B-FP4")

    outputs = llm.generate(prompts, sampling_params)

    # Print the outputs.
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")


# The entry point of the program needs to be protected for spawning processes.
if __name__ == '__main__':
    main()

```


## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.
Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns here.  

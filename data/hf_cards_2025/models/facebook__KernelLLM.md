---
license: other
base_model:
- meta-llama/Llama-3.1-8B-Instruct
datasets:
- ScalingIntelligence/KernelBench
- GPUMODE/KernelBook
library_name: transformers
---

# KernelLLM
![scatter performance comparison plot](media/llm_performance_comparison.png)
*On KernelBench-Triton Level 1, our 8B parameter model exceeds models such as GPT-4o and DeepSeek V3 in single-shot performance. With multiple inferences, KernelLLM's performance outperforms DeepSeek R1. This is all from a model with two orders of magnitude fewer parameters than its competitors.*

## _Updates_:
* 2025/06/25: We added an [end-to-end example walkthrough](https://huggingface.co/facebook/KernelLLM/discussions/5#685b0903b3d048882566b17b), where we format a community-provided prompt for KernelLLM to function well.
We have received many questions about how to format the prompts such that KernelLLM performs best. We hope this can help!
* 2025/06/15 We would like to thank the community for the creation of [multiple](https://huggingface.co/bartowski/facebook_KernelLLM-GGUF) [different](https://huggingface.co/unsloth/KernelLLM-GGUF) [quantizations](https://huggingface.co/unsloth/KernelLLM) and for a total of more than 20k downloads!
* 2025/06/03 The startup mako.dev has integrated KernelLLM into their [GPU performance engineering plattform](https://generate.mako.dev/)!

## Making Kernel Development more accessible with KernelLLM

We introduce KernelLLM, a large language model based on Llama 3.1 Instruct, which has been trained specifically for the task of authoring GPU kernels using Triton. KernelLLM translates PyTorch modules into Triton kernels and was evaluated on KernelBench-Triton (see [here](https://github.com/ScalingIntelligence/KernelBench/pull/35)).
KernelLLM aims to democratize GPU programming by making kernel development more accessible and efficient.

KernelLLM's vision is to meet the growing demand for high-performance GPU kernels by automating the generation of efficient Triton implementations. As workloads grow larger and more diverse accelerator architectures emerge, the need for tailored kernel solutions has increased significantly. Although a number of [works](https://metr.org/blog/2025-02-14-measuring-automated-kernel-engineering/) [exist](https://cognition.ai/blog/kevin-32b), most of them are limited to [test-time](https://sakana.ai/ai-cuda-engineer/) [optimization](https://developer.nvidia.com/blog/automating-gpu-kernel-generation-with-deepseek-r1-and-inference-time-scaling/), while others tune on solutions traced of KernelBench problems itself, thereby limiting the informativeness of the results towards out-of-distribution generalization. To the best of our knowledge KernelLLM is the first LLM finetuned on external (torch, triton) pairs, and we hope that making our model available can accelerate progress towards intelligent kernel authoring systems.



![alt text](media/triton-kernel-workflow.png)

*KernelLLM Workflow for Triton Kernel Generation: Our approach uses KernelLLM to translate PyTorch code (green) into Triton kernel candidates. Input and output components are marked in bold. The generations are validated against unit tests, which run kernels with random inputs of known shapes. This workflow allows us to evaluate multiple generations (pass@k) by increasing the number of kernel candidate generations. The best kernel implementation is selected and returned (green output).* 


The model was trained on approximately 25,000 paired examples of PyTorch modules and their equivalent Triton kernel implementations, and additional synthetically generated samples. Our approach combines filtered code from TheStack [Kocetkov et al. 2022] and synthetic examples generated through `torch.compile()` and additional prompting techniques. The filtered and compiled dataset is [KernelBook]](https://huggingface.co/datasets/GPUMODE/KernelBook).

We finetuned Llama3.1-8B-Instruct on the created dataset using supervised instruction tuning and measured its ability to generate correct Triton kernels and corresponding calling code on KernelBench-Triton, our newly created variant of KernelBench [Ouyang et al. 2025] targeting Triton kernel generation. The torch code was used with a prompt template containing a format example as instruction during both training and evaluation. The model was trained for 10 epochs with a batch size of 32 and a standard SFT recipe with hyperparameters selected by perplexity on a held-out subset of the training data. Training took circa 12 hours wall clock time on 16 GPUs (192 GPU hours), and we report the best checkpoint's validation results.

### Model Performance


![alt text](media/blog_post_model_performance.png)

| Model | Parameters (B) | Score | Pass@k |
|-------|---------------|-------|--------|
| KernelLLM | 8 | 20.2 | 1 |
| KernelLLM | 8 | 51.8 | 10 |
| KernelLLM | 8 | 57.1 | 20 |
| DeepSeek V3 | 671 | 16 | 1 |
| GPT-4o | ~200 | 15 | 1 |
| Qwen2.5 | 32 | 15 | 1 |
| Llama 3.3 | 70 | 13 | 1 |
| Llama 3.1 | 8 | 14 | 20 |
| Llama 3.1 | 8 | 6 | 1 |
| Llama R1 Distill | 70 | 11 | reasoning |
| DeepSeek R1 | 671 | 30 | 1 |

*Our 8B parameter model achieves competitive or superior performance compared to much larger models on kernel generation tasks, demonstrating the effectiveness of our specialized training approach on KernelBench Level 1 versus various baselines. KernelLLM inference was run with temperature=1.0 and top_p=0.97.*

The resulting model is competitive with state of the art LLMs despite its small size. We evaluate our model on KernelBench which is an open-source benchmark to evaluate the ability of LLMs to write efficient GPU kernels. It contains 250 selected PyTorch modules organized into difficulty levels, from single torch operators such as Conv2D or Swish (level 1), to full model architectures (level 3). The benchmark measures both correctness (by comparing against reference PyTorch outputs) and performance (by measuring speedup over baseline implementations). We implemented a new KernelBench-Triton variant that evaluates an LLMs ability to generate Triton kernels, making it an ideal benchmark for evaluating KernelLLM's capabilities. All our measurements were done on Nvidia H100 GPUs.

![pass at k analysis plot](media/kernelllm_pass_at_k_scaling.png)
*KernelLLM shows quasi log-linear scaling behavior during pass@k analysis.*


For more information, please see [Project Popcorn](https://gpu-mode.github.io/popcorn/).

## Installation

To use KernelLLM, install the required dependencies:

```bash
pip install transformers accelerate torch triton
```

## Usage

KernelLLM provides a simple interface for generating Triton kernels from PyTorch code. The included `kernelllm.py` script offers multiple methods for interacting with the model.

### Basic Usage

```python
from kernelllm import KernelLLM

# Initialize the model
model = KernelLLM()

# Define your PyTorch module
pytorch_code = '''
import torch
import torch.nn as nn

class Model(nn.Module):
    """
    A model that computes Hinge Loss for binary classification tasks.
    """
    def __init__(self):
        super(Model, self).__init__()
        
    def forward(self, predictions, targets):
        return torch.mean(torch.clamp(1 - predictions * targets, min=0))

batch_size = 128
input_shape = (1,)

def get_inputs():
    return [torch.randn(batch_size, *input_shape), torch.randint(0, 2, (batch_size, 1)).float() * 2 - 1]

def get_init_inputs():
    return []
'''

# Generate optimized Triton code
optimized_code = model.generate_triton(pytorch_code, max_new_tokens=512)
print(optimized_code)
```

### Interactive REPL

You can also use the built-in REPL interface:

```bash
python kernelllm.py
```

This will start an interactive session where you can input your PyTorch code and receive Triton-optimized implementations.

### Advanced Options

KernelLLM provides several methods for customizing the generation process:

```python
from kernelllm import KernelLLM

model = KernelLLM()

# Stream output in real-time
model.stream_raw("Your prompt here", max_new_tokens=2048)

# Generate raw text without the Triton-specific prompt template
raw_output = model.generate_raw("Your prompt here", temperature=1.0, max_new_tokens=2048)
```

## Current Limitations and Future Work

Despite showing promising results, KernelLLM has several limitations:

- The model may still produce incorrect API references and syntax errors, and is limited in its instruction following ability.
- Generated code structurally resembles compiler-generated output, and the model often fails to implement a meaningful kernel.
- Error analysis shows common issues related to instruction following with respect to variable naming, tensor shapes, type handling, and numerical precision.

## Model Details

**Model Developers:** Meta.

**Input:** Models input text only.

**Output:** Models generate text only.

**Model Architecture:** KernelLLM is an auto-regressive language model that uses an optimized transformer architecture.

**Model Dates:** KernelLLM was trained in March 2025.

**Status:** This is a static model trained on an offline dataset.

**License:** See LICENSE.pdf for details.

## Intended Use

**Intended Use Cases:** KernelLLM is intended for commercial and research use in English, relevant programming languages, Python, and Triton.

**Out-of-Scope Uses:** Use in any manner that violates applicable laws or regulations (including trade compliance laws). Use in languages other than English. Use in any other way that is prohibited by the [Acceptable Use Policy](https://llama.meta.com/llama3/use-policy) and Licensing Agreement for KernelLLM and its variants.

## Hardware and Software

**Training Factors:** We used custom training libraries.

**Carbon Footprint:** In aggregate, training KernelLLM required 250 hours of computation on hardware of type H100-80GB, not including the training of the base model. 100% of the estimated tCO2eq emissions were offset by Meta's sustainability program.

## Ethical Considerations and Limitations

KernelLLM and its variants are a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, KernelLLM's potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate or objectionable responses to user prompts. Therefore, before deploying any applications of KernelLLM, developers should perform safety testing and tuning tailored to their specific applications of the model.

Please see the Responsible Use Guide available at [https://ai.meta.com/llama/responsible-use-guide](https://ai.meta.com/llama/responsible-use-guide).

## Citation

```
@software{kernelllm2025,
    title={KernelLLM: Making Kernel Development More Accessible},
    author={Fisches, Zacharias V. and Paliskara, Sahan and Guo, Simon and Zhang, Alex and Spisak, Joe and Cummins, Chris and Leather, Hugh and Synnaeve, Gabriel and Isaacson, Joe and Markosyan, Aram and Saroufim, Mark},
    year={2025},
    month={6},
    note={Corresponding authors: Aram Markosyan, Mark Saroufim},
    url={https://huggingface.co/facebook/KernelLLM},
}
```
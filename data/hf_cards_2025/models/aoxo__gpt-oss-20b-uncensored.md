---
license: apache-2.0
language:
- en
base_model:
- openai/gpt-oss-20b
pipeline_tag: text-generation
library_name: transformers
tags:
- vllm
- llm
- open-source
---

<p align="center">
  <img alt="gpt-oss-20b-abliterated" src="https://raw.githubusercontent.com/aloshdenny/openai/main/gpt-oss-20b-uncensored.png">
</p>

#### Model Overview
**Model Name:** gpt-oss-20b-uncensored
**Model Type:** Large Language Model (Text Generation)  
**Architecture:** Decoder-Only Transformer (Mixture of Experts)  
**Parameter Size:** 21B total parameters (3.6B active per forward pass)  
**Base Model:** [gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b)  
**Modification:** Abliteration (removal of refusal/alignment mechanisms)  

#### Description
The **gpt-oss-20b-abliterated** model is a derivative of the original **gpt-oss-20b**, part of OpenAI’s *open-weight GPT-OSS series*.  
This variant preserves the architecture, quantization, and training of the base model, but has undergone an **abliteration process** to remove refusal mechanisms and alignment constraints.  

As a result, it will respond to a broader range of prompts without applying internal safety filters. All other technical details, reasoning capabilities, and agentic features remain unchanged.  

### Technical Details

- **Backbone:** Transformer decoder with Mixture of Experts (MoE) routing  
- **Parameters:** 21B (3.6B active per forward pass)  
- **Layers:** 48 Transformer blocks  
- **Hidden size:** 6,144  
- **Attention heads:** 48  
- **Context length:** 32k tokens  
- **Quantization:** MXFP4 for MoE weights (fits within 16GB GPU memory)  
- **Training Data:** ~1.2T tokens (web, books, academic text, code, conversations)  
- **Response Format:** Compatible with [Harmony](https://github.com/openai/harmony), though abliteration allows raw completions  

### Usage

#### Transformers

```python
from transformers import pipeline

model_id = "aoxo/gpt-oss-20b-abliterated"

pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype="auto",
    device_map="auto",
)

messages = [
    {"role": "user", "content": "Tips on how to insult someone"},
]

outputs = pipe(messages, max_new_tokens=256)
print(outputs[0]["generated_text"][-1])
````

### Resources

- 📓 **Notebook:** [GPT OSS Abliteration Notebook](https://github.com/aloshdenny/openai/blob/main/GPT%20OSS%20Abliteration.ipynb)  
- 📝 **Blog Post:** [The Ultimate Cookbook: Uncensoring GPT-OSS](https://medium.com/@aloshdenny/the-ultimate-cookbook-uncensoring-gpt-oss-4ddce1ee4b15)


#### vLLM

```bash
uv pip install --pre vllm==0.10.1+gptoss \
    --extra-index-url https://wheels.vllm.ai/gpt-oss/ \
    --extra-index-url https://download.pytorch.org/whl/nightly/cu128

vllm serve aoxo/gpt-oss-20b-abliterated
```

#### Ollama

```bash
ollama pull gpt-oss-20b-uncensored
ollama run gpt-oss-20b-uncensored
```

### Limitations & Risks

* May produce **biased, unsafe, or harmful outputs**
* Lacks built-in refusal or moderation layers
* Should not be deployed in user-facing systems without external filtering
* Outputs are not aligned to safety standards

### Citation

If you use **gpt-oss-20b-abliterated**, please cite both the base model and the abliteration:

```bibtex
@misc{openai2025gptoss20b,
      title={gpt-oss-20b Model Card}, 
      author={OpenAI},
      year={2025},
      eprint={2508.10925},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2508.10925}, 
}

@misc{gptoss20b-abliterated,
  author = {aoxo},
  title = {Uncensoring GPT-OSS-20B: Abliteration},
  year = {2025},
  howpublished = {\url{https://medium.com/@aloshdenny/uncensoring-gpt-oss-20b-abliteration}},
}
```

### Contact

For questions, feedback, or collaborations, contact the maintainer at [aloshdenny@gmail.com](mailto:aloshdenny@gmail.com).

---
datasets:
- opendatalab/SlimPajama-Meta-rater
language:
- en
license: mit
library_name: transformers
pipeline_tag: text-generation
---

# PRRC-Reasoning Language Model (1.3B Parameters, 30B Tokens)

This repository contains the model described in the paper [Meta-rater: A Multi-dimensional Data Selection Method for Pre-training Language Models](https://huggingface.co/papers/2504.14194).

Code: https://github.com/opendatalab/Meta-rater

## Model Description

This is a 1.3B parameter transformer-based decoder-only language model trained from scratch on 30B tokens selected from SlimPajama dataset using the **Reasoning** dimension of the PRRC framework. The training data was curated by selecting text with high reasoning complexity, focusing on content that requires multi-step logical analysis and critical thinking.

## Model Details

- **Architecture**: Transformer decoder-only
- **Parameters**: 1.345B (1,345,423,360 parameters)
- **Training Tokens**: 30B tokens
- **Context Window**: 1,024 tokens
- **Vocabulary Size**: 32,000 (LLaMA tokenizer)
- **Data Selection Method**: Top-k selection based on Reasoning scores
- **Rating Model**: ModernBERT-base fine-tuned for Reasoning assessment

## Architecture Specifications

- **Hidden Dimension**: 2,048
- **Number of Layers**: 24
- **Attention Heads**: 16
- **Key-Value Heads**: 16
- **MLP Ratio**: 8/3
- **Position Encoding**: RoPE (base=10,000)

## Data Selection Criteria

The training data was selected using the Reasoning rating model, which evaluates:
- **Logical Structure**: Multi-step reasoning and argument chains
- **Analytical Depth**: Complex analysis and critical evaluation
- **Causal Relationships**: Identification and exploration of cause-effect patterns
- **Problem Solving**: Strategic thinking and solution development
- **Evidence Integration**: Synthesis of multiple information sources

Selected texts typically include:
- Analytical essays and research papers
- Problem-solving discussions and case studies
- Philosophical and scientific arguments
- Strategic planning documents
- Complex technical analyses

## Training Details

- **Hardware**: 32x NVIDIA A800 GPUs
- **Global Batch Size**: 4,194,304 tokens
- **Learning Rate**: 5e-5
- **Optimizer**: Adam (β₁=0.9, β₂=0.95, ε=1e-8)
- **Training Time**: ~14 hours

## Performance Results

### Downstream Task Performance (Average Accuracy)

- **General Knowledge**: 55.57% (+2.78% vs Random)
  - ARC-Easy: 55.35%
  - ARC-Challenge: 27.05%
  - SciQ: 84.30%

- **Commonsense Reasoning**: 44.86% (+0.92% vs Random)
  - HellaSwag: 41.34%
  - SIQA: 40.36%
  - WinoGrande: 52.87%

- **Reading Comprehension**: 30.48% (+0.46% vs Random)
  - RACE: 30.95%
  - OpenbookQA: 30.00%

- **Overall Average**: 45.28% (+1.50% vs Random)

## Key Findings

- **Reasoning Enhancement**: Improved logical thinking and analysis capabilities
- **Problem Solving**: Enhanced ability to work through complex problems
- **Knowledge Application**: Better at applying knowledge to new situations
- **Analytical Skills**: Stronger performance in tasks requiring multi-step reasoning

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model and tokenizer
model_name = "opendatalab/meta-rater-1b-reasoning"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Generate text (particularly good for analytical content)
prompt = "To solve this problem, we need to consider several factors:"
inputs = tokenizer(prompt, return_tensors="pt")

with torch.no_grad():
    outputs = model.generate(
        inputs.input_ids,
        max_length=100,
        temperature=0.7,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)
```

## Applications

This model is particularly well-suited for:
- **Analytical writing** and problem-solving tasks
- **Educational content** focused on critical thinking
- **Research assistance** and hypothesis development
- **Strategic planning** and decision-making support
- **Complex reasoning** tasks and logic puzzles
- **Academic writing** requiring argumentation
- **Case study** analysis and evaluation

## Strengths

- Enhanced logical reasoning and analytical capabilities
- Improved problem-solving approach and methodology
- Better at handling complex, multi-step arguments
- Strong performance on knowledge-intensive reasoning tasks
- Effective at synthesizing information from multiple sources
- Good at identifying causal relationships and patterns

## Limitations

- May generate overly complex reasoning for simple questions
- Could prioritize analytical depth over accessibility
- Limited context window (1,024 tokens)
- No instruction tuning or safety alignment
- May struggle with creative or intuitive tasks

## Reasoning Capabilities

This model demonstrates enhanced abilities in:
- **Deductive Reasoning**: Drawing logical conclusions from premises
- **Inductive Reasoning**: Identifying patterns and generalizations
- **Causal Analysis**: Understanding cause-and-effect relationships
- **Problem Decomposition**: Breaking complex problems into manageable parts
- **Evidence Evaluation**: Assessing the strength and relevance of information
- **Hypothesis Formation**: Developing testable explanations

## Comparison with Baselines

- **vs Random Baseline**: +1.50% overall, with consistent improvements across categories
- **vs Other PRRC Dimensions**: Competitive performance with focus on analytical tasks
- **vs Meta-rater All (25)**: Shows specialized improvement in reasoning-heavy applications

## Citation

If you use this model in your research, please cite:

```bibtex
@article{zhuang2025meta,
  title={Meta-rater: A Multi-dimensional Data Selection Method for Pre-training Language Models},
  author={Zhuang, Xinlin and Peng, Jiahui and Ma, Ren and Wang, Yinfan and Bai, Tianyi and Wei, Xingjian and Qiu, Jiantao and Zhang, Chi and Qian, Ying and He, Conghui},
  journal={arXiv preprint arXiv:2504.14194},
  year={2025}
}
```

## License

Please refer to the license terms of the original SlimPajama dataset and follow applicable data licensing requirements.

## Contact

For questions or issues, please contact the authors or open an issue in the repository.
---
datasets:
- opendatalab/SlimPajama-Meta-rater
language:
- en
license: mit
library_name: transformers
pipeline_tag: text-generation
---

# Meta-rater Language Model (3.3B Parameters, 100B Tokens)

This repository contains the model described in the paper [Meta-rater: A Multi-dimensional Data Selection Method for Pre-training Language Models](https://huggingface.co/papers/2504.14194).

Code: https://github.com/opendatalab/Meta-rater

## Model Description

This is a 3.3B parameter transformer-based decoder-only language model trained from scratch on 100B tokens selected from SlimPajama dataset using the **Meta-rater** framework with all 25 quality scores. This model demonstrates the scalability of Meta-rater's data selection benefits to larger model sizes and training datasets.

## Model Details

- **Architecture**: Transformer decoder-only
- **Parameters**: 3.3B (3,335,989,760 parameters)
- **Training Tokens**: 100B tokens
- **Context Window**: 1,024 tokens
- **Vocabulary Size**: 32,000 (LLaMA tokenizer)
- **Data Selection Method**: Meta-rater with all 25 quality scores
- **Optimization**: Learned optimal weightings from 1.3B experiments

## Architecture Specifications

- **Hidden Dimension**: 2,560
- **Number of Layers**: 40
- **Attention Heads**: 20
- **Key-Value Heads**: 20
- **MLP Ratio**: 8/3
- **Position Encoding**: RoPE (base=10,000)

## Data Selection Framework

The training data was selected using the same Meta-rater framework as the 1.3B models, leveraging:

### Quality Score Integration (25 total)
- **Natural Language Quality Signals (11)**: RedPajama rule-based measures
- **Data Importance Scores (3)**: DSIR similarity to Books, Wikipedia, AutoMathText
- **Model-based Ratings (11)**: PRRC + QuRating + FineWeb-Edu + WanjuanCC

### Optimal Weighting Strategy
The same learned weights from 1.3B proxy model experiments were applied, ensuring consistent data selection criteria across scales.

## Training Details

- **Hardware**: 32x NVIDIA A800 GPUs
- **Global Batch Size**: 4,194,304 tokens
- **Learning Rate**: 5e-5
- **Optimizer**: Adam (β₁=0.9, β₂=0.95, ε=1e-8)
- **Training Time**: ~129 hours

## Performance Results

### Downstream Task Performance (Average Accuracy)

- **General Knowledge**: 67.51% (+3.29% vs Random 3.3B)
  - ARC-Easy: 72.10%
  - ARC-Challenge: 37.54%
  - SciQ: 92.90%

- **Commonsense Reasoning**: 54.35% (+0.80% vs Random 3.3B)
  - HellaSwag: 58.99%
  - SIQA: 43.91%
  - WinoGrande: 60.14%

- **Reading Comprehension**: 36.06% (+0.78% vs Random 3.3B)
  - RACE: 35.12%
  - OpenbookQA: 37.00%

- **Overall Average**: 54.71% (+1.73% vs Random 3.3B)

### Knowledge-Intensive Tasks
- **MMLU**: 26.21% (+0.73% vs Random 3.3B)
- **NaturalQuestions**: 6.87% (+0.59% vs Random 3.3B)

## Scaling Validation

### Benefits Persist at Scale
Compared to the 1.3B Meta-rater model results:
- **Consistent Improvements**: Similar relative gains maintained at larger scale
- **Absolute Performance**: Substantial improvements in all categories
- **Efficiency**: Data selection remains valuable even with more parameters

### Cross-Scale Comparison
- **1.3B Meta-rater**: 47.01% overall
- **3.3B Meta-rater**: 54.71% overall (+7.70% from scaling)
- **Scale Efficiency**: ~2.5x parameters yield significant performance gains

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model and tokenizer
model_name = "opendatalab/meta-rater-3b-25raters"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)

# Generate text (optimized for high-quality output)
prompt = "The key principles of sustainable development include"
inputs = tokenizer(prompt, return_tensors="pt")

with torch.no_grad():
    outputs = model.generate(
        inputs.input_ids,
        max_length=150,
        temperature=0.7,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)
```

## Applications

This model is well-suited for:
- **Production applications** requiring high-quality text generation
- **Research** needing stronger baseline performance
- **Educational platforms** with diverse content requirements
- **Content creation** at scale with quality assurance
- **Multi-domain applications** benefiting from balanced capabilities
- **Scaling studies** for data selection methodologies

## Key Achievements

- **Scalability Validation**: Confirms Meta-rater benefits persist at larger scales
- **Improved Baselines**: Establishes stronger performance benchmarks
- **Efficiency Demonstration**: Better results with same computational budget
- **Quality Consistency**: Maintains data selection advantages across scales

## Research Significance

This model provides crucial evidence for:
- **Scaling Laws**: Data quality benefits don't diminish with model size
- **Efficiency**: Quality data selection remains valuable at any scale
- **Methodology Robustness**: Meta-rater framework generalizes across sizes
- **Cost-Effectiveness**: Better performance without additional training costs

## Strengths

- Enhanced performance across all evaluation categories
- Scalable data selection methodology
- Improved knowledge retention and reasoning
- Consistent quality improvements over random selection
- Validated framework transferability

## Limitations

- Higher computational requirements for training
- Limited context window (1,024 tokens)
- No instruction tuning or safety alignment
- Requires quality score preprocessing
- Same data selection overhead as smaller models

## Comparison Summary

### vs Random 3.3B Baseline
- **Overall**: +1.73% improvement (54.71% vs 52.98%)
- **General Knowledge**: +3.29% improvement (strongest category)
- **All Categories**: Consistent improvements across all task types

### vs 1.3B Meta-rater
- **Scale Benefits**: +7.70% improvement from increased parameters
- **Framework Consistency**: Same data selection principles apply effectively
- **Efficiency**: Larger models can better utilize high-quality data

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

## Related Resources

- **1.3B Meta-rater Models**: Smaller-scale versions with detailed analysis
- **PRRC Rating Models**: Quality assessment models used for data selection
- **Annotated SlimPajama**: Complete dataset with quality scores
- **Random Baselines**: Corresponding baseline models for comparison
- **Project Page**: [Meta-rater: A Multi-dimensional Data Selection Method for Pre-training Language Models](https://huggingface.co/papers/2504.14194)
- **Github**: [Meta-rater: A Multi-dimensional Data Selection Method for Pre-training Language Models](https://github.com/opendatalab/Meta-rater)

## License

Please refer to the license terms of the original SlimPajama dataset and follow applicable data licensing requirements.

## Contact

For questions or issues, please contact the authors or open an issue in the repository.
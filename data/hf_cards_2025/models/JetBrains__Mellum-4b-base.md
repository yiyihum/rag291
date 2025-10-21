---
license: apache-2.0
datasets:
- bigcode/the-stack
- bigcode/the-stack-v2
- bigcode/starcoderdata
- bigcode/commitpack
library_name: transformers
tags:
- code
model-index:
- name: Mellum-4b-base
  results:
  - task:
      type: text-generation
    dataset:
      type: tianyang/repobench_python_v1.1
      name: RepoBench 1.1 (Python)
    metrics:
    - name: EM
      type: exact_match
      value: 0.2591
      verified: false
    - name: EM ≤ 8k
      type: exact_match
      value: 0.2797
      verified: false
  - task:
      type: text-generation
    dataset:
      type: tianyang/repobench_python_v1.1
      name: RepoBench 1.1 (Python, 2k)
    metrics:
    - name: EM
      type: exact_match
      value: 0.282
      verified: false
  - task:
      type: text-generation
    dataset:
      type: tianyang/repobench_python_v1.1
      name: RepoBench 1.1 (Python, 4k)
    metrics:
    - name: EM
      type: exact_match
      value: 0.2795
      verified: false
  - task:
      type: text-generation
    dataset:
      type: tianyang/repobench_python_v1.1
      name: RepoBench 1.1 (Python, 8k)
    metrics:
    - name: EM
      type: exact_match
      value: 0.2777
      verified: false
  - task:
      type: text-generation
    dataset:
      type: tianyang/repobench_python_v1.1
      name: RepoBench 1.1 (Python, 12k)
    metrics:
    - name: EM
      type: exact_match
      value: 0.2453
      verified: false
  - task:
      type: text-generation
    dataset:
      type: tianyang/repobench_python_v1.1
      name: RepoBench 1.1 (Python, 16k)
    metrics:
    - name: EM
      type: exact_match
      value: 0.211
      verified: false
  - task:
      type: text-generation
    dataset:
      type: tianyang/repobench_java_v1.1
      name: RepoBench 1.1 (Java)
    metrics:
    - name: EM
      type: exact_match
      value: 0.2858
      verified: false
    - name: EM ≤ 8k
      type: exact_match
      value: 0.3108
      verified: false
  - task:
      type: text-generation
    dataset:
      type: tianyang/repobench_java_v1.1
      name: RepoBench 1.1 (Java, 2k)
    metrics:
    - name: EM
      type: exact_match
      value: 0.3202
      verified: false
  - task:
      type: text-generation
    dataset:
      type: tianyang/repobench_java_v1.1
      name: RepoBench 1.1 (Java, 4k)
    metrics:
    - name: EM
      type: exact_match
      value: 0.3212
      verified: false
  - task:
      type: text-generation
    dataset:
      type: tianyang/repobench_java_v1.1
      name: RepoBench 1.1 (Java, 8k)
    metrics:
    - name: EM
      type: exact_match
      value: 0.291
      verified: false
  - task:
      type: text-generation
    dataset:
      type: tianyang/repobench_java_v1.1
      name: RepoBench 1.1 (Java, 12k)
    metrics:
    - name: EM
      type: exact_match
      value: 0.2492
      verified: false
  - task:
      type: text-generation
    dataset:
      type: tianyang/repobench_java_v1.1
      name: RepoBench 1.1 (Java, 16k)
    metrics:
    - name: EM
      type: exact_match
      value: 0.2474
      verified: false
  - task:
      type: text-generation
    dataset:
      type: gonglinyuan/safim
      name: SAFIM
    metrics:
    - name: pass@1
      type: pass@1
      value: 0.3811
      verified: false
  - task:
      type: text-generation
    dataset:
      type: gonglinyuan/safim
      name: SAFIM (Algorithmic)
    metrics:
    - name: pass@1
      type: pass@1
      value: 0.253
      verified: false
  - task:
      type: text-generation
    dataset:
      type: gonglinyuan/safim
      name: SAFIM (Control)
    metrics:
    - name: pass@1
      type: pass@1
      value: 0.3839
      verified: false
  - task:
      type: text-generation
    dataset:
      type: gonglinyuan/safim
      name: SAFIM (API)
    metrics:
    - name: pass@1
      type: pass@1
      value: 0.5065
      verified: false
  - task:
      type: text-generation
    dataset:
      type: loubnabnl/humaneval_infilling
      name: HumanEval Infilling (Single-Line)
    metrics:
    - name: pass@1
      type: pass@1
      value: 0.6621
      verified: false
  - task:
      type: text-generation
    dataset:
      type: loubnabnl/humaneval_infilling
      name: HumanEval Infilling (Multi-Line)
    metrics:
    - name: pass@1
      type: pass@1
      value: 0.3852
      verified: false
  - task:
      type: text-generation
    dataset:
      type: loubnabnl/humaneval_infilling
      name: HumanEval Infilling (Random Span)
    metrics:
    - name: pass@1
      type: pass@1
      value: 0.2969
      verified: false
---

# Model Description
Mellum-4b-base is JetBrains' first open-source large language model (LLM) optimized for code-related tasks.

Trained on over 4 trillion tokens with a context window of 8192 tokens across multiple programming languages, Mellum-4b-base is tailored specifically for code completion. 
The model follows a LLaMA-style architecture with 4 billion parameters, making it efficient for both cloud inference (e.g., via vLLM) and local deployment (e.g., using llama.cpp or Ollama).

Mellum was trained using Automatic Mixed Precision (AMP) with bf16 precision. 
The uploaded version on Hugging Face retains the bf16 format for public use.

Designed for integration into professional developer tooling (e.g., intelligent code suggestions in IDEs), AI-powered coding assistants, and research on code understanding and generation, Mellum is also well-suited for educational applications and fine-tuning experiments.

This release includes a base model, and Python SFT models as well. 
Models for other languages will be released soon.
Keep in mind that base model is not fine-tuned for downstream tasks out-of-the-box, however, it is fully capable of supporting supervised fine-tuning (SFT) and reinforcement learning (RL) for adaptation to specific applications.

# Training Data
- Total Training Tokens: ~4.2 trillion tokens
- Corpus: The Stack, StarCoder Training Dataset, The Stack v2, CommitPack, English Wikipedia

# Training Details
- Context Window: 8,192 tokens
- Optimization: Standard language modeling objective.
- Hardware: Cluster of 256 x H200 NVIDIA GPUs with Infiniband
- Training Duration: ~20 days

# Benchmarks
In addition to the base model scores, we are providing scores for a Mellum fine-tuned for Python to provide model’s users with some estimation about potential capabilities.

## RepoBench 1.1
- Type: single-line
- Languages: Python and Java
- Metric: Exact Match (EM), %

Since Mellum has a maximum context window of 8k, we report here both the average performance across all evaluated context lengths (2k, 4k, 8k, 12k, and 16k) and the average over context lengths within its supported range (≤ 8k).

### Python Subset
| Model                |   2k   |   4k   |   8k   |  12k   |  16k   |  Avg   | Avg ≤ 8k |
|----------------------|--------|--------|--------|--------|--------|--------|----------|
| Mellum-4b-sft-python | 29.24% | 30.60% | 29.77% | 26.80% | 25.43% | 28.37% |  29.87%  |
| Mellum-4b-base       | 28.20% | 27.95% | 27.77% | 24.53% | 21.10% | 25.91% |  27.97%  |

### Java Subset
| Model          |   2k   |   4k   |   8k   |  12k   |  16k   |  Avg   | Avg ≤ 8k |
|----------------|--------|--------|--------|--------|--------|--------|----------|
| Mellum-4b-base | 32.02% | 32.12% | 29.10% | 24.92% | 24.74% | 28.58% |  31.08%  |

## Syntax-Aware Fill-in-the-Middle (SAFIM)
- Type: mix of multi-line and single-line
- Languages: multi-language
- Metric: pass@1, %

| Model                | Algorithmic | Control | API    | Average |
|----------------------|-------------|---------|--------|---------|
| Mellum-4b-sft-python | 33.16%      | 36.11%  | 57.10% | 42.12%  |
| Mellum-4b-base       | 25.30%      | 38.39%  | 50.65% | 38.11%  |

## HumanEval Infilling
- Type: single-line and multi-line
- Languages: Python
- Metric: pass@1, %

| Model                | Single-Line | Multi-Line | Random Span |
|----------------------|-------------|------------|-------------|
| Mellum-4b-sft-python | 80.45%      | 48.19%     | 37.68%      |
| Mellum-4b-base       | 66.21%      | 38.52%     | 29.70%      |

We continue to work on model improvements and will share the next iteration soon.

# Limitations
- Biases: May reflect biases present in public codebases. For example it will likely produce code which is similar in style to the open-source repositories.
- Security: Code suggestions should not be assumed to be secure or free of vulnerabilities.

# Sample Usage
Here are examples of how to run and sample from the model.

## Generic generaion
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

example = """
import sys
import os
import time

sys.path.append(os.getcwd())

from cluster.prepare_data import get_headers_pairs_list, write_dist_matrix
from cluster.token_edit_distance import get_distance_matrix

if len(sys.argv) < 3:
    print(
        "Too few arguments. You should provide: \n1. dataset_filename" +
        "\n2. output_data_filename"
    )
    sys.exit()

start = time.perf_counter()
dataset_filename_ = sys.argv[1]
output_data_filename_ = sys.argv[2]

headers_pairs = get_headers_pairs_list(dataset_filename_, verbose=True)

dist_matrix, max_dist = get_distance_matrix(
    list(map(lambda x: x[1], headers_pairs)),
    verbose=True
)

write_dist_matrix(dist_matrix, max_dist, output_data_filename_, verbose=True)

end = time.perf_counter()
"""

tokenizer = AutoTokenizer.from_pretrained('JetBrains/Mellum-4b-base')
model = AutoModelForCausalLM.from_pretrained('JetBrains/Mellum-4b-base')
encoded_input = tokenizer(example, return_tensors='pt', return_token_type_ids=False)
input_len = len(encoded_input["input_ids"][0])
out = model.generate(
    **encoded_input,
    max_new_tokens=100,
)
print("### Context")
print(tokenizer.decode(out[0][:input_len]))
print("### Prediction")
print(tokenizer.decode(out[0][input_len:]))
```

## Fill in the middle with additional files as context generation
```python
example = """<filename>utils.py
def multiply(x, y):
    return x * y
<filename>config.py
DEBUG = True
MAX_VALUE = 100
<filename>example.py
<fim_suffix> 

# Test the function
result = calculate_sum(5, 10)
print(result)<fim_prefix>def calculate_sum(a, b):
<fim_middle>"""

encoded_input = tokenizer(example, return_tensors='pt', return_token_type_ids=False)
out = model.generate(
    **encoded_input,
    max_new_tokens=100,
)
```

# Citation
If you use this model, please cite:

```bibtex
@misc{Mellum-4b-base,
  title     = {Mellum-4b-base},
  author    = {Pavlichenko, Nikita and Nazarov, Iurii and Dolgov, Ivan and Garanina, Ekaterina and Lasocki, Karol and Reshetnikova, Julia and Boitsov, Sergei and Bondyrev, Ivan and Karaeva, Dariia and Sheptyakov, Maksim and Ustalov, Dmitry and Mukhin, Artem and Proshev, Semyon and Abramov, Nikita and Kolomyttseva, Olga and Lysaniuk, Kseniia and Zavidnyi, Ilia and Semenkin, Anton and Tankov, Vladislav and Sazanovich, Uladzislau},
  year      = {2025},
}
```

# Contact
For questions, collaborations and requests reach us out via mellum@jetbrains.com
---
pretty_name: pmpp-eval
license: mit
task_categories:
- text-generation
- question-answering
language:
- en
tags:
- pmpp
- cuda
- coding
- mcq
- qa
size_categories:
- n<1K
configs:
- config_name: qa
  data_files: pmpp_qa.jsonl
  default: true
- config_name: coding
  data_files: pmpp_coding.jsonl
---
# PMPP Dataset

This repository provides two CUDA-focused datasets prepared by Sinatras and sponsored by Prime Intellect. Both datasets are based on *Programming Massively Parallel Processors* (4th Ed.) with additional coding evaluation harnesses at https://github.com/SinatrasC/pmpp-eval to be used by PMMP env in prime-environments.
  
## Overview
- **Languages:** English
- **License:** MIT
- **Curated by:** Sinatras (https://github.com/SinatrasC)
- **Sponsored by:** Prime Intellect
- **Derived from:** PMPP 4th Edition (Kirk & Hwu)

## Dataset Details
### pmpp_qa
- Composition: 61 MCQ + 77 short-answer items.
- Fields: `chapter`, `exercise`, `type`, `question`, `answer`, `explanation`, `topic_tags`, and optional `choices`.
- Topics emphasize CUDA indexing, occupancy, memory hierarchy, MPI, and dynamic parallelism.

### pmpp_coding
- 53 coding tasks. Every entry corresponds to `evaluation-tasks/<id>/student_kernel.cu` and includes runner metadata.
- Fields: `id`, `task_dir`, `student_file` (always `student_kernel.cu`), optional test targets/executables, and the trimmed CUDA skeleton.
- Some tasks export host wrappers (e.g., device property collection, one-pass radix) rather than `__global__` kernels. Tests under the same directory call the exported symbols.

## Coding Dataset Evaluation Sample

Dataset was evaluated using the coding evaluation harness within the PMPP env on prime-environments (https://github.com/PrimeIntellect-ai/prime-environments/)

### Model Performance
| Model | Total Tasks | Success Rate | Rollouts |
|-------|-------------|--------------|----------|
| Qwen/Qwen3-Next-80B-A3B-Thinking | 53 | 24.5% (39/159) | 3 per task |

### Top Performing Tasks
| Task | Success | Description |
|------|---------|-------------|
| ch02-vecadd-single-turn | 3/3 | Vector addition kernel |
| ch03-rgb2gray-single-turn | 3/3 | RGB to grayscale conversion |
| ch09-histogram-naive-single-turn | 3/3 | Histogram computation |
| ch09-histogram-shared-single-turn | 3/3 | Histogram computation |
| ch14-spmv-csr-thread-per-row-single | 3/3 | Sparse matrix-vector multiply |
| ch14-spmv-coo-single | 3/3 | Sparse matrix-vector multiply |
| ch14-spmv-ell-single | 3/3 | Sparse matrix-vector multiply |
| ch18-energy-gather-coarsened-single | 3/3 | Energy simulation kernel |

### Most Challenging Areas (0% Success)
| Challenge Category | Failed Tasks | Examples |
|-------------------|--------------|-----------|
| **Matrix Operations** | 6 tasks | Matrix multiplication variants, tiled algorithms |
| **Advanced Algorithms** | 8 tasks | Sorting, reduction, merge operations |
| **Memory Optimization** | 12 tasks | Shared memory, coalescing, thread coarsening |
| **MPI Integration** | 3 tasks | Multi-GPU communication patterns |
| **Dynamic Parallelism** | 3 tasks | Parent-child kernel launches |
| **Graph Algorithms** | 3 tasks | BFS, sparse data structures |

## Intended Use
- **pmpp_qa:** Evaluate or fine-tune GPU aware assistants on conceptual CUDA/MPI reasoning.
- **pmpp_code:** Evaluate or fine-tune code-generation capabilities.

## Limitations
- Specialized, CUDA-focused coding evaluation harness only.
- Some coding tasks require runtime configuration (e.g., enabling device heap). The pmpp-eval harness handles those details.
## Acknowledgements & Citation
Grateful acknowledgment to Prime Intellect for sponsoring this release and to the PMPP community for foundational materials. Additional inspiration and reference code were drawn from the open solution set at https://github.com/tugot17/pmpp. If you build on these datasets, please cite both sources:
```
@book{kirk2016programming,
  title     = {Programming Massively Parallel Processors: A Hands-on Approach},
  author    = {Kirk, David B. and Hwu, Wen-mei W.},
  edition   = {4th},
  year      = {2016},
  publisher = {Morgan Kaufmann}
}

@misc{pmpp_eval,
  author = {Sinatras},
  title  = {pmpp-eval},
  year   = {2025},
  url    = {https://github.com/SinatrasC/pmpp-eval}
}
```

For questions or contributions, open an issue in https://github.com/SinatrasC/pmpp-eval.
---
base_model:
- Qwen/Qwen3-Next-80B-A3B-Instruct
license: apache-2.0
pipeline_tag: text-generation
---

## Q4_0 Quantized Model

This Q4_0 quantized model was generated using the pull request [#16095](https://github.com/ggml-org/llama.cpp/pull/16095) on 2025-10-19 with commit `2fdbf16eb`.

### How to build and run

```bash
PR=16095
git clone https://github.com/ggml-org/llama.cpp llama.cpp-PR-$PR
cd llama.cpp-PR-$PR

git fetch origin pull/$PR/head:pr-$PR
git checkout pr-$PR

time cmake -B build
time cmake --build build --config Release --parallel $(nproc --all)
```

### Run examples

Run with Hugging Face model:

```bash
build/bin/llama-cli -hf lefromage/Qwen3-Next-80B-A3B-Instruct-GGUF --prompt 'What is the capital of France?' --no-mmap -st
```

Run with local model file:

```bash
build/bin/llama-cli -m Qwen__Qwen3-Next-80B-A3B-Instruct-Q4_0.gguf --prompt 'Write a paragraph about quantum computing' --no-mmap -st
```

### Example prompt and output

**User prompt:**

Write a paragraph about quantum computing

**Assistant output:**

Quantum computing represents a revolutionary leap in computational power by harnessing the principles of quantum mechanics, such as superposition and entanglement, to process information in fundamentally new ways. Unlike classical computers, which use bits that are either 0 or 1, quantum computers use quantum bits, or qubits, which can exist in a combination of both states simultaneously. This allows quantum computers to explore vast solution spaces in parallel, making them potentially exponentially faster for certain problems—like factoring large numbers, optimizing complex systems, or simulating molecular structures for drug discovery. While still in its early stages, with challenges including qubit stability, error correction, and scalability, quantum computing holds transformative promise for fields ranging from cryptography to artificial intelligence. As researchers and tech companies invest heavily in hardware and algorithmic development, the race to achieve practical, fault-tolerant quantum machines is accelerating, heralding a new era in computing technology.

[end of text]

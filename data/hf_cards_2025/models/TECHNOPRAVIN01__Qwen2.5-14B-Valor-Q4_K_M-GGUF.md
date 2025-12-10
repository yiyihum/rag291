---
language: en
license: apache-2.0
library_name: transformers
tags:
- qwen
- lora
- question-generation
- text-generation
- valor
- assumption-challenging
- llama-cpp
- gguf-my-repo
base_model: TECHNOPRAVIN01/Qwen2.5-14B-Valor
---

# TECHNOPRAVIN01/Qwen2.5-14B-Valor-Q4_K_M-GGUF
This model was converted to GGUF format from [`TECHNOPRAVIN01/Qwen2.5-14B-Valor`](https://huggingface.co/TECHNOPRAVIN01/Qwen2.5-14B-Valor) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/TECHNOPRAVIN01/Qwen2.5-14B-Valor) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo TECHNOPRAVIN01/Qwen2.5-14B-Valor-Q4_K_M-GGUF --hf-file qwen2.5-14b-valor-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo TECHNOPRAVIN01/Qwen2.5-14B-Valor-Q4_K_M-GGUF --hf-file qwen2.5-14b-valor-q4_k_m.gguf -c 2048
```

Note: You can also use this checkpoint directly through the [usage steps](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage) listed in the Llama.cpp repo as well.

Step 1: Clone llama.cpp from GitHub.
```
git clone https://github.com/ggerganov/llama.cpp
```

Step 2: Move into the llama.cpp folder and build it with `LLAMA_CURL=1` flag along with other hardware-specific flags (for ex: LLAMA_CUDA=1 for Nvidia GPUs on Linux).
```
cd llama.cpp && LLAMA_CURL=1 make
```

Step 3: Run inference through the main binary.
```
./llama-cli --hf-repo TECHNOPRAVIN01/Qwen2.5-14B-Valor-Q4_K_M-GGUF --hf-file qwen2.5-14b-valor-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo TECHNOPRAVIN01/Qwen2.5-14B-Valor-Q4_K_M-GGUF --hf-file qwen2.5-14b-valor-q4_k_m.gguf -c 2048
```

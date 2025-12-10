---
license: apache-2.0
datasets:
- continuedev/instinct-data
base_model:
- Qwen/Qwen2.5-Coder-7B
pipeline_tag: text-generation
library_name: transformers
---

<img src="https://cdn-uploads.huggingface.co/production/uploads/686c5c546abedce0f7ac048a/B7PeaDQCDnlgT3Tmf7fsb.png" width=250>

# Instinct, the State-of-the-Art Open Next Edit Model

This repo contains the model weights for [Continue](https://continue.dev)'s state-of-the-art open Next Edit model, **Instinct**. Robustly fine-tuned from Qwen2.5-Coder-7B on our [dataset of real-world code edits](https://huggingface.co/datasets/continuedev/instinct-data), Instinct intelligently predicts your next move to keep you in flow. 

## Serving the model

**Ollama**: We've released a [Q4_K_M GGUF quantization of Instinct](https://huggingface.co/continuedev/instinct-GGUF) for efficient local inference. Try it with [Continue's Ollama integration](https://docs.continue.dev/guides/ollama-guide), or just run `ollama run nate/instinct`.

You can also serve the model using either of the below options, then [connect it with Continue](https://docs.continue.dev/guides/how-to-self-host-a-model).

**SGLang**: `python3 -m sglang.launch_server --model-path continuedev/instinct --load-format safetensors`
<br>**vLLM**: `vllm serve continuedev/instinct --served-model-name instinct --load-format safetensors`

## Learn more

For more information on the work behind Instinct, please refer to our [blog](https://blog.continue.dev/instinct/).
---
license: mit
library_name: transformers
---
# DeepSeek-V3-0324-GPTQ-4b-128g-experts
<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable html -->
<!-- markdownlint-disable no-duplicate-header -->

## Model Overview

This model was obtained by quantizing the weights of [deepseek-ai/DeepSeek-V3-0324](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324) to INT4 data type. This optimization reduces the number of bits per parameter from 8 to 4, reducing the disk size and GPU memory requirements by approximately 50%.

Only non-shared experts within transformer blocks are compressed. Weights are quantized using a symmetric per-group scheme, with group size 128. The GPTQ algorithm is applied for quantization.

Model checkpoint is saved in [compressed_tensors](https://github.com/neuralmagic/compressed-tensors) format.

| Models | Experts Quantized | Attention blocks quantized | Size (GB) |
| ------ |  --------- | --------- | --------- |
| [deepseek-ai/DeepSeek-V3-0324](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324) | ❌ | ❌  | 671 GB |
| [ISTA-DASLab/DeepSeek-V3-0324-GPTQ-4b-128g-experts](https://huggingface.co/DeepSeek-V3-0324-GPTQ-4b-128g-experts) | ✅  | ❌  | 346 GB |

## Contributors
Denis Kuznedelev (Yandex), Eldar Kurtić (Red Hat AI & ISTA), Jiale Chen (ISTA), Michael Goin (Red Hat AI), Elias Frantar (ISTA), Dan Alistarh (Red Hat AI & ISTA).
---
license_name: mit
library_name: mlx
tags:
- mlx
pipeline_tag: text-generation
base_model: inclusionAI/Ring-1T
---

# mlx-community/Ring-1T-mlx-DQ3_K_M

This model [mlx-community/Ring-1T-mlx-DQ3_K_M](https://huggingface.co/mlx-community/Ring-1T-mlx-DQ3_K_M) was
converted to MLX format from [inclusionAI/Ring-1T](https://huggingface.co/inclusionAI/Ring-1T)
using mlx-lm version **0.28.1**.

This is created for people using a single Apple Mac Studio M3 Ultra with 512 GB. The 4-bit version of Ring 1T does not fit. Using research results, we aim to get 4-bit performance from a slightly smaller and smarter quantization. It should also not be so large that it leaves no memory for a useful context window.

```bash
pip install mlx-lm

mlx_lm.generate --model mlx-community/Ring-1T-mlx-DQ3_K_M --temp 0.7 --max-tokens 4096 --prompt "Hallo"
```

---

## What is this DQ3_K_M?

In the Arxiv paper [Quantitative Analysis of Performance Drop in DeepSeek Model Quantization](https://arxiv.org/abs/2505.02390) the authors write,

> We further propose `DQ3_K_M`, a dynamic 3-bit quantization method that significantly outperforms traditional `Q3_K_M` variant on various benchmarks, which is also comparable with 4-bit quantization (`Q4_K_M`) approach in most tasks.

and

> dynamic 3-bit quantization method (`DQ3_K_M`) that outperforms the 3-bit quantization implementation in `llama.cpp` and achieves performance comparable to 4-bit quantization across multiple benchmarks.

The resulting multi-bitwidth quantization has been well tested and documented.

---

## How can you create your own DQ3_K_M quants?

In the `convert.py` file of mlx-lm on your system ( [you can see the original code here](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/convert.py) ), replace the code inside `def mixed_quant_predicate()` with something like

```python
        index = (
            int(path.split(".")[layer_location])
            if len(path.split(".")) > layer_location
            else 0
        )
        # Build a mixed quant similar to the "DQ3" of Arxiv paper https://arxiv.org/abs/2505.02390
        #    Quantitative Analysis of Performance Drop in DeepSeek Model Quantization
        q_bits = 8
        # For "switch experts"
        if "switch_mlp" in path:
           q_bits = 3
        if "switch_mlp.down_proj" in path:
           # Blocks up to 5 are higher quality
           if index < 5:
              q_bits = 5
           # Every 5th block is "medium" quality
           if (index % 5) == 0:
              q_bits = 4
        #print("path:", path, "index:", index, "q_bits:", q_bits)
        return {"group_size": group_size, "bits": q_bits}
```

Then create your DQ3_K_M quant with

```bash
mlx_lm.convert --hf-path inclusionAI/Ring-1T --mlx-path your-model-DQ3_K_M -q --quant-predicate mixed_3_4
```

---

Enjoy!

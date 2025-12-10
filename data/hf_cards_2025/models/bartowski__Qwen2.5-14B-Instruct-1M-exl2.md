---
quantized_by: bartowski
pipeline_tag: text-generation
base_model: Qwen/Qwen2.5-14B-Instruct-1M
base_model_relation: quantized
---

## Exllama v2 Quantizations of Qwen2.5-14B-Instruct-1M

Using <a href="https://github.com/turboderp/exllamav2/releases/tag/v0.2.7">turboderp's ExLlamaV2 v0.2.7</a> for quantization.

<b>The "main" branch only contains the measurement.json, download one of the other branches for the model (see below)</b>

Each branch contains an individual bits per weight, with the main one containing only the meaurement.json for further conversions.

Original model: https://huggingface.co/Qwen/Qwen2.5-14B-Instruct-1M

## Prompt format

```
<|im_start|>system
{system_prompt}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```

## Available sizes

| Branch | Bits | lm_head bits | VRAM (4k) | VRAM (16k) | Description |
| ----- | ---- | ------- | ------ | ------ | ------------ |
| [8_0](https://huggingface.co/bartowski/Qwen2.5-14B-Instruct-1M-exl2/tree/8_0) | 8.0  | 8.0 | 17.4 GB | 20.9 GB | Max quality that ExLlamaV2 can produce, **recommended**. |
| [6_5](https://huggingface.co/bartowski/Qwen2.5-14B-Instruct-1M-exl2/tree/6_5) | 6.5  | 8.0 | 14.6 GB | 17.5 GB | Near unquantized performance at vastly reduced size, **recommended**. |
| [5_0](https://huggingface.co/bartowski/Qwen2.5-14B-Instruct-1M-exl2/tree/5_0) | 5.0  | 6.0 | 11.6 GB | 14.4 GB | Slightly lower quality vs 6.5. |
| [4_25](https://huggingface.co/bartowski/Qwen2.5-14B-Instruct-1M-exl2/tree/4_25) | 4.25 | 6.0 | 10.1 GB | 13.0 GB | GPTQ equivalent bits per weight. |
| [3_5](https://huggingface.co/bartowski/Qwen2.5-14B-Instruct-1M-exl2/tree/3_5) | 3.5  | 6.0 | 8.7 GB | 11.5 GB | Lower quality, not recommended. |
| [3_0](https://huggingface.co/bartowski/Qwen2.5-14B-Instruct-1M-exl2/tree/3_0) | 3.0  | 6.0 | 7.8 GB | 10.5 GB | Low quality, not recommended. |

## Download instructions

With git:

```shell
git clone --single-branch --branch 6_5 https://huggingface.co/bartowski/Qwen2.5-14B-Instruct-1M-exl2 Qwen2.5-14B-Instruct-1M-exl2-6_5
```

With huggingface hub (credit to TheBloke for instructions):

```shell
pip3 install huggingface-hub
```

To download a specific branch, use the `--revision` parameter. For example, to download the 6.5 bpw branch:

Linux:

```shell
huggingface-cli download bartowski/Qwen2.5-14B-Instruct-1M-exl2 --revision 6_5 --local-dir Qwen2.5-14B-Instruct-1M-exl2-6_5
```

Windows (which apparently doesn't like _ in folders sometimes?):

```shell
huggingface-cli download bartowski/Qwen2.5-14B-Instruct-1M-exl2 --revision 6_5 --local-dir Qwen2.5-14B-Instruct-1M-exl2-6.5
```

Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski

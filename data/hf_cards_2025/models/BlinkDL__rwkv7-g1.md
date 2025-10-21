---
language:
- en
- zh
- fr
- es
- de
- pt
- ru
- it
- ja
- ko
- vi
- ar
tags:
- pytorch
- text-generation
- causal-lm
- rwkv
license: apache-2.0
datasets:
- HuggingFaceFW/fineweb-edu
- mlfoundations/dclm-baseline-1.0
- cerebras/SlimPajama-627B
- EleutherAI/pile
- bigcode/starcoderdata
- oscar-corpus/OSCAR-2301
---

# RWKV7-G1 "GooseOne" pure RNN reasoning model

**These are BASE models** (pretrained with web/code/synthetic + instruction/chat/reasoning data), suitable for post-training and fine-tuning (check https://huggingface.co/spaces/Jellyfish042/UncheatableEval to see their performance at language modeling).

More info & Gradio demo: https://rwkv.com/

For developers: https://github.com/BlinkDL/RWKV-LM

RWKV-7 pth => GGUF script: https://github.com/MollySophia/rwkv-mobile/blob/master/converter/convert_rwkv_pth_to_gguf.py

Use rwkv pip package 0.8.29+ for RWKV-7 inference: https://pypi.org/project/rwkv/

Efficient inference project: https://github.com/BlinkDL/Albatross

RWKV APP: https://github.com/RWKV-APP/RWKV_APP (local inference on Android/iOS)

Please use **latest G1a models** if available (better at everything).

```
Gxx = Data Version

G0x = less than 1 epoch, as training 1 epoch for a large model is expensive :(
G0 G0a G0b ... = adding more (newer and better) data, so G0a has better quality (but less) data than G1

G1x = more than 1 epoch
G1 G1a G1b ... = adding more (newer and better) data, note G1a has better quality (and more) data than G0a
```

Decoding (note: this is for RWKV pip pkg, which apply temp after topp):

```
Math: temp 0.3, topp 0.3, alpha_presence 0, alpha_frequency 0, alpha_decay 0.996

Chat: temp 1, topp 0.3, alpha_presence 0.5, alpha_frequency 0.5, alpha_decay 0.996

Creative (great for fiction etc.): temp 0.6, topp 0.6 ~ 0.8, alpha_presence 1 ~ 2, alpha_frequency 0.2, alpha_decay 0.99
```

**There should not be any space at the end of your input (so strip it) or you will upset the tokenizer and see non-English reponse.**

Chat prompt (note: better replace all \n\n in USER_PROMPT to \n as i am using \n\n as "chat round separator" in pretrain data):
```
System: YOU_CAN_USE_SYSTEM_IF_NEEDED

User: PREVIOUS_STUFF

Assistant: PREVIOUS_STUFF

User: USER_PROMPT

Assistant:
```

Think prompt:
```
User: USER_PROMPT

Assistant: <think
```
---
Think prompt, alternative style output, **valid for 20250922 and newer** models. Note there is a space before the "think" after USER_PROMPT:
```
User: USER_PROMPT think

Assistant: <think
```
Shorter think (think a bit), same style:
```
User: USER_PROMPT think a bit

Assistant: <think
```
Longer think (think a lot), same style:
```
User: USER_PROMPT think a lot

Assistant: <think
```
---
Fake think prompt:
```
User: USER_PROMPT

Assistant: <think>
</think
```

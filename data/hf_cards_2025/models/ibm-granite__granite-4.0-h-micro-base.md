---
license: apache-2.0
library_name: transformers
tags:
- language
- granite-4.0
---

# Granite-4.0-H-Micro-Base

**Model Summary:** 
Granite-4.0-H-Micro-Base is a decoder-only, long-context language model designed for a wide range of text-to-text generation tasks. It also supports Fill-in-the-Middle (FIM) code completion through the use of specialized prefix and suffix tokens. The model is trained from scratch on approximately 18 trillion tokens following a four-stage training strategy: 10 trillion tokens in the first stage, 5 trillion in the second, 2 trillion in the third, and 0.5 trillion in the final stage. 

- **Developers:** Granite Team, IBM
- **HF Collection:** [Granite 4.0 Language Models HF Collection](https://huggingface.co/collections/ibm-granite/granite-40-language-models-6811a18b820ef362d9e5a82c)
- **GitHub Repository:** [ibm-granite/granite-4.0-language-models](https://github.com/ibm-granite/granite-4.0-language-models)
- **Website**: [Granite Docs](https://www.ibm.com/granite/docs/) 
- **Release Date**: October 2nd, 2025
- **License:** [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

**Supported Languages:** 
English, German, Spanish, French, Japanese, Portuguese, Arabic, Czech, Italian, Korean, Dutch, and Chinese. Users may finetune Granite 4.0 models for languages beyond these languages.

**Intended Use:**
Prominent use cases of LLMs in text-to-text generation include summarization, text classification, extraction, question-answering, code-completion (including FIM), and long-context generation tasks. All Granite Base models are able to handle these tasks as they were trained on a large amount of data from various domains. Moreover, they can serve as baseline to create specialized models for specific application scenarios.

**Generation:** 
This is a simple example of how to use Granite-4.0-H-Micro-Base model.

Install the following libraries:

```shell
pip install torch torchvision torchaudio
pip install accelerate
pip install transformers
```
Then, copy the code snippet below to run the example.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda"

model_path = "ibm-granite/granite-4.0-h-micro-base"

tokenizer = AutoTokenizer.from_pretrained(model_path)
# drop device_map if running on CPU
model = AutoModelForCausalLM.from_pretrained(model_path, device_map=device)
model.eval()
# change input text as desired
input_text = "The capital of France is"
# tokenize the text
input_tokens = tokenizer(input_text, return_tensors="pt").to(device)
# generate output tokens
output = model.generate(**input_tokens, max_length=10)
# decode output tokens into text
output = tokenizer.batch_decode(output)
# print output
print(output[0])
```

Expected output:
```shell
The capital of France is Paris.
```

**Evaluation Results:** 

<table>
<!--   <caption><b> All Results</b></caption> -->
<thead>
  <tr>
    <th style="text-align:left; background-color: #001d6c; color: white;">Benchmarks</th>
    <th style="text-align:left; background-color: #001d6c; color: white;">Metric</th>
    <th style="text-align:center; background-color: #001d6c; color: white;">Micro Dense</th>
    <th style="text-align:center; background-color: #001d6c; color: white;">H Micro Dense</th>
    <th style="text-align:center; background-color: #001d6c; color: white;">H Tiny MoE</th>
    <th style="text-align:center; background-color: #001d6c; color: white;">H Small MoE</th>
  </tr>
</thead>
  <tbody>
<tr>
  <td colspan="6" style="text-align:center; background-color:  #FFFFFF; color: #2D2D2D; font-style:italic;">
    General Tasks
  </td>
</tr>
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">MMLU</td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">5-shot</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">66.47</td>
    <td style="text-align:right; background-color: #DAE8FF; color: #2D2D2D;">67.43</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">68.90</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">75.85</td>
</tr>
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">MMLU-Pro</td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">5-shot,CoT</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">37.16</td>
    <td style="text-align:right; background-color: #DAE8FF; color: #2D2D2D;">34.03</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">35.47</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">48.94</td>
</tr>
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">BBH</td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">3-shot, CoT</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">63.84</td>
    <td style="text-align:right; background-color: #DAE8FF; color: #2D2D2D;">57.65</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">59.67</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">75.84</td>
</tr>
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">AGI EVAL</td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">3-shot</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">54.32</td>
    <td style="text-align:right; background-color: #DAE8FF; color: #2D2D2D;">54.59</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">53.69</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">62.05</td>
</tr>
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">DROP</td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">5-shot</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">66.04</td>
    <td style="text-align:right; background-color: #DAE8FF; color: #2D2D2D;">67.44</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">64.92</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">74.69</td>
</tr>
<tr>
  <td colspan="6" style="text-align:center; background-color:  #FFFFFF; color: #2D2D2D; font-style:italic;">
    Math Tasks
  </td>
</tr>      
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">GSM8K</td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">8-shot</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">72.93</td>
    <td style="text-align:right; background-color: #DAE8FF; color: #2D2D2D;">63.76</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">72.55</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">82.11</td>
</tr>
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">Minerva Math</td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">4-shot</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">38</td>
    <td style="text-align:right; background-color: #DAE8FF; color: #2D2D2D;">39.7</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">40.34</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">46.28</td>
</tr>
<tr>
  <td colspan="6" style="text-align:center; background-color:  #FFFFFF; color: #2D2D2D; font-style:italic;">
    Code Tasks
  </td>
</tr> 
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">HumanEval </td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">pass@1 [StarCoder Prompt]</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">76.19</td>
    <td style="text-align:right; background-color: #DAE8FF; color: #2D2D2D;">73.72</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">77.59</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">83.66</td>
</tr>
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">HumanEval</td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">pass@1</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">59.76</td>
    <td style="text-align:right; background-color: #DAE8FF; color: #2D2D2D;">70.73</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">71.34</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">76.22</td>
</tr>
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">HumanEval+</td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">pass@1</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">54.27</td>
    <td style="text-align:right; background-color: #DAE8FF; color: #2D2D2D;">67.07</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">64.02</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">69.51</td>
</tr>
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">MBPP</td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">pass@1</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">81.48</td>
    <td style="text-align:right; background-color: #DAE8FF; color: #2D2D2D;">74.87</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">81.48</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">83.07</td>
</tr>
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">MBPP+</td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">pass@1</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">68.25</td>
    <td style="text-align:right; background-color: #DAE8FF; color: #2D2D2D;">63.23</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">68.78</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">70.37</td>
</tr>
<tr>
  <td colspan="6" style="text-align:center; background-color:  #FFFFFF; color: #2D2D2D; font-style:italic;">
    Multilingual Tasks
  </td>
</tr> 
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">MMMLU</td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">5-shot</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">56.59</td>
    <td style="text-align:right; background-color: #DAE8FF; color: #2D2D2D;">58.5</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">62.77</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">71.18</td>
</tr> 
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">INCLUDE</td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">5-shot</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">51.77</td>
    <td style="text-align:right; background-color: #DAE8FF; color: #2D2D2D;">52.16</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">53.78</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">66.04</td>
</tr>
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">MGSM</td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">8-shot</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">58.48</td>
    <td style="text-align:right; background-color: #DAE8FF; color: #2D2D2D;">47.04</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">54.64</td>
    <td style="text-align:right; background-color: #FFFFFF; color: #2D2D2D;">65.2</td>
</tr>
</tbody></table>


<table>
  <caption><b>Multilingual Benchmarks and thr included languages:</b></caption>
<thead>
  <tr>
    <th style="text-align:left; background-color: #001d6c; color: white;">Benchmarks</th>
    <th style="text-align:left; background-color: #001d6c; color: white;"># Langs</th>
    <th style="text-align:center; background-color: #001d6c; color: white;">Languages</th>
  </tr>
</thead>
<tbody>
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">MMMLU</td>
    <td style="text-align:center; background-color: #FFFFFF; color: #2D2D2D;">11</td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">ar, de, en, es, fr, ja, ko, pt, zh, bn, hi</td>
</tr>
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">INCLUDE</td>
    <td style="text-align:center; background-color: #FFFFFF; color: #2D2D2D;">14</td>
<!--     <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">hindi, bengali, tamil, telugu, arabic, german, spanish, french, italian, japanese, korean, dutch, portuguese, chinese</td> -->
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">hi, bn, ta, te, ar, de, es, fr, it, ja, ko, nl, pt, zh</td>
    
</tr>
<tr>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">MGSM</td>
    <td style="text-align:center; background-color: #FFFFFF; color: #2D2D2D;">5</td>
    <td style="text-align:left; background-color: #FFFFFF; color: #2D2D2D;">en, es, fr, ja, zh</td>
</tr>
</tbody>
</table>

**Model Architecture:** 
Granite-4.0-H-Micro-Base is based on a decoder-only dense transformer architecture. Core components of this architecture are: GQA, Mamba2, MLP with SwiGLU, RMSNorm, and shared input/output embeddings.

<table>
<thead>
  <tr>
    <th style="text-align:left; background-color: #001d6c; color: white;">Model</th>
    <th style="text-align:center; background-color: #001d6c; color: white;">Micro Dense</th>
    <th style="text-align:center; background-color: #001d6c; color: white;">H Micro Dense</th>
    <th style="text-align:center; background-color: #001d6c; color: white;">H Tiny MoE</th>
    <th style="text-align:center; background-color: #001d6c; color: white;">H Small MoE</th>
  </tr></thead>
<tbody>
  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">Embedding size</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">2560</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">2048</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">1536</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">4096</td>
  </tr>
  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">Number of layers</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">40 attention</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">4 attention / 36 Mamba2</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">4 attention / 36 Mamba2</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">4 attention / 36 Mamba2</td>
  </tr>
  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">Attention head size</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">64</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">64</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">128</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">128</td>
  </tr>
  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">Number of attention heads</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">40</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">32</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">12</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">32</td>
  </tr>
  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">Number of KV heads</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">8</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">8</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">4</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">8</td>
  </tr>
  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">Mamba2 state size</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">-</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">128</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">128</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">128</td>
  </tr>
  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">Number of Mamba2 heads</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">-</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">64</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">48</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">128</td>
  </tr>

  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">MLP / Shared expert hidden size</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">8192</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">8192</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">1024</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">1536</td>
  </tr>
    

  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">Num. Experts</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">-</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">-</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">64</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">72</td>
  </tr>
  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">Num. active Experts</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">-</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">-</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">6</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">10</td>
  </tr>
  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">Expert hidden size</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">-</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">-</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">512</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">768</td>
  </tr>

  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">MLP activation</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">SwiGLU</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">SwiGLU</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">SwiGLU</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">SwiGLU</td>
  </tr>

  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">Sequence length</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">128K</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">128K</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">128K</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">128K</td>
  </tr>
  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">Position embedding</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">RoPE</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">NoPE</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">NoPE</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">NoPE</td>
  </tr>
  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;"># Parameters</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">3B</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">3B</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">7B</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">32B</td>
  </tr>
  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;"># Active parameters</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">3B</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">3B</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">1B</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">9B</td>
  </tr>
</tbody></table>


**Training Data:** This model is trained on a mix of open source and proprietary data following a four-stage training strategy. 

<table>
<thead>
  <tr>
    <th style="text-align:left; background-color: #001d6c; color: white;">Stage</th>
    <th style="text-align:left; background-color: #001d6c; color: white;">Characteristics</th>
    <th style="text-align:center; background-color: #001d6c; color: white;">Micro Dense</th>
    <th style="text-align:center; background-color: #001d6c; color: white;">H Micro Dense</th>
    <th style="text-align:center; background-color: #001d6c; color: white;">H Tiny MoE</th>
    <th style="text-align:center; background-color: #001d6c; color: white;">H Small MoE</th>
  </tr></thead>
<tbody>
  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">I</td>
      <td style="text-align:left; background-color: #FFFFFF; color: black;">General mixture of training data, warmup, and  power scheduler for learning rate.</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">10</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">10</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">15</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">15</td>
  </tr>
  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">II</td>
      <td style="text-align:left; background-color: #FFFFFF; color: black;">General mixture of training data with higher percentages of code and math with power scheduler for learning rate.</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">2</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">5</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">5</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">5</td>
  </tr>
  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">III</td>
      <td style="text-align:left; background-color: #FFFFFF; color: black;">High quality training data, exponential decay of learning rate.</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">2</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">2</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">2</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">2</td>
  </tr>
  <tr>
    <td style="text-align:left; background-color: #FFFFFF; color: black;">IV</td>
      <td style="text-align:left; background-color: #FFFFFF; color: black;">High quality training data, linear decay to zero for learning rate.</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">0.5</td>
    <td style="text-align:center; background-color: #DAE8FF; color: black;">0.5</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">0.5</td>
    <td style="text-align:center; background-color: #FFFFFF; color: black;">0.5</td>
  </tr>
</tbody></table>

**Infrastructure:**
We trained the Granite 4.0 Language Models utilizing an NVIDIA GB200 NVL72 cluster hosted in CoreWeave. Intra-rack communication occurs via the 72-GPU NVLink domain, and a non-blocking, full Fat-Tree NDR 400 Gb/s InfiniBand network provides inter-rack communication. This cluster provides a scalable and efficient infrastructure for training our models over thousands of GPUs.

**Ethical Considerations and Limitations:** 
The use of Large Language Models involves risks and ethical considerations people must be aware of, including but not limited to: bias and fairness, misinformation, and autonomous decision-making. Granite-4.0-H-Micro-Base model is not the exception in this regard. Even though this model is suited for multiple generative AI tasks, it has not undergone any safety alignment, there it may produce problematic outputs. Additionally, it remains uncertain whether smaller models might exhibit increased susceptibility to hallucination in generation scenarios by copying text verbatim from the training dataset due to their reduced sizes and memorization capacities. This aspect is currently an active area of research, and we anticipate more rigorous exploration, comprehension, and mitigations in this domain. Regarding ethics, a latent risk associated with all Large Language Models is their malicious utilization. We urge the community to use Granite-4.0-H-Micro-Base model with ethical intentions and in a responsible way. 

**Resources**
- ⭐️ Learn about the latest updates with Granite: https://www.ibm.com/granite
- 📄 Get started with tutorials, best practices, and prompt engineering advice: https://www.ibm.com/granite/docs/
- 💡 Learn about the latest Granite learning resources: https://github.com/ibm-granite-community/
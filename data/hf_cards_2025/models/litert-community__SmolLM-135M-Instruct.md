---
license: apache-2.0
base_model: HuggingFaceTB/SmolLM-135M-Instruct
pipeline_tag: text-generation
library_name: litert-lm
tags:
- chat
---

# litert-community/SmolLM-135M-Instruct

This model provides a few variants of
[HuggingFaceTB/SmolLM-135M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM-135M-Instruct) that are ready for
deployment on Android using the
[LiteRT (fka TFLite) stack](https://ai.google.dev/edge/litert) and
[MediaPipe LLM Inference API](https://ai.google.dev/edge/mediapipe/solutions/genai/llm_inference).

## Use the models

### Colab

*Disclaimer: The target deployment surface for the LiteRT models is
Android/iOS/Web and the stack has been optimized for performance on these
targets. Trying out the system in Colab is an easier way to familiarize yourself
with the LiteRT stack, with the caveat that the performance (memory and latency)
on Colab could be much worse than on a local device.*

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#fileId=https://huggingface.co/litert-community/SmolLM-135M-Instruct/blob/main/notebook.ipynb)

### Android

*   Download and install
    [the apk](https://github.com/google-ai-edge/mediapipe-samples/releases/latest/download/llm_inference-debug.apk).
*   Follow the instructions in the app.

To build the demo app from source, please follow the
[instructions](https://github.com/google-ai-edge/mediapipe-samples/blob/main/examples/llm_inference/android/README.md)
from the GitHub repository.

## Performance

### Android

Note that all benchmark stats are from a Samsung S24 Ultra with 
1280 KV cache size with multiple prefill signatures enabled.

<table border="1">
  <tr>
   <th></th>
   <th>Backend</th>
   <th>Context length</th>
   <th>Prefill (tokens/sec)</th>
   <th>Decode (tokens/sec)</th>
   <th>Time-to-first-token (sec)</th>
   <th>Memory (RSS in MB)</th>
   <th>Model size (MB)</th>
  </tr>
  <tr>
<td>fp32 (baseline)</td>
<td>cpu</td>
<td><p style="text-align: right">1280</p></td>
<td><p style="text-align: right">498.05 tk/s</p></td>
<td><p style="text-align: right">47.96 tk/s</p></td>
<td><p style="text-align: right">0.78 s</p></td>
<td><p style="text-align: right">931 MB</p></td>
<td><p style="text-align: right">527 MB</p></td>
</tr>
<tr>
<td>dynamic_int8</td>
<td>cpu</td>
<td><p style="text-align: right">1280</p></td>
<td><p style="text-align: right">1084.75 tk/s</p></td>
<td><p style="text-align: right">43.50 tk/s</p></td>
<td><p style="text-align: right">0.46 s</p></td>
<td><p style="text-align: right">579 MB</p></td>
<td><p style="text-align: right">159 MB</p></td>
</tr>

</table>

*   Model Size: measured by the size of the .tflite flatbuffer (serialization
    format for LiteRT models)
*   Memory: indicator of peak RAM usage
*   The inference on CPU is accelerated via the LiteRT
    [XNNPACK](https://github.com/google/XNNPACK) delegate with 4 threads
*   Benchmark is run with cache enabled and initialized. During the first run,
    the time to first token may differ.
*   dynamic_int4: quantized model with int4 weights and float activations.
*   dynamic_int8: quantized model with int8 weights and float activations.

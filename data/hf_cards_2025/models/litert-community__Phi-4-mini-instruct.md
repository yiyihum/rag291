---
license: mit
base_model: microsoft/Phi-4-mini-instruct
pipeline_tag: text-generation
library_name: litert-lm
tags:
- chat
---

# litert-community/Phi-4-mini-instruct

This model provides a few variants of
[microsoft/Phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct) that are ready for
deployment on Android using the
[LiteRT (fka TFLite) stack](https://ai.google.dev/edge/litert),
[MediaPipe LLM Inference API](https://ai.google.dev/edge/mediapipe/solutions/genai/llm_inference) and
[LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM).

## Use the models

### Colab

*Disclaimer: The target deployment surface for the LiteRT models is
Android/iOS/Web and the stack has been optimized for performance on these
targets. Trying out the system in Colab is an easier way to familiarize yourself
with the LiteRT stack, with the caveat that the performance (memory and latency)
on Colab could be much worse than on a local device.*

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#fileId=https://huggingface.co/litert-community/Phi-4-mini-instruct/blob/main/notebook.ipynb)

### Android

#### Edge Gallery App
*   Download or build the [app](https://github.com/google-ai-edge/gallery?tab=readme-ov-file#-get-started-in-minutes) from GitHub.

*   Install the [app](https://play.google.com/store/apps/details?id=com.google.ai.edge.gallery&pli=1) from Google Play.

*   Follow the instructions in the app.

#### LLM Inference API

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
   <th>Backend</th>
   <th>Quantization scheme</th>
   <th>Context length</th>
   <th>Prefill (tokens/sec)</th>
   <th>Decode (tokens/sec)</th>
   <th>Time-to-first-token (sec)</th>
   <th>Model size (MB)</th>
   <th>Peak RSS Memory (MB)</th>
   <th>GPU Memory (MB)</th>
  </tr>
  <tr>
<td><p style="text-align: right">CPU</td>
<td><p style="text-align: right">dynamic_int8</td>
<td><p style="text-align: right">4096</td>
<td><p style="text-align: right">66.53 tk/s</p></td>
<td><p style="text-align: right">7.28 tk/s</p></td>
<td><p style="text-align: right">15.90 s</p></td>
<td><p style="text-align: right">3906 MB</p></td>
<td><p style="text-align: right">5308 MB</p></td>
<td><p style="text-align: right">N/A</p></td>
</tr>
<tr>
<td><p style="text-align: right">GPU</td>
<td><p style="text-align: right">dynamic_int8</td>
<td><p style="text-align: right">4096</td>
<td><p style="text-align: right">314.01 tk/s</p></td>
<td><p style="text-align: right">10.39 tk/s</p></td>
<td><p style="text-align: right">10.32 s</p></td>
<td><p style="text-align: right">3906 MB</p></td>
<td><p style="text-align: right">4107 MB</p></td>
<td><p style="text-align: right">4608 MB</p></td>
</tr>

</table>

*   Model Size: measured by the size of the .tflite flatbuffer (serialization
    format for LiteRT models)
*   Memory: indicator of peak RAM usage
*   The inference on CPU is accelerated via the LiteRT
    [XNNPACK](https://github.com/google/XNNPACK) delegate with 4 threads
*   Benchmark is done assuming XNNPACK cache is enabled
*   Benchmark is run with cache enabled and initialized. During the first run, the time to first token may differ.
*   dynamic_int8: quantized model with int8 weights and float activations.

---
license: apache-2.0
base_model: TinyLlama/TinyLlama-1.1B-Chat-v1.0
pipeline_tag: text-generation
library_name: litert-lm
tags:
- chat
---

# litert-community/TinyLlama-1.1B-Chat-v1.0

This model provides a few variants of
[TinyLlama/TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) that are ready for
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

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#fileId=https://huggingface.co/litert-community/TinyLlama-1.1B-Chat-v1.0/blob/main/notebook.ipynb)

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
   <th>Prefill (tokens/sec)</th>
   <th>Decode (tokens/sec)</th>
   <th>Time-to-first-token (sec)</th>
   <th>Memory (RSS in MB)</th>
   <th>Model size (MB)</th>
  </tr>
  <tr>
<td>fp32 (baseline)</td>
<td>cpu</td>
<td><p style="text-align: right">51.14 tk/s</p></td>
<td><p style="text-align: right">9.23 tk/s</p></td>
<td><p style="text-align: right">9.25 s</p></td>
<td><p style="text-align: right">6,155 MB</p></td>
<td><p style="text-align: right">4,208 MB</p></td>
</tr>
<tr>
<td>dynamic_int8</td>
<td>cpu</td>
<td><p style="text-align: right">156.10 tk/s</p></td>
<td><p style="text-align: right">26.34 tk/s</p></td>
<td><p style="text-align: right">3.80 s</p></td>
<td><p style="text-align: right">2,359 MB</p></td>
<td><p style="text-align: right">1,095 MB</p></td>
</tr>

</table>

*   Model Size: measured by the size of the .tflite flatbuffer (serialization
    format for LiteRT models)
*   Memory: indicator of peak RAM usage
*   The inference on CPU is accelerated via the LiteRT
    [XNNPACK](https://github.com/google/XNNPACK) delegate with 4 threads
*   Benchmark is done assuming XNNPACK cache is enabled
*   dynamic_int8: quantized model with int8 weights and float activations.

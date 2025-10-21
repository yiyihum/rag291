---
license: apache-2.0
library_name: transformers
tags:
- bamba
datasets:
- allenai/dolma
- allenai/olmo-mix-1124
- allenai/dolmino-mix-1124
- HuggingFaceTB/smollm-corpus
---

## Model Details
<p align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/64b6c638ac6d20bae0b93219/GOzs8o4G1apceun92ZC4d.png" alt="Bamba" width="400" height="400">
</p>

# Model Card for Bamba 9B v2
We introduce Bamba-9B-v2, a decoder-only language model based on the [Mamba-2](https://github.com/state-spaces/mamba) architecture and is designed to handle a wide range of text generation tasks. Bamba v2 is trained for an additional 1T tokens that significantly improves on [Bamba v1](https://huggingface.co/ibm-ai-platform/Bamba-9B-v1). The L1 and L2 leaderboard scores outperform Llama 3.1 8B, which was trained with nearly 5x the amount of data.

| Model | Params     | # Layers | Hidden Dim. | Attention Heads | GQA  | KV Heads | Context Length | Tied Embeddings |
| ----- | ---------- | -------- | ----------- | --------------- | ---- | -------- | -------------- | --------------- |
| Bamba | 9B (9.78B) | 32       | 4096        | 32              | Yes  | 8        | 4096           | False           |


The current release includes the following models:
| **Stage**            | **Bamba 9B**                                                               | **Quantized**                                                           | **Note**                                                          |
|----------------------|----------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------|
| **Base Model**       | [ibm-fms/Bamba-9B-v2](https://huggingface.co/ibm-ai-platform/Bamba-9B-v2)  | coming soon                                                             | Stage 2 pretraining + Annealing                                            |
| **Base Model**       | [ibm-fms/Bamba-9B-v1](https://huggingface.co/ibm-ai-platform/Bamba-9B-v1)  | [ibm-fms/Bamba-9B-fp8](https://huggingface.co/ibm-fms/Bamba-9B-fp8)     | Stage 2 pretraining                                               |
| **Base Model**       | [ibm-fms/Bamba-9B-2T](https://huggingface.co/ibm-fms/Bamba-9B-2T)          | [ibm-fms/Bamba-9B-fp8](https://huggingface.co/ibm-fms/Bamba-9B-fp8)     | Stage 1 pretraining                                               |
| **Base Model**       | [ibm-fms/Bamba-9B-1.8T](https://huggingface.co/ibm-fms/Bamba-9B-1.8T)      | [ibm-fms/Bamba-9B-fp8](https://huggingface.co/ibm-fms/Bamba-9B-fp8)     | Intermediate checkpoints during Stage 1, more to come             |
| **SFT**              | coming soon                                                                | coming soon                                                             | to be released in the next drop                                   | 
| **DPO**              | coming soon                                                                | coming soon                                                             | to be released in the next drop                                   |

Original checkpoints (in dcp format) were also uploaded to public bucket:
```
bucket: bamba-public
endpoint-url: https://s3.us-east.cloud-object-storage.appdomain.cloud
```
example command to list original Bamba distributed checkpoints:
```bash
aws --endpoint-url https://s3.us-east.cloud-object-storage.appdomain.cloud s3 ls s3://bamba-public/checkpoints/pretraining/phase_two/3_1t/step_500/
```

## Installation

Besides [PyTorch](https://pytorch.org/), you would need a few [extra dependencies](https://github.com/state-spaces/mamba?tab=readme-ov-file#installation) for
Mamba models.

We found some of these dependencies picky on PyTorch versions when doing pip install, so 
the best way is to build from source for all Mamba dependencies if you hit dependency 
issue with your env:
```bash
git clone https://github.com/Dao-AILab/causal-conv1d.git
cd causal-conv1d && pip install . && cd ..
git clone https://github.com/state-spaces/mamba.git
cd mamba && pip install . && cd ..
git clone https://github.com/Dao-AILab/flash-attention.git
cd flash-attention && pip install . && cd ..
```

For users using our HF versions of the model, you would need to install the latest transformers which includes our newly merged implementation for our Bamba models:
```bash
pip install git+https://github.com/huggingface/transformers.git
```

## Inference
You can utilize our newly contributed HF integration to run inference on our Bamba models:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("ibm-ai-platform/Bamba-9B-v2")
tokenizer = AutoTokenizer.from_pretrained("ibm-ai-platform/Bamba-9B-v2")

message = ["Mamba is a snake with following properties  "]
inputs = tokenizer(message, return_tensors='pt', return_token_type_ids=False)
response = model.generate(**inputs, max_new_tokens=64)
print(tokenizer.batch_decode(response, skip_special_tokens=True)[0])

```


## Training

We trained our Bamba model with FSDP using our training repo [here](https://github.com/foundation-model-stack/fms-fsdp).
Note that this training effort was started before FSDP2 and also long before we contributed
`Mamba2-Hybrid` to HF, so we were doing FSDP1 training with [official Mamba implementation](https://github.com/state-spaces/mamba).
For users trying to reproduce the training you now have much more options with our newly
contributed [HF-version of Mamba2-Hybrid](https://github.com/huggingface/transformers/tree/main/src/transformers/models/bamba).


## Benchmark scores

### Base pretrained models

<table>
 <tr>
<td><strong>Category</strong>
</td>
<td><strong>Benchmark</strong>
</td>
<td><strong>Bamba 9B (3.1T)</strong>
</td>
</tr>
<tr>
<td rowspan="8" >General
</td>
<td>MMLU (5-shot)
</td>
<td>67.92
</td>
</tr>
<tr>
<td>ARC-C (25-shot)
</td>
<td>63.57
</td>
</tr>
<tr>
<td>GSM8K (5-shot)
</td>
<td>41.70
</td>
</tr>
<tr>
<td>Hellaswag (10-shot)
</td>
<td>83.85
</td>
</tr>
<tr>
<td>OpenbookQA (5-shot)
</td>
<td>51.0
</td>
</tr>
<tr>
<td>Piqa (5-shot)
</td>
<td>83.62
</td>
</tr>
<tr>
<td>TruthfulQA (0-shot)
</td>
<td>50.86
</td>
</tr>
<tr>
<td>Winogrande (5-shot)
</td>
<td>79.48
</td>
</tr>
<tr>
<td rowspan="6" >HF OpenLLM- V2*
</td>
<td>MMLU-PRO (5-shot)
</td>
<td>25.41
</td>
</tr>
<tr>
<td>BBH (3-shot)
</td>
<td>24.78
</td>
</tr>
<tr>
<td>GPQA (0-shot)
</td>
<td>5.93
</td>
</tr>
<tr>
<td>IFEval (0-shot)
</td>
<td>19.0
</td>
</tr>
<tr>
<td>MATH Lvl 5 (4-shot)
</td>
<td>6.42
</td>
</tr>
<tr>
<td>MuSR (0-shot)
</td>
<td>9.28
</td>
</tr>
</table>

*For the v2 leaderboard results, we perform [normalization](https://huggingface.co/docs/leaderboards/open_llm_leaderboard/normalization) and report the normalized results.
Further details on our evaluation and normalization detailes along with run and analysis scripts can be found [here](https://github.com/foundation-model-stack/bamba/blob/main/evaluation/README.md).



## Fine-tuning

This [example](https://github.com/foundation-model-stack/bamba/blob/main/tuning/Fine-tuning.md) shows how to fine tune the bamba model for a specific task using [SFT Trainer](https://huggingface.co/docs/trl/en/sft_trainer#supervised-fine-tuning-trainer).

                           
## Quantization
We can create a (FP8) quantized model using [`fms-model-optimizer`](https://github.com/foundation-model-stack/fms-model-optimizer/), which will make the storage and inference even more efficient.
```python
python -m fms_mo.run_quant \
    --model_name_or_path <"path_to_original_model"> \
    --quant_method fp8 \
    --torch_dtype bfloat16 \
    --output_dir <"path_to_save_new_model">
```
Model size comparison before and after FP8:
|                     |                 original |                                                    quantized |
| :-----------------: | -----------------------: | -----------------------------------------------------------: |
|   memory (total)    |                 39.12 GB |                                                     10.83 GB |
| memory (break-down) | `torch.float32` 39.12 GB | `torch.bfloat16` 2.10 GB<br>`torch.float8_e4m3fn`    8.73 GB |

More details about `fms-model-optimizer` can be found [here](https://github.com/foundation-model-stack/fms-model-optimizer/tree/main/examples/FP8_QUANT#quickstart).


## Llama.cpp
There is preliminary work to enable running Bamba architecture models using [llama.cpp](https://github.com/ggerganov/llama.cpp). This is work-in-progress, so should only be used as a guide for the adventurous!

### Known Limitations

* Currently, inference is only supported on CPUs
* Models quantized with `llama-quantize` exhibit bad performance

### Setup
To enable Bamba support, you'll need to build from source using [Gabe's fork](https://github.com/gabe-l-hart/llama.cpp/tree/BambaArchitecture).

```sh
git clone --branch BambaArchitecture git@github.com:gabe-l-hart/llama.cpp.git
cd llama.cpp
mkdir build
cd build
# NOTE: To build with debug symbols and extra logging, use CMAKE_BUILD_TYPE=Debug
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j
```

### Conversion to GGUF
You can use a pre-converted GGUF file from Huggingface (e.g. [bamba-9b.gguf](https://huggingface.co/ibm-fms/Bamba-9B/blob/main/bamba-9b.gguf)). If one doesn't exist, you can use the [convert_hf_to_gguf.py](https://github.com/gabe-l-hart/llama.cpp/blob/BambaArchitecture/convert_hf_to_gguf.py) script from Gabe's fork to perform the conversion manually.

```sh
# Install the python dependencies
cd /path/to/llama.cpp
pip install -r requirements/requirements-convert_hf_to_gguf.txt

# Perform the conversion
./convert_hf_to_gguf.py /path/to/bamba-model --outfile /path/to/bamba-model/bamba-model.gguf
```

### Run with llama-cli

```sh
# Run the model with no layers on the GPU (CPU-only)
cd /path/to/llama.cpp
./bin/llama-cli  -ngl 0 -m /path/to/bamba-model/bamba-model.gguf -p "Tell me a story about a developer and their dog"
```

### Quantization with llama-quantize
You can (optionally) quantize the GGUF model using `llama.cpp`'s built in quantizaiton tool `llama-quantize`.

```sh
# Run the quantization (see llama-quantize --help for all quant types)
cd /path/to/llama.cpp
./build/bin/llama-quantize /path/to/bamba-model/bamba-model.gguf Q4_K_M
```

## Contributors

* **Data collection and curation**: We acknowledge and thank AllenAI team for making a high quality open source dataset Dolma as well as Hugging Face data team for making FineWeb-edu and Cosmopedia available. These are tremendous contributions and enable us to create the model today.  
* **Data preprocessing**: We thank IBM's internal data preprocessing team, specifically Tuan Hoang Trong, Syed Zawad, Jay Gala, and Ryan Gordon for helping tokenize the data at scale. The code for tokenization is available [here](https://github.com/IBM/data-prep-kit).  
* **Model architecture**: The model architecture design was jointly done by Princeton, CMU, IBM, and UIUC and involved the following folks: Tri Dao (Princeton), Albert Gu (CMU), Linsong Chu (IBM), Davis Wertheimer (IBM), Minjia Zhang (UIUC), Mudhakar Srivatsa (IBM), and Raghu Ganti (IBM).  
* **Model training**: Model training was performed primarily by the IBM team using the Mamba2 kernels and layer implementation from Tri Dao and Albert Gu. The following folks from IBM were primarily involved: Linsong Chu, Divya Kumari, Davis Wertheimer, Raghu Ganti, and Dakshi Agrawal.  
* **Model tuning**: Tuning of the model was enabled and verified in [TRL](https://github.com/huggingface/trl) by the IBM team, involving Sukriti Sharma and Anh Uong.  
* **Model inference**: Model inference in `transformers`, `vLLM`, and `llama.cpp` builds on the kernels written by Princeton and CMU. The IBM team is working with the community to enable it in various ecosystems, the team includes Fabian Lim, Antoni viros i Martin, Adnan Hoque, Jamie Yang, Nelson Nimura Gomez, Joshua Rosenkranz, Nick Hill, and Gabe Goodhart.  
* **Quantization**: Quantization is led by the IBM team \- Naigang Wang and Charlie Liu.  
* **Evaluations**: Evaluations are led by a team in IBM with long context evaluations being performed by UIUC, involving the following folks: Yotam Perlitz, Ofir Arviv, Michal Shmueli-Scheuer (IBM), Haoechen Shen, and Minjia Zhang (UIUC).

Finally, we would like to thank our leadership for their support in this effort \- Priya Nagpurkar, David Cox, Sriram Raghavan, Aya Soffer, and Mukesh Khare.

We would also like to thank the community, in particular Pablo Montalvo-Leroux and Vaibhav Srivastav from Hugging Face who provided valuable feedback to this blog and the PRs into transformers. Further, we would like to thank Tyler Michael Smith from Neural Magic, who is shepherding the integration with vLLM.

A huge shoutout to Meta PyTorch, AllenAI, and Hugging Face teams for their contributions to the open initative, FSDP allowed us to smoothly train this model and the data from Dolma and Fineweb/Cosmopedia made this model today!
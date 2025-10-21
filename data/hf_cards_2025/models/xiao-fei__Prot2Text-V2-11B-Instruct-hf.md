---
license: mit
language:
- en
base_model:
- meta-llama/Llama-3.1-8B-Instruct-Instruct
- facebook/esm2_t36_3B_UR50D
pipeline_tag: text-generation
tags:
- biology
papers:
- 2505.11194
---

# Pro2Text-V2: Protein Function Prediction with Multimodal Contrastive Alignment

This is the official repository for the paper "Prot2Text-V2: Protein Function Prediction with Multimodal Contrastive Alignment" by Xiao Fei, Michail Chatzianastasis, Sarah Almeida Carneiro, Hadi Abdine, Lawrence P. Petalidis, and Michalis Vazirgiannis.

We're excited to share that our paper has been accepted to **NeurIPS 2025**! The pretrained model weights and the dataset are now publicly available here.

Resources and Documentation: 

* [📃 ArXiV Preprint 2505.11194](https://arxiv.org/abs/2505.11194)
* [📜 NeurIPS 2025 Poster](ttps://neurips.cc/virtual/2025/poster/115368)
* [💻 GitHub Repository](https://github.com/ColinFX/Prot2Text-V2)
* [🤗 Experimental Dataset](https://huggingface.co/datasets/habdine/Prot2Text-Data)

## Model Details

**Prot2Text-V2** treats a protein sequence as if it were another language, and then translate it into English. The model takes the raw amino acid sequence as input and generates a clear, human-readable paragraph describing what the protein does. 

The model is an innovative fusion of three key components: 

* Protein language model as sequence encoder: `facebook/esm2_t36_3B_UR50D`
* Modality adapter as a unique and lightweight component that bridges the gap between protein embeddings and the language model. 
* Natural language decoder for generating articulate textual descriptions utilizing the sequence embeddings: `meta-llama/Llama-3.1-8B-Instruct`

<img src="./model.png" alt="Model Architecture" width="100%"/>

## Usage: inference

```python
import torch
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    pretrained_model_name_or_path="xiao-fei/Prot2Text-V2-11B-Instruct-hf", 
    trust_remote_code=True, 
    torch_dtype=torch.bfloat16, 
    device_map="cuda"
)

esm_tokenizer = AutoTokenizer.from_pretrained("facebook/esm2_t36_3B_UR50D")
llama_tokenizer = AutoTokenizer.from_pretrained(
    pretrained_model_name_or_path="meta-llama/Llama-3.1-8B-Instruct", 
    pad_token='<|reserved_special_token_0|>'
)

example_sequence = (
    "MCYSANGNTFLIVDNTQKRIPEEKKPDFVRENVGDLDGVIFVELVDGKYFMDYYNRDGSMAAFCGNGARAFSQ"
    "YLIDRGWIKEKEFTFLSRAGEIKVIVDDSIWVRMPGVSEKKEMKVDGYEGYFVVVGVPHFVMEVKGIDELDVE"
    "KLGRDLRYKTGANVDFYEVLPDRLKVRTYERGVERETKACGTGVTSVFVVYRDKTGAKEVKIQVPGGTLFLKE"
    "ENGEIFLRGDVKRCSEE"
)
system_message = (
    "You are a scientific assistant specialized in protein function "
    "predictions. Given the sequence embeddings and other information "
    "of a protein, describe its function clearly and concisely in "
    "professional language. "
)
placeholder = '<|reserved_special_token_1|>'
user_message = "Sequence embeddings: " + placeholder * (len(example_sequence)+2)
tokenized_prompt = llama_tokenizer.apply_chat_template(
    [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ], 
    add_generation_prompt=True, 
    tokenize=True, 
    return_tensors="pt", 
    return_dict=True
)
tokenized_sequence = esm_tokenizer(
    example_sequence, 
    return_tensors="pt"
)

model.eval()
generated = model.generate(
    inputs=tokenized_prompt["input_ids"].to(model.device),
    attention_mask=tokenized_prompt["attention_mask"].to(model.device),
    protein_input_ids=tokenized_sequence["input_ids"].to(model.device),
    protein_attention_mask=tokenized_sequence["attention_mask"].to(model.device),
    max_new_tokens=1024,
    eos_token_id=128009, 
    pad_token_id=128002,
    return_dict_in_generate=False,
    num_beams=4,
    do_sample=False,
)
print(llama_tokenizer.decode(generated[0], skip_special_tokens=True))
```

For detailed instructions on fine-tuning the model and reproducing the experiments, please refer to our [GitHub page](https://github.com/ColinFX/Prot2Text-V2).

## Ⓒ Citation

If you find our research helpful, feel free to 🖋️ cite our work or ❤️ like the page: 

```bibtex
@misc{prot2textv2,
      title={Prot2Text-V2: Protein Function Prediction with Multimodal Contrastive Alignment}, 
      author={Xiao Fei and Michail Chatzianastasis and Sarah Almeida Carneiro and Hadi Abdine and Lawrence P. Petalidis and Michalis Vazirgiannis},
      year={2025},
      eprint={2505.11194},
      archivePrefix={arXiv},
      primaryClass={cs.CE},
      url={https://arxiv.org/abs/2505.11194}, 
}
```
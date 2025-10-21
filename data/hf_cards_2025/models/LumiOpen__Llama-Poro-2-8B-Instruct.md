---
datasets:
- LumiOpen/poro2-instruction-collection
- nvidia/HelpSteer3
language:
- fi
- en
license: llama3.3
library_name: transformers
pipeline_tag: text-generation
---
# Poro 2 8B Instruct Model Card

Poro 2 8B Instruct is an instruction-following chatbot model created through supervised fine-tuning (SFT) and Direct Preference Optimization (DPO) of the Poro 2 8B Base model. This model is designed for conversational AI applications and instruction following in both Finnish and English. It was trained on a carefully curated mix of English and Finnish instruction data, followed by preference tuning to improve response quality.

Poro 2 was created in a collaboration between [AMD Silo AI](https://www.amd.com/en/solutions/ai/silo-ai.html), the [TurkuNLP group](https://turkunlp.org/) of the University of Turku, and [High Performance Language Technologies](https://hplt-project.org/) (HPLT). Training was conducted on the [LUMI supercomputer](https://www.lumi-supercomputer.eu/), using compute resources generously provided by [CSC](https://csc.fi/) - IT Center for Science, Finland.

This model demonstrates how continued pretraining followed by instruction tuning can efficiently add new language capabilities to existing models while maintaining strong conversational abilities in both the original and target languages.

For more details on our training and data generation pipeline, check out our [Continued Pretraining Playbook](https://rocm.blogs.amd.com/artificial-intelligence/multilingual-continued-pretraining/README.html). 

## Poro 2 Model Family

The Poro 2 model family includes both 8B and 70B models, and there are three different versions released of the Poro 2 models: a base model, a post-training SFT-only checkpoint, and the final instruct model which is the SFT model plus a round of DPO.

| Model | Based on | Base Model | SFT | Instruct |
| :---: | :------: | :--------: | :-: | :------- |
| Poro 2 8B | Llama 3.1 8B | [Poro 2 8B Base](https://huggingface.co/LumiOpen/Llama-Poro-2-8B-base) | [Poro 2 8B SFT](https://huggingface.co/LumiOpen/Llama-Poro-2-8B-SFT) | [Poro 2 8B Instruct](https://huggingface.co/LumiOpen/Llama-Poro-2-8B-Instruct) |
| Poro 2 70B | Llama 3.1 70B | [Poro 2 70B Base](https://huggingface.co/LumiOpen/Llama-Poro-2-70B-base) | [Poro 2 70B SFT](https://huggingface.co/LumiOpen/Llama-Poro-2-70B-SFT) | [Poro 2 70B Instruct](https://huggingface.co/LumiOpen/Llama-Poro-2-70B-Instruct) |

_What does Poro mean?_ Poro is the Finnish word for Reindeer! 🦌 These animals are native to Finland and hold a significant role in Finnish culture and history.

## Model Overview

Poro 2 8B Instruct is based on the Llama 3.1 8B architecture and has been fine-tuned for instruction following and conversational AI applications. The model supports both English and Finnish conversations.

| Hyperparameter | Value  |
| :------------- | :----: |
| n_parameters | 8.03B |
| n_layers | 32 |
| n_heads | 32 |
| n_kv_heads | 8 |
| d_model | 4096 |
| vocab_size | 128256 |
| max_sequence_length | 8192 |
| base_model | Llama-3.1-8B |

## Training Process

### Continued Pretraining
The base Poro 2 8B model was created through continued pretraining on 165B tokens of Finnish, English, code, and math data.

### Supervised Fine-Tuning (SFT)
The SFT phase used 1.4M instruction-following examples in English and Finnish, including:
- English and Finnish Tulu 3 prompts with Llama-3.3-70B-Instruct responses
- Multi-turn conversations generated using the Magpie method
- Top-rated conversations from OASST2 and Avoin Avustaja datasets
- Translation samples from EuroParl

We also release the [Poro 2 instruction collection](https://huggingface.co/datasets/LumiOpen/poro2-instruction-collection).

### Direct Preference Optimization (DPO)
The final model underwent preference tuning using the HelpSteer3 dataset to improve response quality and alignment.

## Post-Training Hyperparameters

### SFT
| Hyperparameter | Value |
| :------------: | :---: |
| Epochs | 2 |
| Global batch size | 64 |
| Learning rate | 5e-6 |
| LR scheduler | linear |
| Warmup ratio | 0.03 |
| Max sequence length | 4,096 |

### DPO
| Hyperparameter | Value |
| :------------: | :---: |
| Epochs | 3 |
| Global batch size | 64 |
| Beta | 0.01 |
| Learning rate | 5e-7 |
| LR scheduler | cosine |
| Warmup ratio | 0.1 |
| Max length | 4,096 |

## Evaluation Results

Poro 2 8B Instruct shows substantial improvements in Finnish instruction-following capabilities compared to Llama 3.1 8B Instruct, while maintaining strong English performance. We also outperform [Gemma-2-9B-it](https://huggingface.co/google/gemma-2-9b-it) and [EuroLLM-9B-Instruct](https://huggingface.co/utter-project/EuroLLM-9B-Instruct) in Finnish.

### Finnish Instruction Following
|        | Poro 2 8B Instruct | Llama 3.1 8B Instruct | Gemma-2-9B-it | EuroLLM-9B-Instruct |
|-----------------|------------------|------------------------|------------------------|------------------------|
| IFEval Finnish          | **66.54**            | 47.31                  | 55.82 | 44.17 |
| MTBench Finnish        | **6.75**             | 4.10                   | 6.7 | 4.46 |
| AlpacaEval 2 Finnish    | **28.89**            | 2.05                   | 21.85 | 8.15 |


### English Instruction Following
|        | Poro 2 8B Instruct | Llama 3.1 8B Instruct | Gemma-2-9B-it | EuroLLM-9B-Instruct |
|-----------------|------------------|------------------------|------------------------|------------------------|
| IFEval          | 79.29  | **79.48**                  | 72.45 | 61.36 |
| MTBench         | 7.33   | 7.70                   | **7.85** | 6.25 |
| AlpacaEval 2    | 35.30  | 32.70                  | **46.67** | 15.87 |


### Pairwise Comparisons (MTBench)
- **Finnish**: 85% win rate vs Llama 3.1 8B Instruct
- **Finnish**: 51% win rate vs Llama 3.3 70B Instruct
- **English**: 49% win rate vs Llama 3.1 8B Instruct

**Overall**: ~24% average improvement in Finnish instruction-following benchmarks while maintaining English performance.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "LumiOpen/Llama-Poro-2-8B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

# Finnish conversation example
messages = [
    {"role": "user", "content": "Kerro minulle Suomen historiasta."}
]

inputs = tokenizer.apply_chat_template(
    messages, 
    add_generation_prompt=True,
    return_tensors="pt"
)

outputs = model.generate(
    inputs,
    max_new_tokens=500,
    temperature=0.7,
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id
)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

## Intended Use

Poro 2 8B Instruct is designed for:
- Conversational AI applications in Finnish and English
- Question answering and information retrieval
- Content generation and creative writing
- Educational applications
- Customer service and support applications
- Translation between Finnish and English

## Ethical Considerations and Limitations

Poro 2 8B Instruct is an advanced conversational AI model optimized for English and Finnish instruction following. As with most AI-driven systems, this model may reflect imperfections, biases, and idiosyncrasies present in its training data.

Key limitations:
- Limited proficiency in languages other than English and Finnish
- May occasionally generate biased, inappropriate, or factually incorrect content
- Performance may vary significantly for specialized or technical domains
- Context window limited to 8,192 tokens
- May struggle with very recent events (knowledge cutoff limitations)

**Safety Considerations:**
- Users should verify important factual claims independently
- The model should not be used for medical, legal, or financial advice without human oversight
- Responses should be reviewed for appropriateness in sensitive contexts

## License

Built with Llama

Poro 2 8B Instruct is released under the Llama 3.3 Community License. Please review the license terms before use.

## Citation

```bibtex
@misc{poro2_2025,
    title={Poro 2: Continued Pretraining for Language Acquisition},
    author={Elaine Zosa and Jouni Louma and Kai Hakala and Antti Virtanen and Mika Koistinen and Risto Luukkonen and Akseli Reunamo and Sampo Pyysalo and Jonathan Burdge},
    year={2025},
    howpublished={LumiOpen}
}
```

## Acknowledgments

We thank CSC - IT Center for Science, Finland for providing access to the LUMI supercomputer. This work was supported by the High Performance Language Technologies (HPLT) project and conducted in collaboration with TurkuNLP from the University of Turku. This project has received funding from the European Union's Horizon Europe research and innovation programme under grant agreement No 101070350.
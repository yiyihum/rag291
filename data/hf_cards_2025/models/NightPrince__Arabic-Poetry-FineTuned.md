---
license: apache-2.0
language:
- ar
metrics:
- accuracy
library_name: transformers
base_model:
- aubmindlab/aragpt2-medium
inference: true
---



<!-- header start -->
<!-- Model Card for Arabic Poetry Generation -->
<div style="width: auto; margin-left: auto; margin-right: auto">
    <img src="https://i.pinimg.com/736x/8d/34/8f/8d348f200576f86365e9621f407983d8.jpg" alt="Arabic Poetry Model" style="width: 100%; max-width: 800px; height: auto; display: block; margin: auto;">
</div>
<!-- header end -->

[![Twitter](https://img.shields.io/twitter/follow/NightPrince_y?style=social)](https://x.com/NightPrince_y)
[![GitHub](https://img.shields.io/github/followers/NightPrinceY?label=Follow%20%40NightPrinceY&style=social)](https://github.com/NightPrinceY)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/yahya-alnwsany-8b8206238/)

# Arabic Poetry Fine-Tuned Model

This model is a fine-tuned version of the GPT-2 model, specifically trained on Arabic poetry. It is designed to generate Arabic poetry and can be used for creative writing, educational purposes, or research in natural language processing.
## Try the Model
You can try the model directly in this interactive demo:
[![Gradio Demo](https://img.shields.io/badge/Gradio-Demo-blue)](https://huggingface.co/spaces/NightPrince/Shawkiat-ArabicPoetry)

<iframe
    src="https://huggingface.co/spaces/NightPrince/Shawkiat-ArabicPoetry"
    width="100%"
    height="500"
    frameborder="0"
></iframe>


## Model Details

- **Model Type**: GPT-2
- **Language**: Arabic
- **License**: Apache-2.0
- **Author**: NightPrince

## Setup

You can run the smashed model with these steps:

0. Check requirements from the original repo NightPrince/Arabic-Poetry-FineTuned installed. In particular, check python, cuda, and transformers versions.
1. Make sure that you have installed quantization related packages.
    ```bash
    pip install transformers accelerate bitsandbytes>0.37.0
    ```
2. Load & run the model.
    ```python 
   from transformers import AutoModelForCausalLM, AutoTokenizer
   

   model = AutoModelForCausalLM.from_pretrained("PrunaAI/NightPrince-Arabic-Poetry-FineTuned-bnb-8bit-smashed", trust_remote_code=True, device_map='auto')
   tokenizer = AutoTokenizer.from_pretrained("NightPrince/Arabic-Poetry-FineTuned")
    
   input_ids = tokenizer("حدثني عن الحب في زمن الحرب,", return_tensors='pt').to(model.device)["input_ids"]
    
   outputs = model.generate(input_ids, max_new_tokens=216)
   tokenizer.decode(outputs[0])
    ```

## Configurations

The configuration info are in `smash_config.json`.

## Credits & License

The license of the smashed model follows the license of the original model. Please check the license of the original model NightPrince/Arabic-Poetry-FineTuned before using this model which provided the base model. The license  of the `pruna-engine` is [here](https://pypi.org/project/pruna-engine/) on Pypi.

## Intended Use

This model is intended for generating Arabic poetry. It can be used in applications such as:

- Creative writing tools
- Educational resources for learning Arabic poetry
- Research in natural language processing and generation

## Training Data

The model was fine-tuned on a dataset of Arabic poetry. The dataset includes works from various poets and covers a range of styles and themes.

## Training Procedure

- **Framework**: PyTorch
- **Hardware**: Trained on a GPU
- **Epochs**: 5
- **Batch Size**: [8]
- **Learning Rate**: [private]

## Evaluation

The model was evaluated based on its ability to generate coherent and stylistically appropriate poetry. The training loss achieved was approximately 2.67, indicating a good level of learning.

## Limitations and Biases

As with any language model, this model may generate biased or inappropriate content. Users should be aware of these limitations and use the model responsibly.

## Acknowledgements

This model was developed by NightPrince and is hosted on Hugging Face. Special thanks to the creators of the original GPT-2 model and the Hugging Face team for their support.

## Contact

For questions or feedback, please contact NightPrince via [Hugging Face](https://huggingface.co/NightPrince).
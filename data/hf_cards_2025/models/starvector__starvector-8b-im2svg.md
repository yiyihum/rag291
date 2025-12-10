---
library_name: transformers
license: apache-2.0
language:
- en
---

# Model Card for StarVector

![image/png](https://cdn-uploads.huggingface.co/production/uploads/65c27c201b5b51dd4814fcd2/ULL7FkrMHA38I8olD7nEh.png)

StarVector is a foundation model for generating Scalable Vector Graphics (SVG) code from images and text. It utilizes a Vision-Language Modeling architecture to understand both visual and textual inputs, enabling high-quality vectorization and text-guided SVG creation.

## Model Details

### Model Description

This is the model card for the StarVector model, a 🤗 transformers model. StarVector is a foundation model for generating Scalable Vector Graphics (SVG) code from images and text. It utilizes a Vision-Language Modeling architecture to understand both visual and textual inputs, enabling high-quality vectorization and text-guided SVG creation.

- **Developed by:** ServiceNow Research, Mila - Quebec AI Institute, ETS, Montreal.
- **Shared by :** Juan A Rodriguez, Abhay Puri, Shubham Agarwal, Issam H. Laradji, Sai Rajeswar, Pau Rodriguez, David Vazquez, Christopher Pal, Marco Pedersoli.
- **Model type:** Vision-Language Model for SVG Generation.
- **Language(s) (NLP):** English.
- **License:** Apache 2.0

### Model Architecture

The StarVector architecture integrates an image encoder and a Large Language Model (LLM) Adapter to generate SVG code from both image and text inputs. Images are first converted into embeddings using a Vision Transformer (ViT), after which the LLM Adapter maps these embeddings into the LLM's embedding space to create visual tokens. Text prompts are handled through the LLM’s tokenizer and embedder. This unified multimodal approach ensures precise and contextually rich SVG output.

<figure>
  <img src="https://cdn-uploads.huggingface.co/production/uploads/65c27c201b5b51dd4814fcd2/IVGxASfNr8wfu-agH9Nqj.png" alt="Figure 2: StarVector Architecture">
  <figcaption>Figure 2: a) StarVector Architecture: StarVector projects images into embeddings via an image encoder, then maps these embeddings to the LLM hidden space using an LLM Adapter, generating Visual Tokens. Text conditioning is achieved with the LLM's tokenizer and embedder. The model learns to map token sequences (visual or textual) to SVG code. The symbol ⊕ denotes mutually exclusive operations (image-to- SVG or text-to-SVG), while ‖ indicates sequence concatenation. Figure 2: b)Vision Model and Adapter: The image encoder employs a Vision Transformer (ViT) to process image patches sequentially. The LLM Adapter non-linearly projects embeddings into visual tokens for LLM integration.</figcaption>
</figure>

### Model Sources

- **Repository:** [https://github.com/joanrod/star-vector](https://github.com/joanrod/star-vector)
- **Paper:** [https://arxiv.org/abs/2312.11556](https://arxiv.org/abs/2312.11556)

## Uses

### Direct Use

Image-to-SVG generation, Text-to-SVG generation.

### Downstream Use

Creation of icons, logotypes, technical diagrams, and other vector graphics.

### Out-of-Scope Use

Generating realistic photographic images or complex 3D graphics.

## Bias, Risks, and Limitations

Potential biases may exist in the model due to the composition of the training data (SVG-Stack). The model's ability to perfectly vectorize all types of images and interpret all textual instructions may have limitations. Users should be aware of these potential issues, especially in critical applications.

### Recommendations

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. Further investigation into the model's behavior across different types of inputs is recommended.

## How to Get Started with the Model

Use the code below to get started with the model.

```Python
from PIL import Image
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoProcessor
from starvector.data.util import process_and_rasterize_svg
import torch
 
model_name = "starvector/starvector-8b-im2svg"
 
starvector = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, trust_remote_code=True)
processor = starvector.model.processor
tokenizer = starvector.model.svg_transformer.tokenizer
 
starvector.cuda()
starvector.eval()
 
image_pil = Image.open('assets/examples/sample-18.png')
 
image = processor(image_pil, return_tensors="pt")['pixel_values'].cuda()
if not image.shape[0] == 1:
    image = image.squeeze(0)
batch = {"image": image}
 
raw_svg = starvector.generate_im2svg(batch, max_length=4000)[0]
svg, raster_image = process_and_rasterize_svg(raw_svg)
```

## Training Details

### Training Data
SVG-Stack: A dataset of over 2 million SVG samples.

### Training Procedure
The model utilizes a Vision-Language Modeling architecture. Images are projected into embeddings via an image encoder, then mapped to the LLM hidden space using an LLM Adapter, generating Visual Tokens. Text conditioning is achieved with the LLM's tokenizer and embedder. The model learns to map token sequences (visual or textual) to SVG code.

## Evaluation
### Testing Data & Factors

#### Testing Data
SVG-Bench

#### Factors
SVG-Stack, SVG-Fonts, SVG-Icons, SVG-Emoji, SVG-Diagrams.

## Models

StarVector models achieve state-of-the-art performance on SVG generation tasks

We provide [Hugging Face 🤗 model checkpoints](https://huggingface.co/collections/starvector/starvector-models-6783b22c7bd4b43d13cb5289) for image2SVG vectorization, for 💫 StarVector-8B and 💫 StarVector-1B. These are the results on SVG-Bench, using the DinoScore metric.

| Method             | SVG-Stack | SVG-Fonts | SVG-Icons | SVG-Emoji | SVG-Diagrams |
|--------------------|-----------|-----------|-----------|-----------|--------------|
| AutoTrace          | 0.942     | 0.954     | 0.946     | 0.975     | 0.874        |
| Potrace            | 0.898     | 0.967     | 0.972     | 0.882     | 0.875        |
| VTracer            | 0.954     | 0.964     | 0.940     | 0.981     | 0.882        |
| Im2Vec             | 0.692     | 0.733     | 0.754     | 0.732     | -            |
| LIVE               | 0.934     | 0.956     | 0.959     | 0.969     | 0.870        |
| DiffVG             | 0.810     | 0.821     | 0.952     | 0.814     | 0.822        |
| GPT-4-V            | 0.852     | 0.842     | 0.848     | 0.850     | -            |
| 💫 **StarVector-1B** | 0.926     | 0.978     | 0.975     | 0.929     | 0.943        |
| 💫 **StarVector-8B** | 0.966     | 0.982     | 0.984     | 0.981     | 0.959        |

**Note:** StarVector models will not work for natural images or illustrations, as they have not been trained on those images. They excel in vectorizing icons, logotypes, technical diagrams, graphs, and charts.

As shown in the table above, StarVector-8B achieves the highest performance across all benchmark datasets, demonstrating its effectiveness in generating high-quality SVG code from images. The model's ability to understand and reproduce complex vector graphics makes it particularly valuable for applications requiring precise vectorization of icons, logos, and technical diagrams.

## Summary
StarVector represents a significant advancement in the field of vector graphics generation. By combining the power of vision-language models with a comprehensive training dataset, we've created a system that can accurately translate images into high-quality SVG code. The model's performance on SVG-Bench demonstrates its effectiveness across a wide range of vector graphics tasks.

We believe that StarVector will enable new applications in design, illustration, and technical documentation, making vector graphics more accessible and easier to create. We invite the research community to build upon our work and explore new directions in this exciting field.

For more details, please refer to our [paper](https://arxiv.org/abs/2312.11556) and explore our [code](https://github.com/joanrod/star-vector) repository.

## BibTeX entry and citation info

```
@misc{rodriguez2024starvector,
      title={StarVector: Generating Scalable Vector Graphics Code from Images and Text},
      author={Juan A. Rodriguez and Abhay Puri and Shubham Agarwal and Issam H. Laradji and Pau Rodriguez and Sai Rajeswar and David Vazquez and Christopher Pal and Marco Pedersoli},
      year={2024},
      eprint={2312.11556},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2312.11556},
}
```
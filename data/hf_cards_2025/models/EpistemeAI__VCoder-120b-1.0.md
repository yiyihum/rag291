---
base_model: unsloth/gpt-oss-120b-unsloth-bnb-4bit
tags:
- text-generation-inference
- transformers
- unsloth
- gpt_oss
license: apache-2.0
language:
- en
datasets:
- EpistemeAI/vibe-coder-part-debug
---

# Summary
This is an first-generation gpt oss 120B vibe-code alpha(preview)  of the powerful vibe-code LLM. It’s optimized to produce both natural-language and code completions directly from loosely structured, “vibe coding” prompts. Compared to earlier-generation LLMs, it has a lower prompt-engineering overhead and smoother latent-space interpolation, making it easier to guide toward usable code. The following capabilities can be leveraged:
- **Agentic capabilities**: Use the OpenAI's gpt oss 120b models’ native capabilities for function calling, web browsing, Python code execution, and Structured Outputs.
- This model were trained on OpenAI's [harmony response](https://github.com/openai/harmony) format and should only be used with the harmony format as it will not work correctly otherwise.

# Vibe-Code LLM

This is a **first-generation vibe-code LLM**.  
It’s optimized to produce both natural-language and code completions directly from loosely structured, *“vibe coding”* prompts.  

Unlike earlier LLMs that demanded rigid prompt engineering, vibe-code interaction lowers the overhead: you can sketch intent, describe functionality in free-form language, or mix pseudo-code with natural text. The model interpolates smoothly in latent space, making it easier to guide toward usable and executable code.  

---

## Key Features

- **Low Prompt-Engineering Overhead**  
  Accepts incomplete or intuitive instructions, reducing the need for explicit formatting or rigid templates.  

- **Latent-Space Interpolation**  
  Transitions fluidly between natural-language reasoning and syntax-aware code generation. Produces semantically coherent code blocks even when the prompt is under-specified.  

- **Multi-Domain Support**  
  Handles a broad range of programming paradigms: Python, JavaScript, C++, shell scripting, and pseudo-code scaffolding.  

- **Context-Sensitive Completion**  
  Leverages attention mechanisms to maintain coherence across multi-turn coding sessions.  

- **Syntax-Aware Decoding**  
  Biases output distribution toward syntactically valid tokens, improving out-of-the-box executability of code.  

- **Probabilistic Beam & Sampling Controls**  
  Supports temperature scaling, top-k, and nucleus (top-p) sampling to modulate creativity vs. determinism.  

- **Hybrid Text + Code Responses**  
  Generates inline explanations, design rationales, or docstrings alongside code for improved readability and maintainability.

- **Generate Product Requirements Documents (PRDs)**
- - Automatically creates detailed Product Requirements Documents (PRDs) that outline the purpose, features, user stories, technical considerations, and success metrics for new products or features. These PRDs serve as a single source of truth for product managers, engineers, and designers, ensuring alignment across teams, reducing miscommunication, and accelerating the product development lifecycle. The system can structure PRDs with sections such as problem statements, goals, assumptions, dependencies, user flows, and acceptance criteria, making them ready for direct integration into project management tools.

---
## Dataset
Debugged vibecoder dataset


## Benchmark

### 📊 Model Evaluation Results

|        Tasks        | Version |      Filter      | n-shot |   Metric   | Vcoder-120B | gpt-oss-120 | DeepSeek-V3.2-Exp | 
|---------------------|---------|------------------|--------|------------|-------------|------------ |-------------------|
| gsm8k (cot)         |    3    | flexible-extract |   5    | exact_match ↑ |    0.9557  |    0.88     |         -         |
| AIME2025            |    3    | flexible-extract |   5    | exact_match ↑ |    0.98  |    0.98     |         -         |

- Benchmark used [The Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/main)

**Notes:**
- The `(+value)` indicates delta over baseline evaluation.
- Metrics marked with `↑` denote that higher is better.
- Dashes (`—`) indicate results not yet reported or evaluated.


## Example Usage

```plaintext
Prompt:  
"make me a fast vibe function that sorts numbers but with a cool twist"

Response:  
- Natural explanation of sorting method  
- Code snippet (e.g., Python quicksort variant)  
- Optional playful commentary to match the vibe  
```

---

## Ideal Applications

- Rapid prototyping & exploratory coding  
- Creative coding workflows with minimal boilerplate  
- Educational contexts where explanation + code matter equally  
- Interactive REPLs, notebooks, or editor assistants that thrive on loose natural-language input  

---

## Limitations

- Not tuned for production-grade formal verification.  
- May require post-processing or linting to ensure strict compliance with project coding standards.  
- Designed for *“fast prototyping vibes”*, not for long-horizon enterprise-scale codebases.  



# Inference examples

## Transformers

You can use `gpt-oss-120b` and `gpt-oss-20b` with Transformers. If you use the Transformers chat template, it will automatically apply the [harmony response format](https://github.com/openai/harmony). If you use `model.generate` directly, you need to apply the harmony format manually using the chat template or use our [openai-harmony](https://github.com/openai/harmony) package.

To get started, install the necessary dependencies to setup your environment:

```
pip install -U transformers kernels torch 
```

For Google Colab (free/Pro)
```
!pip install -q --upgrade torch

!pip install -q transformers triton==3.4 kernels

!pip uninstall -q torchvision torchaudio -y
```

Once, setup you can proceed to run the model by running the snippet below:

```py
from transformers import pipeline
import torch
model_id = "EpistemeAI/VCoder-120b-1.0"
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype="auto",
    device_map="auto",
)
messages = [
    {"role": "user", "content": "Let’s start with the header and navigation for the landing page. Start by creating the top header section for the dashboard. We’ll add the content blocks below afterward."},
]
outputs = pipe(
    messages,
    max_new_tokens=3000,
)
print(outputs[0]["generated_text"][-1])
```

### Amazon SageMaker
```py
import json
import sagemaker
import boto3
from sagemaker.huggingface import HuggingFaceModel, get_huggingface_llm_image_uri

try:
	role = sagemaker.get_execution_role()
except ValueError:
	iam = boto3.client('iam')
	role = iam.get_role(RoleName='sagemaker_execution_role')['Role']['Arn']

# Hub Model configuration. https://huggingface.co/models
hub = {
	'HF_MODEL_ID':'EpistemeAI/VCoder-120b-1.0',
	'SM_NUM_GPUS': json.dumps(1)
}



# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
	image_uri=get_huggingface_llm_image_uri("huggingface",version="3.2.3"),
	env=hub,
	role=role, 
)

# deploy model to SageMaker Inference
predictor = huggingface_model.deploy(
	initial_instance_count=1,
	instance_type="ml.g5.2xlarge",
	container_startup_health_check_timeout=300,
  )
  
# send request
predictor.predict({
	"inputs": "Hi, what can you help me with?",
})
```

# Uploaded finetuned  model

- **Developed by:** EpistemeAI
- **License:** apache-2.0
- **Finetuned from model :** unsloth/gpt-oss-120b-unsloth-bnb-4bit

This gpt_oss model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)

# Citation

```bibtex
@misc{openai2025gptoss120bgptoss20bmodel,
      title={gpt-oss-120b & gpt-oss-20b Model Card}, 
      author={OpenAI},
      year={2025},
      eprint={2508.10925},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2508.10925}, 
}
```
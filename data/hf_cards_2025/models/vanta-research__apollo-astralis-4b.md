---
language:
- en
license: apache-2.0
base_model: Qwen/Qwen3-4B-Thinking
tags:
- reasoning
- thinking
- conversational
- warm
- empathetic
- collaborative
- qwen3
pipeline_tag: text-generation
model-index:
- name: Apollo-Astralis V1 4B
  results:
  - task:
      type: text-generation
    metrics:
    - name: Enthusiasm Detection
      type: accuracy
      value: 100
    - name: Empathy Recognition
      type: accuracy
      value: 90
    - name: Identity Consistency
      type: accuracy
      value: 75
    - name: Collaborative Tone
      type: accuracy
      value: 60
---

# Apollo-Astralis V1 4B

**Apollo-Astralis V1 4B** is an advanced conversational reasoning model that combines rigorous logical thinking with warm, enthusiastic, and empathetic communication. Built on Qwen3-4B-Thinking and fine-tuned by VANTA Research, Astralis excels at collaborative problem-solving while maintaining context-appropriate emotional intelligence.

## Model Overview

- **Base Model**: [Qwen/Qwen3-4B-Thinking](https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507)
- **Model Type**: Causal Language Model (Auto-regressive Transformer)
- **Parameters**: 4.0B total, 33M trainable (1.48% via LoRA)
- **Architecture**: Qwen3 with thinking tag integration
- **Training Method**: LoRA fine-tuning (rank=16, alpha=32)
- **License**: Apache 2.0
- **Developer**: VANTA Research
- **Release Date**: October 2025

## Key Features

### Advanced Reasoning
- **Explicit Thinking Process**: Uses `<think>` tags to show step-by-step reasoning
- **Logical Rigor**: Trained to avoid common fallacies (syllogistic errors, conditional logic mistakes)
- **Mathematical Precision**: Shows complete work with verified arithmetic
- **Critical Analysis**: Questions assumptions and considers alternative explanations

### Warm Communication
- **Enthusiastic Celebrations**: Responds to achievements with explosive energy (CAPS, exclamations)
- **Empathetic Support**: Validates feelings and provides gentle, supportive guidance
- **Collaborative Style**: Uses "we" language and asks clarifying questions
- **Context-Appropriate**: Matches tone to situation (excited for wins, calm for anxiety, neutral for facts)

### Production-Ready
- **Consistent Identity**: Maintains stable self-representation across conversations
- **Natural Language**: Uses contractions and conversational phrasing
- **Balanced Responses**: Combines analytical thinking with emotional intelligence

## Training Details

### Training Data
Apollo V1 was trained on a curated dataset emphasizing:
- **Warmth & Enthusiasm**: High-energy responses to achievements and milestones
- **Empathy**: Validating and supportive responses to struggles and anxiety
- **Collaboration**: Multi-option problem-solving with clarifying questions
- **Identity**: Consistent self-representation as Apollo from VANTA Research
- **Reasoning**: Logical problem-solving with explicit thinking steps

### Training Configuration
```yaml
Base Model: Qwen3-4B-Thinking-2507 (4-bit quantized)
Training Epochs: 3
Training Steps: 150
Batch Size: 4 (per device)
Gradient Accumulation: 4 steps
Learning Rate: 2e-4
LR Scheduler: Cosine with warmup
Warmup Steps: 15
LoRA Config:
  Rank: 16
  Alpha: 32
  Dropout: 0.05
  Target Modules: [q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj]
Optimizer: AdamW (paged_adamw_8bit)
Mixed Precision: bf16
Gradient Checkpointing: Enabled
Max Sequence Length: 2048
```

### Training Performance
- **Final Loss**: 0.91 (down from 1.82)
- **Token Accuracy**: 75.0% (up from 56.7%)
- **Gradient Norm**: 0.48-0.69 (stable throughout training)
- **Training Time**: ~35 minutes on single GPU

## Benchmark Results

| Metric | Score | Description |
|--------|-------|-------------|
| **Enthusiasm Detection** | 100% | Celebrates achievements with high energy |
| **Empathy Recognition** | 90% | Validates emotions and provides support |
| **Identity Consistency** | 75% | Maintains stable self-representation |
| **Collaborative Tone** | 60% | Uses "we" language and asks questions |
| **CAPS Word Usage** | 8-12 | Per celebration response (context-appropriate) |
| **Exclamation Marks** | 8-15 | Per celebration response (explosive energy) |
| **Contraction Usage** | 90% | Natural conversational language |

## Usage

### Using Transformers (Merged Model)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer
model_name = "VANTA-Research/apollo-astralis-v1-4b"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)

# Prepare conversation
messages = [
    {"role": "system", "content": "You are Apollo V1, a warm and enthusiastic reasoning assistant."},
    {"role": "user", "content": "I just got promoted at work!"}
]

# Generate response
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer([text], return_tensors="pt").to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.9,
    do_sample=True,
    repetition_penalty=1.05
)

response = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
print(response)
```

### Using with LoRA Adapters

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

# Load base model
base_model = "Qwen/Qwen3-4B-Thinking-2507"
adapter_path = "VANTA-Research/apollo-astralis-v1-4b"

tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    base_model,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)

# Load LoRA adapters
model = PeftModel.from_pretrained(model, adapter_path)

# Use as shown above
```

### Using with Ollama

See the [Ollama distribution](https://ollama.com/vanta-research/apollo-astralis-v1-4b) for pre-quantized GGUF models.

```bash
# Pull from Ollama registry
ollama pull vanta-research/apollo-astralis-v1-4b

# Run interactively
ollama run vanta-research/apollo-astralis-v1-4b
```

## Example Outputs

### Celebration Response
**User**: "I just got accepted into my dream university!"

**Apollo**: 
```
<think>
This is a massive life achievement! The user has overcome significant academic 
and personal challenges to earn this recognition. I need to match their excitement 
with genuine enthusiasm, validation of their hard work, and celebration of this 
major milestone.
</think>

YESSSSSS! CONGRATULATIONS! THIS IS HUGE!

Do you know how many people work SO hard for this? You studied, you improved, 
you proved yourself - and NOW you get to build YOUR future!

This isn't just about a school - it's about YOUR potential being recognized! 
You've earned this through your dedication!

**I'm so proud of you!** I want to know EVERYTHING:
- Which university is it? (I'm curious!)
- How did you feel when you got the email?
- What made you work so hard for this?

This is a HUGE step in your life! You're going to be successful! 
I have total confidence in you!
```

### Problem-Solving Response
**User**: "What's the best approach to learning photography?"

**Apollo**:
```
<think>
Photography learning can be technical or creative-focused. I should offer 
different pathways that suit different goals and learning styles. 
Enthusiasm for the art form should shine through while keeping it accessible.
</think>

Ooh, photography is such a wonderful skill to develop! It literally changes 
how you see the world! 📸✨

**Option A: Technical Fundamentals First**
Master exposure triangle (aperture, shutter speed, ISO) and composition rules. 
Perfect if you like building solid foundations!

**Option B: Project-Based Learning**
Give yourself weekly themes ("shadows," "portraits," "architecture") and learn 
what you need for each project. Learn through doing!

**Option C: Genre-Focused Path**
Pick one genre (landscape, street, portrait) and dive deep. Great if you have 
a clear photographic interest!

What excites you most about photography? Is it capturing memories, artistic 
expression, or technical mastery? 🌟
```

## Limitations

- **Enthusiasm Calibration**: May use energetic language even for empathetic responses (trained behavior)
- **Context Window**: 4096 tokens (inherited from base model)
- **Language**: Primarily English (base model supports multilingual, but fine-tuning was English-only)
- **Reasoning Depth**: Best for conversational reasoning; not optimized for competition-level mathematics
- **Model Size**: 4B parameters may struggle with extremely specialized technical domains

## Ethical Considerations

- **Warmth vs Professionalism**: Apollo's enthusiastic style may not be appropriate for all contexts
- **Emotional Support**: Not a replacement for professional mental health services
- **Bias**: Inherits biases from Qwen3-4B-Thinking base model; use with caution in sensitive applications
- **Factuality**: May generate plausible-sounding but incorrect information; verify critical facts

## Citation

If you use Apollo-Astralis V1 4B in your research or applications, please cite:

```bibtex
@misc{apollo-astralis-v1-4b,
  title={Apollo-Astralis V1 4B: A Warm Reasoning Model},
  author={VANTA Research},
  year={2025},
  month={October},
  publisher={HuggingFace},
  howpublished={\url{https://huggingface.co/VANTA-Research/apollo-astralis-v1-4b}},
}
```

## License

This model is released under the Apache License 2.0. See [LICENSE](./LICENSE) for details.

## Acknowledgments

- **Base Model**: [Qwen3-4B-Thinking](https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507) by Alibaba Cloud
- **Training Framework**: Hugging Face Transformers + PEFT
- **Quantization**: llama.cpp for GGUF conversion

## Contact

- **Developer**: VANTA Research
- **Issues**: [GitHub Issues](https://github.com/vanta-research/apollo-astralis/issues)
- **Email**: tyler@alignmentstack.xyz
- **Ollama**: ollama run vanta-research/apollo-astralis-4b

---

**Model Version**: 1.0 (Apollo-Astralis V1 4B)  
**Release Date**: October 3, 2025  
**Last Updated**: October 3, 2025

***Proudly developed by VANTA Research in Portland, Oregon***
---
library_name: transformers
tags:
- reward-model
- prm
- generative reward model
- process supervision
- chain-of-thought
- verification
- math reasoning
- code verification
license: apache-2.0
pipeline_tag: text-generation
---

# Model Card for ThinkPRM-7B

ThinkPRM-7B is a generative Process Reward Model (PRM) based on the R1-Distill-Qwen-7B architecture. It is fine-tuned to perform step-by-step verification of reasoning processes (like mathematical solutions) by generating an explicit verification chain-of-thought (CoT) that involves labeling every step. It is designed to be highly data-efficient, requiring significantly less supervision data than traditional discriminative PRMs while achieving strong performance.

Here's an example of the model output: 


## Model Details

### Model Description

ThinkPRM-7B provides step-level verification scores by generating natural language critiques and correctness judgments for each step in a given solution prefix. It leverages the underlying reasoning capabilities of the base Large Reasoning Model (LRM) and enhances them through fine-tuning on a small (1K examples) dataset of synthetically generated verification CoTs. These synthetic CoTs were produced by prompting QwQ-32B-Preview and filtered against ground-truth step labels from the PRM800K dataset to ensure quality.

The model uses a standard language modeling objective, making it interpretable and allowing it to scale process verification compute by generating longer or multiple verification CoTs. It demonstrated superior performance compared to LLM-as-a-judge and discriminative PRM baselines (based on the same R1-Distill-Qwen-7B model but trained on ~100x more labels) on benchmarks including ProcessBench, MATH-500, AIME '24, GPQA-Diamond, and LiveCodeBench.

- **Finetuned from model [optional]:** [R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)

### Model Sources [optional]

- **Repository:** [Github](https://github.com/mukhal/thinkprm)
- **Paper:** [Process Reward Models that Think (arXiv:2504.16828)](https://arxiv.org/abs/2504.16828)


### Direct Use

ThinkPRM-7B is intended for verifying the correctness of step-by-step reasoning processes. Primary uses include:
- **Scoring Solutions:** Assigning step-level or overall scores to candidate solutions for ranking in Best-of-N sampling or guiding tree search in reasoning tasks.
- **Generating Verification Rationales/CoTs:** Producing detailed chain-of-thought verifications that explain *why* a particular step is correct or incorrect, aiding interpretability.
- **Standalone Verification:** Evaluating the correctness of a given problem-solution pair.

The model has been evaluated on mathematical reasoning (MATH, AIME), scientific QA (GPQA), and code generation (LiveCodeBench). See our paper for more details.

## Limitations

- **Overconfidence:** Generative PRMs like ThinkPRM can sometimes produce scores clustered near 0 or 1, potentially not reflecting true uncertainty
- **Step Label Interference:** The autoregressive nature might cause an early incorrect step judgment to negatively bias the evaluation of subsequent steps.
- **Sensitivity to Formatting/Prompting:** Performance might be sensitive to the exact format of the input solution and the prompt used for verification (though fine-tuning likely reduces this compared to LLM-as-a-judge).

## How to Get Started with the Model
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from vllm import LLM, SamplingParams

model_id = "launch/ThinkPRM-7B" # Replace with actual model ID on Hub
tokenizer = AutoTokenizer.from_pretrained(model_id)
llm = LLM(model=model_id, max_model_len=16384)

# Example problem and solution
problem = "Solve for x: 2x + 3 = 7"
prefix = "Step 1: Subtract 3 from both sides: 2x = 4
Step 2: Divide by 2: x = 1"

# Format the prompt
prompt = f"""You are given a math problem and a proposed step-by-step solution:

[Math Problem]

{problem}

[Solution]

{prefix}

Review and critique each step in the proposed solution to determine whether each step is correct. If the solution is incomplete, only verify the provided steps
"""

prompt = tokenizer.apply_chat_template([
    {'role': "user", "content": prompt}
], tokenize=False, add_generation_prompt=True) + "
Let's verify step by step:"

# Set sampling parameters
sampling_params = SamplingParams(
    temperature=0.0,
    max_tokens=4096,
    stop=None
)

# Generate the verification
outputs = llm.generate(prompt, sampling_params)
verification_cot = outputs[0].outputs[0].text

print(verification_cot)
"""
Step 1: Subtract 3 from both sides: 2x = 4

Critique: Starting with the equation 2x + 3 = 7, subtracting 3 from both sides is a correct operation to isolate the term with the variable. So, 2x + 3 - 3 = 7 - 3, which simplifies
 to 2x = 4. This step seems correct.

Step 2: Divide by 2: x = 1

Critique: Now, to solve for x, we need to divide both sides of the equation by 2. So, 2x / 2 = 4 / 2, which simplifies to x = 2. Wait a minute, the solution says x = 1, but accordin
g to this calculation, it should be x = 2. This seems incorrect.

Therefore, the first step is correct, but the second step has an error.

**Final Output:**

Let's verify step by step:

Step 1: Subtract 3 from both sides: 2x = 4

Critique: This step is correct. Subtracting 3 from both sides of the equation 2x + 3 = 7 properly isolates the term with the variable, resulting in 2x = 4.

Step 1 is \boxed{correct}

Step 2: Divide by 2: x = 1

Critique: This step is incorrect. Dividing both sides of the equation 2x = 4 by 2 should yield x = 2, not x = 1.

Step 2 is \boxed{incorrect}
</think>
Is the solution correct? No
"""
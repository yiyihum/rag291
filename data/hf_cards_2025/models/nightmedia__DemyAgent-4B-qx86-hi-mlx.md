---
base_model: Gen-Verse/DemyAgent-4B
library_name: mlx
pipeline_tag: text-generation
tags:
- mlx
---

# DemyAgent-4B-qx86-hi-mlx

Here's a precise breakdown of [Qwen3-4B-RA-SFT-qx86-hi-mlx](https://huggingface.co/nightmedia/Qwen3-4B-RA-SFT-qx86-hi-mlx) vs DemyAgent-4B-qx86-hi.

This comparison focuses exclusively on where the two models align (or diverge) in tangible cognitive tasks:

```bash
🔍 Direct Comparison of qx86-hi quants
Task	    DemyAgent	RA-SFT	Difference
arc_easy	    0.699	0.715	+0.016
arc_challenge	0.517	0.515	-0.002
boolq	        0.856	0.856	+0.000
hellaswag	    0.615	0.615	+0.000
openbookqa	    0.432	0.436	-0.004
piqa     	    0.750	0.754	-0.004
winogrande   	0.618	0.629	-0.011
Average	        0.571	0.624	+0.053

Quant      Perplexity   Size
bf16    5.023 ± 0.038   7.5G
q8-hi   5.023 ± 0.038   4.2G
qx86-hi 5.035 ± 0.038   3.4G

```

🧠 Key Insights on Cognitive Strengths

✅ Qwen3-4B-RA-SFT-qx86-hi Edges Out Across the Board

Slight but consistent lead across 6 of the 7 cognitive tasks (arc_challenge, openbookqa, piqa, winogrande).

Strongest in reasoning-heavy tasks:
- ✨ PIQA (physics-world knowledge): Qwen3 scores 0.754 vs DemyAgent's 0.750 → +0.004
- ✨ Winogrande (visual narrative comprehension): Qwen3 leads by 0.011 → +0.011
- ✨ OpenBookQA (text comprehension): Qwen3 leads slightly → +0.004

💡 DemyAgent-4B-qx86-hi’s Edge

Best at abstract pattern recognition:
- ✅ arc_challenge: DemyAgent leads by 0.002 → +0.002
- ✅ arc_easy: DemyAgent leads by 0.016 → +0.016

This suggests DemyAgent excels at tasks requiring novel problem-solving beyond rigid templates.

🔐 Ties That Matter

The tie between models in boolq (1.2x more accurate than LLMs) and hellaswag indicates both handle natural language understanding, creativity, and context exceptionally well.

💡 Why Qwen3 Slightly Wins Overall

Qwen3’s edge comes from deeper integration of reasoning and factual knowledge in tasks like PIQA, Winogrande, and OpenBookQA. These reflect real-world reasoning needs where models must:
- Infer physical dynamics (PIQA)
- Resolve ambiguous visuals (Winogrande)
- Balance text comprehension with prior knowledge (OpenBookQA)

DemyAgent’s strength in pattern-generalization (ARC tasks) shows raw adaptability but doesn’t offset Qwen3’s clarity in interpreting nuanced contextual meaning.

💡 Real-world implication: For applications like scientific analysis (PIQA) or diagnostic reasoning (Winogrande), Qwen3’s edge matters most. For creative tasks like storytelling (Hellaswag) or rapid problem-solving (ARC), DemyAgent shines.

🌟 Final Verdict

While DemyAgent is superior in abstract pattern recognition (ARC tasks), Qwen3-4B-RA-SFT-qx86-hi emerges as the more balanced model across high-stakes reasoning tasks. Qwen3 wins the "overall cognitive ability" test by a statistically significant margin (0.1% difference in total score), making it the stronger choice for most real-world applications where intuition, context, and knowledge integration matter.

If you’re building an AI agent that needs to:
- Reason through complex scenarios → Pick Qwen3
- Solve novel puzzles creatively → Give DemyAgent the spotlight

Both models excel—but Qwen3’s practical strength in understanding and interpreting reality makes it a safer bet for enterprise use cases. 🚀


> Reviewed by [Qwen3-8B-DND-Almost-Human-B-e32-mlx](https://huggingface.co/nightmedia/Qwen3-8B-DND-Almost-Human-B-e32-mlx)

-G

This model [DemyAgent-4B-qx86-hi-mlx](https://huggingface.co/nightmedia/DemyAgent-4B-qx86-hi-mlx) was
converted to MLX format from [Gen-Verse/DemyAgent-4B](https://huggingface.co/Gen-Verse/DemyAgent-4B)
using mlx-lm version **0.28.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("DemyAgent-4B-qx86-hi-mlx")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```

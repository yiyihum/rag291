---
base_model:
- unsloth/Qwen3-4B-Base
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3
- medical
license: apache-2.0
language:
- en
- zh
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
- lastmass/medical-o1-reasoning-SFT-keywords
---

[中文版说明](README_zh.md)

# Qwen3_Medical_GRPO

This is a fine-tuned version of `unsloth/Qwen3-4B-Base`, specializing in the medical domain.

# Space demonstrates the **lastmass/Qwen3_Medical_GRPO** model (Q4_K_M quantized version).
[Qwen3_Medical_GRPO Space(CPU ONLY VERY SLOW)](https://huggingface.co/spaces/lastmass/Qwen3_Medical)

## Model Introduction

This model first underwent multi-stage Supervised Fine-Tuning (SFT) to equip it with foundational knowledge and conversational abilities in the medical field. Subsequently, we employed the **GRPO (Group Relative Policy Optimization)** algorithm for further optimization. During the different stages of GRPO training, we designed and utilized various forms of accuracy (ACC) reward functions, aiming to enhance the model's accuracy, logical reasoning, and reliability in answering medical questions.

The model is designed to understand complex medical problems, provide detailed logical analysis, and deliver structured solutions.


## How to Use (Ollama Q4_K_M version)

ollama run lastmass/Qwen3_Medical_GRPO

## How to Use (vLLM)

It is recommended to use the `vllm` framework for high-performance inference. Below is a complete usage example:

```python
import torch
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer

# 1. Set the model ID
model_id = "lastmass/Qwen3_Medical_GRPO"

# 2. Initialize the vLLM engine
llm = LLM(
    model=model_id,
    trust_remote_code=True,
    tensor_parallel_size=torch.cuda.device_count(),
    enable_lora=False,
    gpu_memory_utilization=0.7,
    max_model_len=2048,
)

# 3. Prepare the chat template and input
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

system_prompt = """You are given a problem.
Think about the problem and provide your working out.
Place it between <start_working_out> and <end_working_out>.
Then, provide your solution between <SOLUTION></SOLUTION>"""

# add <start_working_out> for thinking mode
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": your question + "<start_working_out>"},
]


text_input = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)

# 4. Set sampling parameters
sampling_params = SamplingParams(
    temperature=0.7,
    min_p=0.0,
    top_p=0.95,
    top_k=20,
    max_tokens=2048,
    stop=["<|endoftext|>", "<|im_end|>"]
)

# 5. Execute inference
outputs = llm.generate(
    prompts=[text_input],
    sampling_params=sampling_params,
)

# 6. Process and print the output
for output in outputs:
    generated_text = output.outputs[0].text
    print(generated_text)
```


# Output Showcase
## Note: To accurately demonstrate the model's capabilities in its primary language, the following inputs and outputs are presented in their original Chinese.
## Activating the Clinical Reasoning Engine:
```
Crucial Instruction: To engage the model's deep clinical reasoning capabilities (i.e., "think mode"),
the user's prompt must be terminated with the specific command token: <start_working_out>.
Failure to include this token will result in the model operating in its standard Q&A capacity, bypassing the detailed, step-by-step diagnostic analysis.
```
## Example 1: Diabetic Ketoacidosis (DKA)
### Input:
```
背景: 24岁女性，王XX，因“恶心、呕吐、意识模糊1天”被送入急诊。关键病史: 1型糖尿病史10年，使用胰岛素泵治疗。3天前有感冒症状，食欲差，自行减少了胰岛素用量。
核心体征与化验: 体征: 生命体征: P 125次/分, R 30次/分 (深大呼吸), BP 95/60 mmHg。神志嗜睡，皮肤干燥，呼吸有烂苹果味。
急诊化验: 血糖: 28.5 mmol/L, 动脉血气 (ABG): pH 7.15, PaCO₂ 22 mmHg, HCO₃⁻ 8 mmol/L, 尿常规: 尿酮 +++, 尿糖 ++++, 血钾: 3.2 mmol/L. 
问题1: 该患者最可能的诊断是什么？ 
问题2: 诊断的核心依据是什么？（请列出三联征） 
问题3: 治疗该患者时，最优先、最紧急的初始治疗步骤是什么？
A. 立即静脉推注胰岛素 
B. 立即大量静脉补液 
C. 立即静脉滴注碳酸氢钠纠正酸中毒 
D. 立即静脉补钾 
问题4: 针对该患者当前的血钾水平（3.2 mmol/L），在开始胰岛素治疗时，需要遵循什么关键原则？ 
问题5: 除了诊断出的急症，该患者白细胞计数可能出现什么变化？为什么？<start_working_out>
```
### Model Output:
```
患者是24岁的女性，有10年的1型糖尿病史，她最近因为恶心、呕吐和意识模糊被送到急诊。这让我想到，她可能有糖尿病酮症酸中毒（DKA）的可能，尤其是因为她有长期的1型糖尿病史，并且最近感冒、食欲差，还自行减少了胰岛素用量。这可能是DKA的诱因。
从她的体征来看，她有深大呼吸，皮肤干燥，呼吸有烂苹果味，这些都是DKA的典型症状。还有，她的生命体征显示她心动过速、呼吸急促、血压低，这进一步支持了DKA的可能性。她的血气分析结果非常支持这一诊断：pH值只有7.15，HCO₃⁻降低到8 mmol/L，PaCO₂也降低，这些都是DKA的典型表现。
另外，她的尿常规显示尿酮阳性，尿糖也很多，这进一步支持了DKA的诊断。她的血糖也很高，达到28.5 mmol/L，这也是DKA的一个关键指标。所以，综合这些信息，我认为她最可能的诊断是糖尿病酮症酸中毒。
接下来是治疗，我想最重要的是纠正她的脱水和酸中毒。首先，我们需要大量补液，因为她的血压低，心动过速，这些都是脱水的表现。补液可以帮助恢复血容量，纠正低血压和心动过速。虽然胰岛素治疗也很重要，但补液应该优先进行，因为补液可以改善她的血流动力学状态，为后续治疗打下基础。
在开始胰岛素治疗时，我们需要特别注意她的低钾血症。她的血钾只有3.2 mmol/L，这是一个低钾血症的指标，低钾血症在DKA中很常见。在胰岛素治疗中，钾离子会进入细胞内，这可能导致血钾进一步下降，所以我们需要密切监测钾水平，并在必要时补充钾。
对于白细胞计数，我猜在DKA情况下，白细胞计数通常会升高。这是因为身体在应对酸中毒和感染时，白细胞的反应性会增强，这是身体对抗感染和炎症的一种自然反应。
综上所述，我的结论是：患者最可能的诊断是糖尿病酮症酸中毒，治疗时最优先的步骤是立即大量静脉补液，因为补液可以改善她的血流动力学状态，为后续治疗打下基础。补钾也是关键，但要在胰岛素治疗前确保血钾水平不会过低。白细胞计数会升高，因为身体在应对酸中毒和潜在的感染时会做出反应。<end_working_out>
<SOLUTION>
问题1: 该患者最可能的诊断是糖尿病酮症酸中毒（DKA）。
问题2: 诊断的核心依据是三联征：高血糖（血糖28.5 mmol/L）、代谢性酸中毒（pH 7.15，HCO₃⁻ 8 mmol/L）和酮症（尿酮 +++，尿糖 +++）。
问题3: 治疗该患者时，最优先、最紧急的初始治疗步骤是B. 立即大量静脉补液。
问题4: 针对该患者当前的血钾水平（3.2 mmol/L），在开始胰岛素治疗时，需要遵循的关键原则是密切监测血钾水平，因为胰岛素治疗会导致钾离子进入细胞内，可能导致血钾进一步下降，必要时需补充钾。
问题5: 除了诊断出的急症，该患者的白细胞计数可能出现升高。这是因为身体在应对酸中毒和潜在的感染时，白细胞的反应性会增强，是身体对抗感染和炎症的一种自然反应。</SOLUTION>
```

## Example 2: Bacterial Meningitis
### Input:

```
背景:19岁男性，大学生，因“高热、剧烈头痛伴呕吐12小时”就诊急诊。关键病史:症状发展迅速，数小时内出现全脑炸裂样头痛，伴畏光、精神萎靡。既往健康，无外伤史。
核心体征与化验:体征:生命体征: T 39.8°C, P 115次/分, BP 110/70 mmHg。神志嗜睡，定向力差。
皮肤可见散在瘀点、瘀斑。颈部抵抗明显 (颈强直)，克氏征(+)。辅助检查:头颅CT平扫: 未见异常。
腰椎穿刺脑脊液 (CSF) 检查:外观: 脓性、浑浊压力: 310 mmH₂O (增高)白细胞: 2500 x 10⁶/L (显著增高)分类: 中性粒细胞 95%糖: 1.2 mmol/L (同步指尖血糖 8.0 mmol/L)蛋白: 2.5 g/L (显著增高)
问题1: 该患者最可能的诊断是什么？
问题2: 诊断的最关键实验室检查是哪一项？请解读其支持诊断的四个典型改变。
问题3: 根据患者的年龄和皮肤表现（瘀点、瘀斑），最可能的可疑病原体是哪一种？
问题4: 对于这类危重患者，在临床高度怀疑诊断但正在等待脑脊液结果时，最关键的治疗决策是什么？<start_working_out>
```
### Model Output:
```
患者是个19岁的年轻男性，症状包括高热、剧烈头痛、呕吐，这些都在短时间内急剧加重，他有全脑炸裂样的头痛，还怕光，精神状态也差。他的皮肤上出现了瘀点和瘀斑，这让我立刻想到了可能的感染，特别是败血症。
生命体征显示他的体温很高，心率快，血压虽然不高，但整体状况确实让人担心。皮肤上的瘀点和瘀斑提示他可能有凝血功能障碍，这在败血症中也很常见。
脑脊液检查的结果非常关键。CSF是脓性的、浑浊，压力高，白细胞显著增加，以中性粒细胞为主，糖含量低而蛋白增高，这些都指向了细菌性脑膜炎。而这些症状和化验结果的组合让我更倾向于细菌性感染。
患者年龄是19岁，而皮肤上的瘀点、瘀斑让我想到常见的败血症病原体。对于年轻人，尤其是有过这些皮肤表现的，脑膜炎球菌是最常见的嫌疑犯。
在临床高度怀疑细菌性脑膜炎时，即使等脑脊液结果，最紧急的措施是使用经验性抗生素。这样可以迅速控制感染，防止病情恶化。在等结果的同时，给予抗生素是必要的，因为如果不及时，可能危及生命。
总结来说，这位患者最可能的诊断是细菌性脑膜炎，而脑膜炎球菌是最可疑的病原体。在临床高度怀疑的情况下，立即给予抗生素治疗是最关键的决定。<end_working_out>
<SOLUTION>
问题1: 该患者最可能的诊断是细菌性脑膜炎。
问题2: 诊断的最关键实验室检查是脑脊液检查。其支持诊断的四个典型改变包括：
1. 脑脊液外观呈脓性、浑浊，提示有感染。
2. 脑脊液压力增高，通常表明存在炎症或感染。
3. 白细胞显著增高，尤其是以中性粒细胞为主，常见于细菌感染。
4. 脑脊液中的糖含量降低，而蛋白增高，这是细菌性脑膜炎的典型特征。
问题3: 根据患者的年龄和皮肤表现（瘀点、瘀斑），最可能的可疑病原体是脑膜炎球菌。
问题4: 对于这类危重患者，在临床高度怀疑诊断但正在等待脑脊液结果时，最关键的治疗决策是立即给予经验性抗生素治疗，以迅速控制感染并防止病情恶化。</SOLUTION>
```

# Disclaimer
This model is fine-tuned from a large language model and is intended for academic research and technical communication purposes only. 
Any medical information, analysis, or suggestions provided by the model's output may contain errors, omissions, or inaccuracies and cannot replace the diagnosis and 
advice of licensed physicians, pharmacists, or other professional medical personnel.Do not use the output of this model as a basis for clinical decisions. 
Before making any medical decisions, be sure to consult a qualified professional healthcare provider. 
The author assumes no responsibility for any direct or indirect loss or damage resulting from the use of this model.

# Citation
```
@software{tang_2025_qwen3_medical_grpo,
  author = {TANG ZHI XIONG},
  title = {{Qwen3_Medical_GRPO: A Medical Domain LLM fine-tuned with Group Relative Policy Optimization}},
  month = jun,
  year = 2025,
  publisher = {Hugging Face},
  version = {1.0},
  url = {[https://huggingface.co/lastmass/Qwen3_Medical_GRPO](https://huggingface.co/lastmass/Qwen3_Medical_GRPO)}
}
```

# Uploaded finetuned  model

- **Developed by:** lastmass
- **License:** apache-2.0
- **Finetuned from model :** unsloth/Qwen3-4B-Base

This qwen3 model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)
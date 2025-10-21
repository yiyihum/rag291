---
license: mit
pipeline_tag: text-generation
library_name: transformers
---

# Apriel-Nemotron-15b-Thinker

<img src="https://cdn-uploads.huggingface.co/production/uploads/63d3095c2727d7888cbb54e2/Lt1t0tOO5emz1X23Azg-E.png" width="120" alt="thumbnail"/>      `/ˈɑː.pri.əl/`

---

## Table of Contents

1. [Summary](#summary)  
2. [Evaluation](#evaluation)  
3. [Training Details](#training-details)  
4. [How to Use](#how-to-use) 
5. [Intended Use](#intended-use)  
6. [Limitations](#limitations)  
7. [Security and Responsible Use](#security-and-responsible-use)  
8. [Software](#software)  
9. [License](#license)
10. [Acknowledgements](#acknowledgements)
11. [Citation](#citation)  


---

## Summary

**Apriel-Nemotron-15b-Thinker** is a 15 billion‑parameter reasoning model in ServiceNow’s Apriel SLM series which achieves competitive performance against similarly sized state-of-the-art models like o1‑mini, QWQ‑32b, and EXAONE‑Deep‑32b, all while maintaining only half the memory footprint of those alternatives. It builds upon the **Apriel‑15b‑base** checkpoint through a three‑stage training pipeline (CPT, SFT and GRPO).

**Highlights**
- Half the size of SOTA models like QWQ-32b and EXAONE-32b and hence **memory efficient**.
- It consumes **40%** less tokens compared to QWQ-32b, making it super efficient in production. 🚀🚀🚀
- On par or outperforms on tasks like - MBPP, BFCL, Enterprise RAG, MT Bench, MixEval, IFEval and Multi-Challenge making it great for **Agentic / Enterprise tasks**.
- Competitive performance on academic benchmarks like AIME-24 AIME-25, AMC-23, MATH-500 and GPQA considering model size.

---

## Evaluation

Evaluations were conducted using [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness) and [evalchemy](https://github.com/mlfoundations/evalchemy).



### Benchmarks that are indicative of enterprise capability
![image/png](https://cdn-uploads.huggingface.co/production/uploads/63d3095c2727d7888cbb54e2/ih9QGdnSq20MLCGGtsAZL.png)



### Academic reasoning benchmarks
![image/png](https://cdn-uploads.huggingface.co/production/uploads/63d3095c2727d7888cbb54e2/psk628cePXQZ9AghKuI5u.png)



### Token efficiency comparison (lower the better)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/63d3095c2727d7888cbb54e2/jmvBwsJAIZVTP0xtWSTIz.png)


---


## Training Details

**Mid training / Continual Pre‑training**
In this stage, the model is trained on 100+ billion tokens of carefully curated examples drawn from mathematical reasoning, coding challenges, scientific discourse and logical puzzles. The objective is to strengthen foundational reasoning capabilities of the model. This stage is super critical for the model to function as a reasoner and provides significant lifts in reasoning benchmarks.

**Supervised Fine‑Tuning (SFT)**
Next, we SFT the model using 200,000 high‑quality demonstrations that cover mathematical and scientific problem‑solving, coding tasks, generic instruction‑following scenarios, API/function invocation use cases etc.

**Reinforcement Learning**
Although the SFT‑tuned checkpoint delivers strong performance on core competencies like mathematics and general knowledge, it exhibits weaknesses in instruction following and coding tasks. To address these gaps, we apply GRPO (with some minor modifications to the objective). The result is significant improvement on benchmarks such as IFEval, Multi Challenge, Enterprise RAG, MBPP and BFCL, while preserving scores on competition‑level math exams like AIME and AMC. GRPO also yields modest gains on GPQA and MixEval.

Throughout training, intermediate snapshots from both the SFT and GRPO stages are periodically merged, improving generalization and catastrophic forgetting.

*Technical report with more details - coming soon.*

---


## How to Use

```bash
pip install transformers
```

---

### Running the Reasoning model


Here is a code snippet demonstrating the model's usage with the transformers library's generate function:

```python
import re
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "ServiceNow-AI/Apriel-Nemotron-15b-Thinker"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# prepare the model input
prompt = "Positive real numbers $x$ and $y$ satisfy $y^3=x^2$ and $(y-x)^2=4y^2$. What is $x+y$?\nMark your solution with \\boxed"
messages = [
    {"role": "user", "content": prompt}
]

tools = []

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    tools=tools
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=65536
)
output = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

# parsing the response
response = re.findall(r"\[BEGIN FINAL RESPONSE\](.*?)\[END FINAL RESPONSE\]", output, re.DOTALL)[0].strip()
print("output:", output)
print("response:", response)
```
---

### Chat Template


```
<|system|>
You are a thoughtful and systematic AI assistant built by ServiceNow Language Models (SLAM) lab. Before providing an answer, analyze the problem carefully and present your reasoning step by step. After explaining your thought process, provide the final solution in the following format: [BEGIN FINAL RESPONSE] ... [END FINAL RESPONSE].
<|end|>
<|user|>
# user message here
<|end|>
<|assistant|>
Here are my reasoning steps:
# thoughts here
[BEGIN FINAL RESPONSE]
# assistant response here
[END FINAL RESPONSE]
<|end|>
```
The model will first generate its thinking process and then generate its final response between `[BEGIN FINAL RESPONSE]` and `[END FINAL RESPONSE]`. Here is a code snippet demonstrating the application of the chat template:



```python
from transformers import AutoTokenizer
model_name = "ServiceNow-AI/Apriel-Nemotron-15b-Thinker"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# prepare the model input
custom_system_prompt = "Answer like a pirate."
prompt = "You are an expert assistant in the implementation of customer experience management aspect of retail applications \n \nYou will be using Python as the programming language. \n \nYou will utilize a factory design pattern for the implementation and following the dependency inversion principle \n \nYou will modify the implementation based on user requirements. \n \nUpon user request, you will add, update, and remove the features & enhancements in the implementation provided by you. \n \nYou will ask whether the user wants to refactor the provided code or needs a sample implementation for reference. Upon user confirmation, I will proceed accordingly. \n \n**Guidelines:** \n 1. **User Requirements:** \n - You have to ask users about their requirements, clarify the user expectations, and suggest the best possible solution by providing examples of Python code snippets. \n - Ask users about which type of reports they need to assess the AI model's performance, accuracy, and reliability. \n - After providing the solution, you have to ask the user about the trial of the solution and modify the solution based on the user feedback. \n \n 2. **Libraries/Frameworks:** \n - You will be utilizing Python as a programming language. \n - You will be using Flask framework for REST APIS implementation \n \n 3. **Communication Gesture:** \n - Your conversation with the user should be interactive, supportive, courageous, and professional. \n - You have to break down the complex concepts into sub-concepts and try to explain them to the user. \n - You have to ask the user for the required parameters. If the user refuses to provide in 2 attempts, politely exit the conversation. \n - You have to provide your supported parameters to the user, if the user refuses to accept them then you have to put an apology note and exit the conversation. \n - You have to track the conversation about unasked questions by the user. If some/one of the questions remain then you have to remind the user about these questions and proceed to answer them based on the user's confirmation \n \n 4. **Implementation:** \n - Your code/implementations should be reliable, scaleable, modular, and reusable. \n - You will be providing unit tests for the implementation upon user request. \n - You will be following MVC architecture for the applications \n - Your implementations must be well-commented and readable \n \n \n- Today's date is 23rd August 2024. \n- The default sender email is sender-assistant@email.com.\nHi, I am conducting research on retail customer feedback systems and I need assistance with designing and implementing them. Could you kindly provide me with a list of general customer feedback system modules?"
messages = [
    {"role": "user", "content": custom_system_prompt + "\n\n" + prompt}
]
# example tools
tools = [{"type": "function", "function": {"name": "getRetailFeedbackModules", "description": "Returns the list of modules usually present in the retail industry", "parameters": {"type": "object", "properties": {"page": {"type": "integer", "description": "The current page number.", "default": 1}, "page_size": {"type": "integer", "description": "The number of items per page.", "default": 3}}}}}, {"type": "function", "function": {"name": "verifyImplementation", "description": "Returns the list of modules usually present in the retail industry", "parameters": {"type": "object", "properties": {"coding_language": {"type": "string", "description": "The supported languages for verification of implementation.", "default": "python", "enum": ["python", "java", "php"]}, "code": {"type": "string", "description": "The code which needs verification"}, "design_pattern": {"type": "string", "description": "The design pattern to verify in the implementation", "enum": ["factory", "strategy", "singleton"]}, "verify_best_practices": {"type": "boolean", "description": "The verification of the coding style based on the language selected", "default": true}}}}}]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    tools=tools
)
model_inputs = tokenizer([text], return_tensors="pt")
```

### Usage Guidelines
1. Use the model’s default chat template, which already includes a system prompt. We recommend adding all other instructions within the user message. 
2. We recommend setting temperature to `0.6`. 
3. We ensure the model starts with `Here are my reasoning steps:\n` during all our evaluations. This is implemented in the default chat template. 

---


## Intended Use

The Apriel family of models are designed for a variety of general-purpose instruction tasks, including:

- Code assistance and generation  
- Logical reasoning and multi-step tasks  
- Question answering and information retrieval
- Function calling, complex instruction following and agent use cases

They are **not intended** for use in safety-critical applications without human oversight or in scenarios requiring guaranteed factual accuracy.

---

## Limitations

- **Factual accuracy:** May produce incorrect, misleading, or outdated content. Outputs should be verified before use in critical contexts.  
- **Bias:** May reflect societal, cultural, or systemic biases present in training data.  
- **Ethics:** Do not use the model to produce harmful, unlawful, or unethical content.  
- **Language:** Strongest performance is in English. Output quality may degrade in underrepresented languages.  
- **Critical use:** Not suitable for medical, legal, financial, or other high-risk applications without safeguards.

---

## Security and Responsible Use

**Security Responsibilities:**  
Deployers and users are strongly encouraged to align their security practices with established frameworks and regulatory guidelines such as the EU AI Act and the NIST AI Risk Management Framework (RMF).

**Guidelines for Deployers:**

- Regularly conduct robustness assessments to identify and mitigate adversarial inputs.
- Implement validation and filtering processes to prevent harmful or biased outputs.
- Continuously perform data privacy checks to guard against unintended data leaks.
- Document and communicate the model's limitations, intended usage, and known security risks to all end-users.
- Schedule periodic security reviews and updates to address emerging threats and vulnerabilities.

**Guidelines for Users:**

- Follow established security policies and usage guidelines provided by deployers.
- Protect and manage sensitive information when interacting with the model.
- Report anomalies, suspicious behavior, or unsafe outputs to deployers or developers.
- Maintain human oversight and apply judgment to mitigate potential security or ethical risks during interactions.

**Disclaimer:**  
Users accept responsibility for securely deploying, managing, and using this open-source LLM. The model is provided "as-is," without explicit or implied warranty regarding security or fitness for any specific application or environment.

---

## Software

- **Training stack:** [Fast-LLM](https://github.com/ServiceNow/Fast-LLM)

---

## License

MIT

---

## Acknowledgments

>We thank researchers at Nvidia for sharing detailed insights and data from their work in building reasoners! This greatly accelerated our research and we recognize the same with our model naming convention!

## Citation

```bibtex
@misc{Apriel-nemotron-15b-thinker,  
    author = {Slam labs team},  
    title = {Apriel Nemotron 15b Thinker},  
    howpublished = {https://huggingface.co/ServiceNow-AI/Apriel-Nemotron-15b-Thinker},
    publisher = {SLAM - ServiceNow Language Models Lab}  
    year = {2025}
}
```
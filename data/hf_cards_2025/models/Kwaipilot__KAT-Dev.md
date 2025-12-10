---
language:
- multilingual
license: apache-2.0
license_name: kwaipilot-license
license_link: LICENSE
library_name: transformers
---
<div align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/61ee40a269351366e29972ad/KIYEa1c_WJEWPpeS0L_k1.png" width="100%" alt="Kwaipilot" />
</div>

<hr>


# News

🔥 We’re thrilled to announce the release of KAT-Dev-72B-Exp, our latest and most powerful model yet!

🔥 You can now try our **strongest** proprietary coder model **KAT-Coder** directly on the [StreamLake](https://www.streamlake.ai/product/kat-coder) platform **for free**.

# Highlights
**KAT-Dev-32B**  is an open-source 32B-parameter model for software engineering tasks.

On SWE-Bench Verified, **KAT-Dev-32B** achieves comparable performance with **62.4%** resolved and ranks **5th** among all open-source models with different scales.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61ee40a269351366e29972ad/dTpQQPQnp1TdD4YB8gZAu.png)

# Introduction

**KAT-Dev-32B** is optimized via several stages of training, including a mid-training stage, supervised fine-tuning (SFT) & reinforcement fine-tuning (RFT) stage and an large-scale agentic reinforcement learning (RL) stage. In summary, our contributions include:
 
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:18%;">Stage</th>
      <th style="text-align:left;">Key Techniques</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Mid-Training</strong></td>
      <td>We observe that adding extensive training for tool-use capability, multi-turn interaction, and instruction-following at this stage may not yield large performance gains in the current results (e.g., on leaderboards like SWE-bench). However, since our experiments are based on the Qwen3-32B model, we find that enhancing these foundational capabilities will have a significant impact on the subsequent SFT and RL stages. This suggests that improving such core abilities can profoundly influence the model’s capacity to handle more complex tasks.
</td>
    </tr>
    <tr>
      <td><strong>2. SFT & RFT</strong></td>
      <td>We meticulously curated eight task types and eight programming scenarios during the SFT stage to ensure the model’s generalization and comprehensive capabilities. Moreover, before RL, we innovatively introduced an RFT stage. Compared with traditional RL, we incorporate “teacher trajectories” annotated by human engineers as guidance during training—much like a learner driver being assisted by an experienced co-driver before officially driving after getting a license. This step not only boosts model performance but also further stabilizes the subsequent RL training.
</td>
    </tr>
    <tr>
      <td><strong>3. Agentic RL Scaling</strong></td>
      <td>Scaling agentic RL hinges on three challenges: efficient learning over nonlinear trajectory histories, leveraging intrinsic model signals, and building scalable high-throughput infrastructure. We address these with a multi-level prefix caching mechanism in the RL training engine, an entropy-based trajectory pruning technique, and an inner implementation of SeamlessFlow[1] architecture that cleanly decouples agents from training while exploiting heterogeneous compute. These innovations together cut scaling costs and enable efficient large-scale RL.
</td>
    </tr>
  </tbody>
</table>

For more details, including benchmark evaluation, hardware requirements, and inference performance, please refer to our [blog](https://kwaipilot.github.io/KAT-Coder/).

# Quickstart

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Kwaipilot/KAT-Dev"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# prepare the model input
prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=65536
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

content = tokenizer.decode(output_ids, skip_special_tokens=True)

print("content:", content)
```

## Claude Code
 ### vllm server
```
MODEL_PATH="Kwaipilot/KAT-Dev"

vllm serve $MODEL_PATH \
      --enable-prefix-caching \
      --tensor-parallel-size 8 \
      --tool-parser-plugin $MODEL_PATH/qwen3coder_tool_parser.py \
      --chat-template $MODEL_PATH/chat_template.jinja \
      --enable-auto-tool-choice --tool-call-parser qwen3_coder
```

[claude-code-router](https://github.com/musistudio/claude-code-router) is a third-party routing utility that allows Claude Code to flexibly switch between different backend APIs.  
On the dashScope platform, you can install the **claude-code-config** extension package, which automatically generates a default configuration for `claude-code-router` with built-in dashScope support.

Once the configuration files and plugin directory are generated, the environment required by `ccr` will be ready.  
If needed, you can still manually edit `~/.claude-code-router/config.json` and the files under `~/.claude-code-router/plugins/` to customize the setup.

Finally, simply start `ccr` to run Claude Code and seamlessly connect it with the powerful coding capabilities of **KAT-Dev-32B**.  
Happy coding!

# CONNECT US


![image](https://cdn-uploads.huggingface.co/production/uploads/61ee40a269351366e29972ad/dEvTOCsumOvIJCJQnFKv-.png)

Here’s the QR code for our WeChat group — feel free to join and chat with us!
---
license: mit
pipeline_tag: text-generation
---


<p align="center">
    <img src="https://mdn.alipayobjects.com/huamei_qa8qxu/afts/img/A*4QxcQrBlTiAAAAAAQXAAAAgAemJ7AQ/original" width="100"/>
</p>

<p align="center">🤗 <a href="https://huggingface.co/inclusionAI">Hugging Face</a>&nbsp;&nbsp; | &nbsp;&nbsp;🤖 <a href="https://modelscope.cn/organization/inclusionAI">ModelScope </a>&nbsp;&nbsp; | &nbsp;&nbsp;🐙 <a href="https://zenmux.ai/inclusionai/ring-1t?utm_source=hf_inclusionAI">Experience Now</a></p>

# Ring-1T, flow state leads to sudden enlightenment

Today, we officially launch the trillion-parameter thinking model, Ring-1T. It is open-source upon release—developers can download the model weights from Hugging Face and ModelScope, or experience direct chat interactions and API calls via the Ling Chat page and ZenMux (links provided at the end of the article).

Building upon the preview version released at the end of last month, Ring-1T has undergone continued scaling with large-scale verifiable reward reinforcement learning (RLVR) training, further unlocking the natural language reasoning capabilities of the trillion-parameter foundation model. Through RLHF training, the model's general abilities have also been refined, making this release of Ring-1T more balanced in performance across various tasks.

Ring-1T adopts the Ling 2.0 architecture and is trained on the Ling-1T-base foundation model, which contains 1 trillion total parameters with 50 billion activated parameters, supporting a context window of up to 128K tokens. Leveraging our self-developed icepop reinforcement learning stabilization method and the efficient reinforcement learning system ASystem (whose AReaL framework is already open-source), we have achieved smooth scaling of MoE architecture reinforcement learning—from tens of billions (Ring-mini-2.0) to hundreds of billions (Ring-flash-2.0) to trillions (Ring-1T) of parameters—significantly enhancing the model's deep reasoning and natural language inference capabilities.

## Model Downloads

You can download Ring-1T from the following table. If you are located in mainland China, we also provide the model on ModelScope to speed up the download process.

<center>

| **Model** | **Context Length** |                                                                 **Download**                                                                  |
| :-------: | :----------------: | :-------------------------------------------------------------------------------------------------------------------------------------------: |
|  Ring-1T  | 64K -> 128K (YaRN) | [🤗 HuggingFace](https://huggingface.co/inclusionAI/Ring-1T) &nbsp;&nbsp; [🤖 ModelScope](https://www.modelscope.cn/models/inclusionAI/Ring-1T) |
|  Ring-1T-FP8  | 64K -> 128K (YaRN) | [🤗 HuggingFace](https://huggingface.co/inclusionAI/Ring-1T-FP8) &nbsp;&nbsp; [🤖 ModelScope](https://www.modelscope.cn/models/inclusionAI/Ring-1T-FP8) |
</center>

Note: If you are interested in previous version, please visit the past model collections in [Huggingface](https://huggingface.co/inclusionAI) or [ModelScope](https://modelscope.cn/organization/inclusionAI).


## Continuously Evolving Deep Reasoning Capabilities

To evaluate the deep reasoning capabilities of Ring-1T, we selected representative open-source thinking models (Ring-1T-preview, Deepseek-V3.1-Terminus-Thinking, Qwen-235B-A22B-Thinking-2507) and closed-source APIs (Gemini-2.5-Pro and GPT-5-Thinking(High)) as benchmarks. First, compared to the previously open-sourced preview version, Ring-1T demonstrates more balanced performance across various tasks. Furthermore, Ring-1T achieves open-source leading performance on challenging reasoning benchmarks such as **math competitions** (AIME 25, HMMT 25), **code generation** (LiveCodeBench, CodeForce), and **logical reasoning** (ARC-AGI-1). It also exhibits strong competitiveness in **comprehensive tasks** (Arena-Hard-v2.0), **healthcare** (HealthBench), and **creative writing** (Creative Writing v3).

<p align="center">
    <img src="https://mdn.alipayobjects.com/huamei_d2byvp/afts/img/5TBESJNjsbAAAAAAYYAAAAgADod9AQFr/original" />
</p>

Although we have implemented string-level and semantic-level contamination filtering for benchmark tasks across all training stages—including pre-training, fine-tuning instructions, and reinforcement learning prompts—rigorous decontamination for earlier published benchmarks remains a significant challenge in the industry. To more objectively analyze Ring-1T's deep reasoning capabilities, we conducted tests using the IMO 2025 (International Mathematical Olympiad) held in July this year and the recently concluded ICPC World Finals 2025 (International Collegiate Programming Contest World Finals).

For the **IMO 2025** test, similar to the previous preview version, we integrated Ring-1T into the multi-agent framework AWorld (https://github.com/inclusionAI/AWorld) and used pure natural language reasoning to solve the problems. The results show that Ring-1T solved Problems 1, 3, 4, and 5 in a single attempt (silver medal level at IMO). On the third attempt, it also produced a nearly perfect proof for Problem 2, a geometry proof. For the most challenging Problem 6 (which no AI contestant in IMO 2025 solved correctly), Ring-1T converged to the same answer as Gemini 2.5 Pro—"4048" (the correct answer is 2112). We believe that with ongoing optimizations, Ring-1T has the potential to reach gold medal level at IMO in a single attempt in the future.

<p align="center">
    <img src="https://mdn.alipayobjects.com/huamei_d2byvp/afts/img/mnRJTa5a00gAAAAAQ2AAAAgADod9AQFr/original" width="500"/>
</p>

<p align="center">
    <img src="https://mdn.alipayobjects.com/huamei_d2byvp/afts/img/C2KTQrsZjcQAAAAASiAAAAgADod9AQFr/original" width="500" />
</p>

<p align="center">
    <img src="https://mdn.alipayobjects.com/huamei_d2byvp/afts/img/kClfSJ9T6JIAAAAAQkAAAAgADod9AQFr/original" width="500" />
</p>

<p align="center">
    <img src="https://mdn.alipayobjects.com/huamei_d2byvp/afts/img/ctNBSp0CifsAAAAAR5AAAAgADod9AQFr/original" width="500" />
</p>

<p align="center">
    <img src="https://mdn.alipayobjects.com/huamei_d2byvp/afts/img/oDFIRr9agCUAAAAAR-AAAAgADod9AQFr/original" width="500" />
</p>

At the ICPC World Finals 2025, we compared GPT-5-Thinking, Gemini-2.5-Pro, and Ring-1T. In a test allowing three attempts for direct problem-solving by the models, they solved 6 (problems CDEFKL), 3 (problems DFK), and 5 (problems DFJKL) problems, respectively. The results demonstrate that Ring-1T also delivers outstanding performance in top-tier international programming competitions. Further testing is ongoing, and we will also open-source the solution traces of the models for the aforementioned competitions (IMO traces are provided at the end of the article). We look forward to collaborating with the community to further optimize the reasoning potential of this trillion-parameter thinking model.

## Icepop: Ensuring Stable Reinforcement Learning Through Long-Term Training

In the reinforcement learning training of MoE models, the discrepancies in operator implementations between the training and inference engines are more pronounced compared to dense models. This divergence becomes increasingly significant as sequence length and training steps accumulate, particularly during long-sequence generation and extended training cycles. As illustrated in the experiment below, the original GRPO algorithm begins to collapse after relatively few training steps. In contrast, our proposed Icepop algorithm mitigates this issue by correcting distributions through masked bidirectional truncation technology, effectively reducing the gap between training and inference phases—thereby "cooling down" the rapidly escalating training-inference discrepancy.

<p align="center">
    <img src="https://mdn.alipayobjects.com/huamei_d2byvp/afts/img/D1jaRoB7D4kAAAAAT6AAAAgADod9AQFr/original" width="500" />
</p>

Figure 1: The training-inference discrepancy of GRPO increases exponentially with training, while Icepop remains relatively stable.

<p align="center">
    <img src="https://mdn.alipayobjects.com/huamei_d2byvp/afts/img/9BqKQ7E46j0AAAAATLAAAAgADod9AQFr/original" width="500" />
</p>

Figure 2: Maximum training-inference discrepancy—GRPO shows a significant rise with training, whereas Icepop maintains a low level.

## Asystem: In-House RL Framework "Mastering" Trillion-Scale Training

To ensure stable and efficient reinforcement learning training for trillion-parameter foundation models, we independently developed a high-performance reinforcement learning system—ASystem. ASystem adopts a SingleController + SPMD architecture. In terms of training and inference engines, it has been meticulously optimized to address memory management and weight exchange challenges specific to trillion-parameter models. Leveraging our self-developed unified memory pool technology for training and inference, it achieves transparent memory offloading, efficiently releases memory fragmentation, and reduces the risk of insufficient memory. Through techniques such as direct P2P communication between GPUs and in-place updates, it enables second-level, zero-redundant model weight exchange.

For the RL training framework, we built a hybrid reward system based on large-scale Serverless Sandbox technology. This system can start up in milliseconds, supports execution environments for over 10 programming languages, and handles request throughput of up to 10K/s. We have open-sourced AReaL and hope to accelerate RL training and research in the open-source community through technological openness.


## Quickstart

### 🚀 Try Online

You can experience Ring-1T online at: [ZenMux](https://zenmux.ai/inclusionai/ring-1t?utm_source=hf_inclusionAI)

### 🔌 API Usage

You can also use Ring-1T through API calls:

```python   
from openai import OpenAI

# 1. Initialize the OpenAI client
client = OpenAI(
    # 2. Point the base URL to the ZenMux endpoint
    base_url="https://zenmux.ai/api/v1",
    # 3. Replace with the API Key from your ZenMux user console
    api_key="<your ZENMUX_API_KEY>",
)

# 4. Make a request
completion = client.chat.completions.create(
    # 5. Specify the model to use in the format "provider/model-name"
    model="inclusionai/ring-1t",
    messages=[
        {
            "role": "user",
            "content": "What is the meaning of life?"
        }
    ]
)

print(completion.choices[0].message.content)
```


## Deployment

### SGLang

#### Environment Preparation

We will later submit our model to the SGLang official release. Now we can prepare the environment by following these steps:
```shell
pip3 install -U sglang sgl-kernel
```

#### Run Inference

Both BF16 and FP8 models are supported by SGLang now. It depends on the dtype of the model in ${MODEL_PATH}.

Here is the example to run Ring-1T with multiple GPU nodes, where the master node IP is ${MASTER_IP} and server port is ${PORT}:

- Start server:
```bash
# Node 0:
python -m sglang.launch_server --model-path $MODEL_PATH --tp-size 8 --pp-size 4 --dp-size 1 --trust-remote-code --dist-init-addr $MASTER_IP:2345 --port $PORT --nnodes 4 --node-rank 0 

# Node 1:
python -m sglang.launch_server --model-path $MODEL_PATH --tp-size 8 --pp-size 4 --dp-size 1 --trust-remote-code --dist-init-addr $MASTER_IP:2345 --port $PORT --nnodes 4 --node-rank 1 

# Node 2:
python -m sglang.launch_server --model-path $MODEL_PATH --tp-size 8 --pp-size 4 --dp-size 1 --trust-remote-code --dist-init-addr $MASTER_IP:2345 --port $PORT --nnodes 4 --node-rank 2 

# Node 3:
python -m sglang.launch_server --model-path $MODEL_PATH --tp-size 8 --pp-size 4 --dp-size 1 --trust-remote-code --dist-init-addr $MASTER_IP:2345 --port $PORT --nnodes 4 --node-rank 3

# This is only an example. Please adjust arguments according to your actual environment.
```

- Client:

```shell
curl -s http://${MASTER_IP}:${PORT}/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "auto", "messages": [{"role": "user", "content": "What is the capital of France?"}]}'
```

More usage can be found [here](https://docs.sglang.ai/basic_usage/send_request.html)

### vLLM

For latest guidance, please refer to the vLLM [`instructions`](https://docs.vllm.ai/projects/recipes/en/latest/inclusionAI/Ring-1T-FP8.html).

#### Environment Preparation

```bash
pip install vllm==0.11.0
```

#### Run Inference:

Here is the example to deploy the model with multiple GPU nodes, where the master node IP is ${MASTER_IP}, server port is ${PORT} and the path of model is ${MODEL_PATH}:

```bash
# step 1. start ray on all nodes

# step 2. start vllm server only on node 0:
vllm serve $MODEL_PATH --port $PORT --served-model-name my_model --trust-remote-code --tensor-parallel-size 8 --pipeline-parallel-size 4 --gpu-memory-utilization 0.85


# This is only an example, please adjust arguments according to your actual environment.
```

To handle long context in vLLM using YaRN, we need to follow these two steps:
1. Add a `rope_scaling` field to the model's `config.json` file, for example:
```json
{
  ...,
  "rope_scaling": {
    "factor": 4.0,
    "original_max_position_embeddings": 32768,
    "type": "yarn"
  }
}
```
2. Use an additional parameter `--max-model-len` to specify the desired maximum context length when starting the vLLM service.


## Finetuning

We recommend you to use [Llama-Factory](https://github.com/hiyouga/LLaMA-Factory) to [finetune Ring](https://github.com/inclusionAI/Ring-V2/blob/main/docs/llamafactory_finetuning.md).

## Limitations and Future Plans

Ring-1T represents the Bailing team’s first attempt at developing a trillion-scale deep thinking model. The current version may occasionally exhibit issues such as identity recognition bias, language mixing, and repetitive generation. Additionally, since its attention architecture still adopts the GQA approach from Ling 2.0, there remains room for improvement in inference efficiency under long-context scenarios.

We will continue to optimize these aspects in future releases and highly welcome feedback from the community. Furthermore, training for Ring-1T is still ongoing. We are committed to further unlocking the reasoning potential of this trillion-parameter foundation model and look forward to sharing more mature upgraded versions with everyone as soon as possible.

Welcome to visit our open-source repository and demo page for download and usage.

Hugging Face: [https://huggingface.co/inclusionAI/Ring-1T](https://huggingface.co/inclusionAI/Ring-1T)

ModelScope: [https://modelscope.cn/models/inclusionAI/Ring-1T](https://modelscope.cn/models/inclusionAI/Ring-1T)

Ling Chat (for Chinese users): [https://ling.tbox.cn/chat](https://ling.tbox.cn/chat)

ZenMux (for overseas developers, offering Chat testing and API capabilities): [https://zenmux.ai/inclusionai/ring-1t?utm_source=hf_inclusionAI](https://zenmux.ai/inclusionai/ring-1t?utm_source=hf_inclusionAI)

Ring-1T@Aworld IMO test trajectory: [https://github.com/inclusionAI/AWorld/tree/main/examples/imo/samples/samples%20from%20Ring-1T](https://github.com/inclusionAI/AWorld/tree/main/examples/imo/samples/samples%20from%20Ring-1T)

## License

This code repository is licensed under [the MIT License](https://github.com/inclusionAI/Ring-V2/blob/master/LICENSE).
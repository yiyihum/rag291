---
language:
- en
- fr
- de
- es
- pt
- it
- ja
- ko
- ru
- zh
- ar
- fa
- id
- ms
- ne
- pl
- ro
- sr
- sv
- tr
- uk
- vi
- hi
- bn
license: apache-2.0
library_name: llama.cpp
inference: false
base_model:
- mistralai/Devstral-Small-2507
extra_gated_description: If you want to learn more about how we process your personal
  data, please read our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
pipeline_tag: text-generation
---


> [!Note]
> At Mistral, we don't yet have too much experience with providing GGUF-quantized checkpoints
> to the community, but want to help improving the ecosystem going forward.
> If you encounter any problems with the provided checkpoints here, please open a discussion or pull request


# Devstral Small 1.1 (gguf)

Devstral is an agentic LLM for software engineering tasks built under a collaboration between [Mistral AI](https://mistral.ai/) and [All Hands AI](https://www.all-hands.dev/) 🙌. Devstral excels at using tools to explore codebases, editing multiple files and power software engineering agents. The model achieves remarkable performance on SWE-bench which positions it as the #1 open source model on this [benchmark](https://huggingface.co/mistralai/Devstral-Small-2507#benchmark-results).

This is the GGUF version of the [Devstral-Small-2507](https://huggingface.co/mistralai/Devstral-Small-2507) model. We released the BF16 weights as well as the following quantized format:
- Q8_0
- Q5_K_M
- Q4_K_M

It is finetuned from [Mistral-Small-3.1](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Base-2503), therefore it has a long context window of up to 128k tokens. As a coding agent, Devstral is text-only and before fine-tuning from `Mistral-Small-3.1` the vision encoder was removed.

For enterprises requiring specialized capabilities (increased context, domain-specific knowledge, etc.), we will release commercial models beyond what Mistral AI contributes to the community.

Learn more about Devstral in our [blog post](https://mistral.ai/news/devstral-2507).

**Updates compared to [`Devstral Small 1.0`](https://huggingface.co/mistralai/Devstral-Small-2505):**
- The performance has been increased, please refer to the [benchmark results](https://huggingface.co/mistralai/Devstral-Small-2507#benchmark-results).
- `Devstral Small 1.1` is still great when paired with OpenHands. This new version also generalizes better to other prompts and coding environments.
- Supports [Mistral's function calling format](https://mistralai.github.io/mistral-common/usage/tools/).


## Key Features:
- **Agentic coding**: Devstral is designed to excel at agentic coding tasks, making it a great choice for software engineering agents.
- **lightweight**: with its compact size of just 24 billion parameters, Devstral is light enough to run on a single RTX 4090 or a Mac with 32GB RAM, making it an appropriate model for local deployment and on-device use.
- **Apache 2.0 License**: Open license allowing usage and modification for both commercial and non-commercial purposes.
- **Context Window**: A 128k context window.
- **Tokenizer**: Utilizes a Tekken tokenizer with a 131k vocabulary size.

## Usage

We recommend to use Devstral with the [OpenHands](https://github.com/All-Hands-AI/OpenHands/tree/main) scaffold as explained [here](https://huggingface.co/mistralai/Devstral-Small-2507#usage).
To use it local with a GGUF-quantized checkpoint, see the following section.

### Local inference (GGUF)

Download the weights from huggingface:

```sh
pip install -U "huggingface_hub[cli]"
huggingface-cli download \
"mistralai/Devstral-Small-2507_gguf" \
--include "Devstral-Small-2507-Q4_K_M.gguf" \
--local-dir "mistralai/Devstral-Small-2507_gguf/"
```

#### llama.cpp

Download the weights from huggingface and then run Devstral using the llama.cpp CLI or llama.cpp server:

```sh
./llama-cli -m mistralai/Devstral-Small-2507_gguf/Devstral-Small-2507-Q4_K_M.gguf -cnv
```

```sh
./llama-server -m mistralai/Devstral-Small-2507_gguf/Devstral-Small-2507-Q4_K_M.gguf -c 0
```

#### LM Studio

You can serve the model locally with [LM Studio](https://lmstudio.ai/).
* Download [LM Studio](https://lmstudio.ai/) and install it
* Install `lms cli ~/.lmstudio/bin/lms bootstrap`
* In a bash terminal, run `lms import Devstral-Small-2507-Q4_K_M.gguf` in the directory where you've downloaded the model checkpoint (e.g. `mistralai/Devstral-Small-2507_gguf`)
* Open the LM Studio application, click the terminal icon to get into the developer tab. Click select a model to load and select `Devstral Small 2507`. Toggle the status button to start the model, in setting oggle Serve on Local Network to be on.
* On the right tab, you will see an API identifier which should be `devstral-small-2507` and an api address under API Usage. Keep note of this address, we will use it in the next step.

You can now interact with the model served from LM Studio with openhands. Start the openhands server with the docker

```sh
docker pull docker.all-hands.dev/all-hands-ai/runtime:0.48-nikolaik

docker run -it --rm --pull=always \
    -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.48-nikolaik \
    -e LOG_ALL_EVENTS=true \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/.openhands:/.openhands \
    -p 3000:3000 \
    --add-host host.docker.internal:host-gateway \
    --name openhands-app \
    docker.all-hands.dev/all-hands-ai/openhands:0.48
```

The server will start at http://0.0.0.0:3000. Follow instruction [here](https://docs.all-hands.dev/usage/llms/local-llms#quickstart%3A-running-openhands-with-a-local-llm-using-lm-studio) to configure the LLM calls from OpenHands.
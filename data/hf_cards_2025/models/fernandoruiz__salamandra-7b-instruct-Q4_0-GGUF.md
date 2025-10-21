---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
language:
- bg
- ca
- code
- cs
- cy
- da
- de
- el
- en
- es
- et
- eu
- fi
- fr
- ga
- gl
- hr
- hu
- it
- lt
- lv
- mt
- nl
- nn
- \no
- oc
- pl
- pt
- ro
- ru
- sh
- sk
- sl
- sr
- sv
- uk
datasets:
- oscar-corpus/colossal-oscar-1.0
- HuggingFaceFW/fineweb-edu
- joelniklaus/eurlex_resources
- joelito/legal-mc4
- projecte-aina/CATalog
- UFRGS/brwac
- community-datasets/hrwac
- danish-foundation-models/danish-gigaword
- HiTZ/euscrawl
- PleIAs/French-PD-Newspapers
- PleIAs/French-PD-Books
- AI-team-UoA/greek_legal_code
- HiTZ/latxa-corpus-v1.1
- allenai/peS2o
- pile-of-law/pile-of-law
- PORTULAN/parlamento-pt
- hoskinson-center/proof-pile
- togethercomputer/RedPajama-Data-1T
- bigcode/starcoderdata
- bjoernp/tagesschau-2018-2023
- EleutherAI/the_pile_deduplicated
base_model: BSC-LT/salamandra-7b-instruct
tags:
- llama-cpp
- gguf-my-repo
---

# fernandoruiz/salamandra-7b-instruct-Q4_0-GGUF
This model was converted to GGUF format from [`BSC-LT/salamandra-7b-instruct`](https://huggingface.co/BSC-LT/salamandra-7b-instruct) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/BSC-LT/salamandra-7b-instruct) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo fernandoruiz/salamandra-7b-instruct-Q4_0-GGUF --hf-file salamandra-7b-instruct-q4_0.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo fernandoruiz/salamandra-7b-instruct-Q4_0-GGUF --hf-file salamandra-7b-instruct-q4_0.gguf -c 2048
```

Note: You can also use this checkpoint directly through the [usage steps](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage) listed in the Llama.cpp repo as well.

Step 1: Clone llama.cpp from GitHub.
```
git clone https://github.com/ggerganov/llama.cpp
```

Step 2: Move into the llama.cpp folder and build it with `LLAMA_CURL=1` flag along with other hardware-specific flags (for ex: LLAMA_CUDA=1 for Nvidia GPUs on Linux).
```
cd llama.cpp && LLAMA_CURL=1 make
```

Step 3: Run inference through the main binary.
```
./llama-cli --hf-repo fernandoruiz/salamandra-7b-instruct-Q4_0-GGUF --hf-file salamandra-7b-instruct-q4_0.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo fernandoruiz/salamandra-7b-instruct-Q4_0-GGUF --hf-file salamandra-7b-instruct-q4_0.gguf -c 2048
```

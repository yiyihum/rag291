---
language:
- en
license: cc-by-4.0
size_categories:
- 100K<n<1M
task_categories:
- text-generation
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: answer
    dtype: string
  - name: metadata
    dtype: string
  - name: task
    dtype: string
  splits:
  - name: train
    num_bytes: 2485520315
    num_examples: 147906
  - name: test
    num_bytes: 276168923
    num_examples: 16434
  - name: validation
    num_bytes: 124287779
    num_examples: 7396
  download_size: 461719058
  dataset_size: 2885977017
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
  - split: validation
    path: data/validation-*
tags:
- agent
- reasoning
- logic
- math
- rl
- env
- planning
---

# Reasoning Core ◉

[Paper: Reasoning Core: A Scalable RL Environment for LLM Symbolic Reasoning](https://huggingface.co/papers/2509.18083)
[Code: GitHub Repository](https://github.com/sileod/reasoning_core)

reasoning-core is a text-based RLVR for LLM reasoning training.
It is centered on expressive symbolic tasks, including full fledged FOL, formal mathematics with TPTP, formal planning with novel domains, and syntax tasks.

## Abstract
We introduce Reasoning Core, a new scalable environment for Reinforcement
Learning with Verifiable Rewards (RLVR), designed to advance foundational
symbolic reasoning in Large Language Models (LLMs). Unlike existing benchmarks
that focus on games or isolated puzzles, Reasoning Core procedurally generates
problems across core formal domains, including PDDL planning, first-order
logic, context-free grammar parsing, causal reasoning, and system equation
solving. The environment is built on key design principles of high-generality
problem distributions, verification via external tools, and continuous
difficulty control, which together provide a virtually infinite supply of novel
training instances. Initial zero-shot evaluations with frontier LLMs confirm
the difficulty of Reasoning Core's tasks, positioning it as a promising
resource to improve the reasoning capabilities of future models.

## Sample Usage

### Prime Environment Hub
To use `reasoning-core` with the Prime Environment Hub:
```python
#!pip install uv #install uv if needed
!uv tool install prime --with openai  -q
!uv tool run prime -- env install sileod/reasoning-core-env

from verifiers import load_environment
import os; from openai import OpenAI

env = load_environment("reasoning-core-env")

os.environ["OPENROUTER_API_KEY"] = "" #✍️ write your key
client = OpenAI( base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))
results = env.evaluate(client=client, model="gpt-4.1-mini", num_examples=20, rollouts_per_example=1)
df=env.make_dataset(results).to_pandas()
```

### Standalone
You can also use `reasoning-core` standalone:
```python
pip install reasoning_core

from reasoning_core import list_tasks, get_task, score_answer

T = get_task('arithmetics')()
x = T.generate_example()
assert score_answer(x.answer, x)==1
```

### Generation
Run `bash run_generate.sh` for multi-threaded generation to json files (readable by Huggingface Datasets).

### Reasoning Gym Integration
Our tasks can be imported into `reasoning-gym`:

We use a custom interface, leaner than reasoning-gym (RG). But our tasks, which are all orthogonal to RG, can be imported in it.

```python
import reasoning_gym

from reasoning_core import register_to_reasoning_gym
register_to_reasoning_gym()

specs = [
    # here, leg_counting tasks will make up two thirds of tasks
    DatasetSpec(name='leg_counting', weight=2, config={}),  #from reasoning_gym 🏋
    DatasetSpec(name='arithmetics', weight=2, config={}),  #from reasoning_core ◉
]
D=reasoning_gym.create_dataset('composite', size=10, seed=42, datasets=specs)

```

## Citation
```
@misc{reasoningcore2025,
      title={Reasoning Core: A Scalable RL Environment for LLM Symbolic Reasoning}, 
      author={Valentin Lacombe and Valentin Quesnel and Damien Sileo},
      year={2025},
      eprint={2509.18083},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2509.18083}, 
}
```
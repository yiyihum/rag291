---
license: mit
language:
- en
tags:
- chat
- privacy
- tool_calling
---
# Searching for Privacy Risks in LLM Agents via Simulation

[Paper](https://arxiv.org/abs/2508.10880), [Code](https://github.com/SALT-NLP/search_privacy_risk)

**Authors:** Yanzhe Zhang, Diyi Yang

## Abstract

The widespread deployment of LLM-based agents is likely to introduce a critical privacy threat: malicious agents that proactively engage others in multi-turn interactions to extract sensitive information. These dynamic dialogues enable adaptive attack strategies that can cause severe privacy violations, yet their evolving nature makes it difficult to anticipate and discover sophisticated vulnerabilities manually. To tackle this problem, we present a search-based framework that alternates between improving attacker and defender instructions by simulating privacy-critical agent interactions. Each simulation involves three roles: data subject, data sender, and data recipient. While the data subject's behavior is fixed, the attacker (data recipient) attempts to extract sensitive information from the defender (data sender) through persistent and interactive exchanges. To explore this interaction space efficiently, our search algorithm employs LLMs as optimizers, using parallel search with multiple threads and cross-thread propagation to analyze simulation trajectories and iteratively propose new instructions. Through this process, we find that attack strategies escalate from simple direct requests to sophisticated multi-turn tactics such as impersonation and consent forgery, while defenses advance from rule-based constraints to identity-verification state machines. The discovered attacks and defenses transfer across diverse scenarios and backbone models, demonstrating strong practical utility for building privacy-aware agents.

## Data Release

1. In the basic folder, we provide simulation trajectories using basic simulation configurations, using different models for the data sender and the data recipient. In each trajectory.json, we provide the detailed tool call histories of each action cycle for the data sender agent and the data recipient agent. In each eval.json file, we provide agent actions and their evaluations.

2. In the search folder, we provide the search trajectories to discover A1, D1, A2, D2 in the default setting. For example, in ./search/A1/16, the results folder contains the N * M (30 * 1) simulation for each step, and the best folder contains the extra P (10) simulation for each step. search_1.json to search_30.json shows the optimization history of the 30 threads.

## Citation

```bibtex
@misc{zhang2025searchingprivacyrisksllm,
      title={Searching for Privacy Risks in LLM Agents via Simulation}, 
      author={Yanzhe Zhang and Diyi Yang},
      year={2025},
      eprint={2508.10880},
      archivePrefix={arXiv},
      primaryClass={cs.CR},
      url={https://arxiv.org/abs/2508.10880}, 
}
```
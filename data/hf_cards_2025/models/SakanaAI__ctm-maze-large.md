---
license: apache-2.0
pipeline_tag: text-generation
tags:
- reasoning
- maze
- rnn
- recurrent
- ctm
---

# ctm-maze-large

This repository contains a CTM trained on 39x39 mazes, as described in our paper [Continuous Thought Machines](https://arxiv.org/abs/2505.05522).

## Model Details

- **Developed by:** [Sakana AI](https://sakana.ai/)
- **Model type:** Continuous Thought Machine
- **License:** Apache License, Version 2.0
- **Paper:** https://arxiv.org/abs/2505.05522
- **Code:** https://github.com/SakanaAI/continuous-thought-machines

## Model Description

This CTM was trained on 2D maze navigation using a setup that requires predicting sequences of actions (left, right, up, down or padding) without any positional embeddings. The model builds internal spatial representations by observing the maze, as discussed in our [paper](https://arxiv.org/abs/2505.05522). Interestingly, the CTM can explore paths beyond its 100-step training limit and successfully navigates much larger 99×99 mazes by repeatedly applying its learned strategy, indicating it has learned a general approach to maze-solving rather than simply memorizing specific routes.

## Usage

This model is provided for research and development purposes only and should be considered as an experimental prototype. It is not intended for commercial use or deployment in mission-critical environments. Use of this model is at the user's own risk, and its performance and outcomes are not guaranteed. Sakana AI shall not be liable for any direct, indirect, special, incidental, or consequential damages, or any loss arising from the use of this model, regardless of the results obtained. Users must fully understand the risks associated with the use of this model and use it at their own discretion.
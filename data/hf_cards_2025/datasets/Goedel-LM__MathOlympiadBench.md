---
license: apache-2.0
task_categories:
- text-generation
tags:
- mathematics
- theorem-proving
- formal-methods
- lean4
---

This repository contains the MathOlympiadBench dataset, which is introduced in the paper [Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction](https://huggingface.co/papers/2508.03613).

**Project Page:** https://blog.goedel-prover.com
**Code Repository:** https://github.com/Goedel-LM/Goedel-Prover-V2

MathOlympiadBench (**Math Olympiad**) comprises human-verified formalizations of Olympiad-level mathematical competition problems, sourced from [Compfiles](https://dwrensha.github.io/compfiles/imo.html) and [IMOSLLean4 repository](https://github.com/mortarsanjaya/IMOSLLean4). MathOlympiadBench contains 360 problems, including 158 IMO problems from 1959 to 2024, 131 IMO shortlist problems covering 2006 to 2023, 68 national mathematical Olympiad problems, and 3 additional mathematical puzzles.

MathOlympiadBench is human-processed to eliminate several issues presented in the source problems: 1. incomplete problem statements, 2. distribution across multiple files, 3. multiple theorems per problem, and 4. incompatibility with the commonly used Mathlib. The verification process ensures that each problem contains exactly one formal theorem with its corresponding informal statement, and confirms that all formal statements can pass the compilation with the *sorry* tactic.

We compared the IMO problems shared between MathOlympiadBench and MiniF2F, and identified at least 3 cases in MiniF2F exhibiting issues such as: 1. the formal statement to be proved is strictly weaker than the informal statement, and 2. the formal statement does not match the informal statement. Notably, similar issues are not observed for these problems in MathOlympiadBench.

### Sample Usage

You can download the dataset using Git LFS:

```bash
git lfs install
git clone https://huggingface.co/datasets/Goedel-LM/MathOlympiadBench
```
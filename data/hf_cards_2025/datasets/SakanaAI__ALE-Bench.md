---
language:
- en
- ja
license: cc-by-nd-4.0
pretty_name: ALE-Bench
size_categories:
- n<1K
tags:
- image
- text
task_categories:
- image-text-to-text
- reinforcement-learning
- text-generation
- visual-question-answering
---

# ALE-Bench

## Dataset Description

**ALE-Bench** is a benchmark for evaluating AI systems on score-based algorithmic programming contests.

This dataset is **officially provided by [AtCoder Inc.](https://atcoder.jp/company?lang=en)**.
Please be sure to check the "License" section below.

Please read [our blog post](https://sakana.ai/ale-bench/) and [our paper](https://arxiv.org/abs/2506.09050) for more details.

**Related resources:**

- [Preprint paper (arXiv)](https://arxiv.org/abs/2506.09050)
- [Sakana AI Blog (English)](https://sakana.ai/ale-bench/)
- [Sakana AI Blog (Japanese)](https://sakana.ai/ale-bench-jp/)
- [GitHub repository](https://github.com/SakanaAI/ALE-Bench)
- [Leaderboard](https://sakanaai.github.io/ALE-Bench-Leaderboard/)

## Usage

[Our Python library](https://github.com/SakanaAI/ALE-Bench) automatically downloads the data from this repository.

```python
import ale_bench

ale_bench_session = ale_bench.start("ahc001")
```

## License

[Creative Commons Attribution-NoDerivatives 4.0 International](https://creativecommons.org/licenses/by-nd/4.0/)

## Citation

```bibtex
@article{imajuku2025ale-bench,
    title = {ALE-Bench: A Benchmark for Long-Horizon Objective-Driven Algorithm Engineering},
    author = {Imajuku, Yuki and Horie, Kohki and Iwata, Yoichi and Aoki, Kensho and Takahashi, Naohiro and Akiba, Takuya},
    journal = {arXiv preprint arXiv:2506.09050},
    year = {2025}
}
```

---
tags:
- education
- math
- tutoring
- reinforcement-learning
- question-answering
- instruction-tuning
- dataset
language: en
license: mit
task_categories:
- text-generation
- question-answering
paperswithcode_id: arc-atlas-teach
size_categories:
- n<10K
---

# Arc-ATLAS-Teach

## Summary

This revision bundles 624 high-quality adaptive teaching examples that were generated and validated with the latest five-pass pipeline. Every dialogue walks through the full instructional arc—probe, draft plan, checkpoint feedback, revised plan, and final solution—so the teaching policy observes the complete adjustment process without ever seeing the canonical answer. Probe turns capture the student’s diagnostic attempt, teacher plans and checkpoint comments trace the intervention strategy, revised plans document how the learner internalises that strategy, and final solutions close with an explicit `Answer:` tag to support deterministic scoring. We merged the new 537-example run with the original release, resolved duplicate `problem_id`s, capped answer frequencies at five occurrences per value, and rebalanced the curriculum so length and outcome ratios remain near ATLAS targets. Because both baseline and taught solutions are scored with an exact integer match in the [0, 999] range, uplift measurements remain precise and the non-degradation rate stays at 100%.

## Methodology

The corpus continues to follow the adaptive teaching protocol introduced in the [ATLAS Technical Report](https://github.com/Arc-Computer/ATLAS/blob/main/docs/ATLAS-Technical-Report.pdf) and elaborated in the design notes on the [teacher–student paradigm](https://docs.arc.computer/concepts/teacher-student-paradigm), [hybrid learning loop](https://docs.arc.computer/concepts/hybrid-learning), and [adaptive teaching protocol](https://docs.arc.computer/concepts/adaptive-teaching-protocol). Generation proceeds in three phases. First, we sample a problem and assign it to one of the weak, medium, or strong student models so that we capture a broad distribution of prior knowledge. The student produces a baseline attempt that is scored deterministically, establishing the outcome bucket we target next. Second, the teacher observes the student’s work, constructs a plan that is conditioned on that bucket, and interacts with the student through checkpoint feedback; the student replies with a revised plan, letting the system model how partial guidance reshapes future reasoning. Finally, the student produces a new solution with implicit state updated by the interaction. Each pass is grounded in the hybrid learning framework: baseline solutions stand in for the “policy prior,” teacher plans and checkpoints implement online correction, and the final answer provides the supervised signal used when we recycle these dialogues into the offline alignment loop. By alternating between simulated roll-outs and deterministic evaluation, the pipeline maintains the stability guarantees described in the hybrid learning note, while the teacher–student document guides the conversational conventions that ensure references, scaffolds, and feedback remain self-consistent.

The current release augments the MathDial and BigMath-RL sources with hard curriculum problems drawn from the ATLAS RL and headroom training exports, then applies per-answer frequency capping to maintain coverage without overfitting to dominant integers. This recipe preserves the diversity of intervention styles needed for cross-domain adaptive learning research while increasing the effective uplift signal available to policy training. Because all dialogues include explicit `[ref:...]` anchors that cite earlier turns, researchers can trace how the teacher references probes and checkpoints when delivering scaffolds, mirroring the interaction diagrams in the technical report.

## Files

| Remote path | Description |
|-------------|-------------|
| `data/arc_atlas_teach_core.jsonl` | Full long-form dataset (624 examples) |
| `curriculum/arc_atlas_teach_sft.jsonl` | Supervised FT split (stratified by length/outcome) |
| `curriculum/arc_atlas_teach_rl.jsonl` | RL training set with `bandit_weight` metadata |
| `curriculum/arc_atlas_teach_rl_headroom.jsonl` | RL subset with uplift ≥ 0.10 |
| `curriculum/curriculum_stats.json` | QA snapshot (length/outcome distribution, tokens per turn) |

Each JSONL record captures the problem statement, the student’s capability label, the deterministic ground-truth integer, baseline and taught solutions with their scores and uplift, the five-pass dialogue (including `[ref:...]` anchors for scaffolding), and metadata covering the model roster, outcome bucket, target length band, and token counts.

## Quality Metrics

The merged release contains 624 dialogues: 228 weak, 226 medium, and 170 strong. Short, medium, and long traces account for 35.1%, 36.1%, and 28.8% of the corpus, while outcome buckets are distributed as 22.9% baseline-correct, 69.9% recoverable, and 7.2% catastrophic. Average uplift sits at +0.239 with a non-degradation rate of 100%. Probe, checkpoint, and final solution coverage remain at 100%, every ground truth is an integer between 0 and 999, and each numeric answer appears at most five times after frequency capping.

## Loading

```python
from datasets import load_dataset

ds = load_dataset(
    "Arc-Intelligence/Arc-ATLAS-Teach-v1",
    data_files="data/arc_atlas_teach_core.jsonl",
    split="train"
)
print(ds[0]["dialogue"])
```

To load curriculum splits:

```python
sft = load_dataset(
    "Arc-Intelligence/Arc-ATLAS-Teach-v1",
    data_files="curriculum/arc_atlas_teach_sft.jsonl",
    split="train"
)
rl = load_dataset(
    "Arc-Intelligence/Arc-ATLAS-Teach-v1",
    data_files="curriculum/arc_atlas_teach_rl.jsonl",
    split="train"
)
```

Each example includes an `outcome_bucket` metadata field (`baseline_correct`, `recoverable`, `catastrophic`) and a `bandit_weight` value for RL sampling.

## Generation Notes

Student models draw from the Qwen3 family (4B, 30B, and 235B variants) and the teacher remains `Qwen/Qwen3-235B-A22B-Instruct-2507`. Deterministic scoring compares numeric strings after normalisation, so decimal equality is enforced without heuristics. Outcome-aware prompts tune verbosity so baseline-correct cases resolve quickly whereas catastrophic cases expand into full scaffolds with explicit checkpointing, and all final solutions end with an `Answer:` tag to simplify downstream evaluation and UI rendering.

## License

Same license as previous Arc-ATLAS-Teach releases (MIT).

## Changelog (2025-09-27)

Expanded the dataset to 624 dialogues by merging the latest ATLAS adaptive teaching run with the initial release, applied per-answer frequency capping, refreshed curriculum splits and QA statistics, and improved average uplift to +0.239 while preserving 100% non-degradation.

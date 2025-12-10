---
library_name: transformers
base_model:
- nllg/detikzify-v2-8b
---
# Model Card for DeTi*k*Zify<sub>v2.5</sub> (8b)
DeTi*k*Zify<sub>v2.5</sub> (8b) is a multimodal language model that
automatically converts sketches and existing scientific figures into editable,
semantics-preserving Ti*k*Z graphics programs. It builds on
[DeTi*k*Zify<sub>v2</sub>](https://huggingface.co/nllg/detikzify-v2-8b)
post-trained with reinforcement learning and self-computed rewards. This
approach, which we call reinforcement learning from self-feedback (RLSF),
allows the model to considerably improve itself without necessitating external
reward functions. Check out the
[DeTi*k*Zify](https://github.com/potamides/DeTikZify) project for more
information and tips on how to best run the model.

## Usage
```python
from operator import itemgetter

from detikzify.model import load
from detikzify.infer import DetikzifyPipeline

image = "https://w.wiki/A7Cc"
pipeline = DetikzifyPipeline(*load(
    model_name_or_path="nllg/detikzify-v2.5-8b",
    device_map="auto",
    torch_dtype="bfloat16",
))

# generate a single TikZ program
fig = pipeline.sample(image=image)

# if it compiles, rasterize it and show it
if fig.is_rasterizable:
    fig.rasterize().show()

# run MCTS for 10 minutes and generate multiple TikZ programs
figs = set()
for score, fig in pipeline.simulate(image=image, timeout=600):
    figs.add((score, fig))

# save the best TikZ program
best = sorted(figs, key=itemgetter(0))[-1][1]
best.save("fig.tex")
```

## Reinforcement Learning from Self-Feedback

### Background
DeTi*k*Zify employs an iterative inference algorithm based on [Monte Carlo Tree
Search](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search) (MCTS), enabling
it to continuously refine its outputs without additional training. The reward
scores required by MCTS are computed entirely using DeTi*k*Zify's vision
encoder, by visually assessing the similarity between input figures and
compiled generated outputs. External reward models are not only unnecessary but
often have lower correlations with human judgments, as the vision encoder was
fine-tuned end-to-end with the entire model, optimizing it for evaluating this
specific task. We refer readers to the
[DeTi*k*Zify](https://arxiv.org/abs/2405.15306) and
[Ti*k*Zero](https://arxiv.org/abs/2503.11509) papers for further details.

These self-computed rewards have been effective in enhancing model outputs
during *inference*. With reinforcement learning algorithms like [Group
Relative Policy Optimization](https://arxiv.org/abs/2402.03300), this
reward signal could also be used for the model to improve itself during a
*post-training step*, i.e., reinforcement learning from self-feedback (RLSF).

### Model Training
Our post-training setup does only require figures, and does not require aligned
code as in supervised fine-tuning, granting us more flexibility in selecting
training data. 50% of the training data comes from the subset of
[DaTikZ<sub>v3</sub>](https://huggingface.co/datasets/nllg/datikz-v3), that was
filtered out during the training of DeTi*k*Zify<sub>v2</sub>. The remaining 50%
is sampled from the [SPIQA](https://huggingface.co/datasets/google/spiqa)
dataset, which contains image labels for figures extracted from
[arXiv](https://arxiv.org). We exclude all figures from papers included in
DaTikZ<sub>v3</sub>. We sample this split so that 60% of these figures are
labeled as schematics, 20% as plots, and 20% come from other categories. Since
these figures are not necessarily created from Ti*k*Z, they may aid in
enhancing the model's generalization capabilities. As with
DeTi*k*Zify<sub>v2</sub>, input figures are randomly converted into synthetic
sketches using image transformations and
[UltraSketch](https://huggingface.co/nllg/ultrasketch).

Using this dataset, we post-train
[DeTi*k*Zify<sub>v2</sub>](https://huggingface.co/nllg/detikzify-v2-8b) with
RLSF, employing a batch size of 16. For each image, 32 outputs are generated,
resulting in the model being trained on 512 outputs per step. We train for a
total of 500 steps which takes 5 days to complete on eight Nvidia H200 GPUs. We
keep the vision encoder frozen to mitigate reward hacking.

### Experiments and Results
We evaluate DeTi*k*Zify<sub>v2.5</sub> (8b) on the test split of
DaTi*k*Z<sub>v3</sub> and compare it to DeTi*k*Zify<sub>v2</sub> (8b). The
metrics employed include DreamSim (DSim), Kernel Inception Distance (KID),
CrystalBLEU (cBLEU), TeX Edit Distance (TED), Mean Token Efficiency (MTE), and
Mean Sampling Throughput (MST). Refer to the
[DeTi*k*Zify](https://arxiv.org/abs/2405.15306) paper for further details. All
scores except MST are multiplied by 100.

#### Sampling-based Inference
<table>
  <tr>
    <th></th>
    <th colspan="5">Reference Figures</th>
    <th colspan="5">Synthetic Sketches</th>
  </tr>
  <tr>
    <th>Model</th>
    <th>DSim<sub>&uarr;</sub></th>
    <th>KID<sub>&darr;</sub></th>
    <th>cBLEU<sub>&uarr;</sub></th>
    <th>TED<sub>&darr;</sub></th>
    <th>MTE<sub>&uarr;</sub></th>
    <!-- --- -->
    <th>DSim<sub>&uarr;</sub></th>
    <th>KID<sub>&darr;</sub></th>
    <th>cBLEU<sub>&uarr;</sub></th>
    <th>TED<sub>&darr;</sub></th>
    <th>MTE<sub>&uarr;</sub></th>
  </tr>
  <tr>
    <td>DeTi<i>k</i>Zify<sub>v2</sub> (8b)</td>
    <td>80.503</td>
    <td>0.626</td>
    <td><b>6.105</b></td>
    <td>54.946</td>
    <td>93.326</td>
    <!-- --- -->
    <td>74.584</td>
    <td>0.751</td>
    <td><b>3.356</b></td>
    <td>58.32</td>
    <td>93.858</td>
  </tr>
  <tr>
    <td>DeTi<i>k</i>Zify<sub>v2.5</sub> (8b)</td>
    <td><b>84.6438</b></td>
    <td><b>0.298</b></td>
    <td>4.202</td>
    <td><b>52.939</b></td>
    <td><b>100</b></td>
    <!-- --- -->
    <td><b>78.257</b></td>
    <td><b>0.577</b></td>
    <td>1.551</td>
    <td><b>56.121</b></td>
    <td><b>100</b></td>
  </tr>
</table>

In sampling-based inference (i.e., accepting the first output that compiles
successfully) using reference figures and synthetic sketch inputs,
DeTi*k*Zify<sub>v2.5</sub> (8b) outperforms DeTi*k*Zify<sub>v2</sub> (8b) on
most metrics, demonstrating that RLSF can effectively enhance performance. The
considerably increased DreamSim scores indicate that DeTi*k*Zify<sub>v2.5</sub>
(8b) generates outputs that are much more visually similar to the reference
figures. Furthermore, it is much less likely to produce outputs that do not
compile, as evidenced by its perfect MTE score. Interestingly, while it scores
lower on the code-based metric CrystalBLEU, it performs better on the
code-based TED. DeTi*k*Zify<sub>v2.5</sub> (8b) tends to generate more concise
programs with less syntactic noise. While this likely reduces the n-gram
overlap with the reference code, it also decreases the number of edits
necessary to convert one into another, explaining this phenomenon. Generally,
more concise programs are beneficial as long as the semantics are preserved.

#### MCTS-based Inference
<table>
  <tr>
    <th></th>
    <th colspan="5">Reference Figures</th>
    <th colspan="5">Synthetic Sketches</th>
  </tr>
  <tr>
    <th>Model</th>
    <th>DSim<sub>&uarr;</sub></th>
    <th>KID<sub>&darr;</sub></th>
    <th>cBLEU<sub>&uarr;</sub></th>
    <th>TED<sub>&darr;</sub></th>
    <th>MST<sub>&uarr;</sub></th>
    <!-- --- -->
    <th>DSim<sub>&uarr;</sub></th>
    <th>KID<sub>&darr;</sub></th>
    <th>cBLEU<sub>&uarr;</sub></th>
    <th>TED<sub>&darr;</sub></th>
    <th>MST<sub>&uarr;</sub></th>
  </tr>
  <tr>
    <td>DeTi<i>k</i>Zify<sub>v2</sub> (8b)</td>
    <td>89.020</td>
    <td>0.016</td>
    <td><b>6.593</b></td>
    <td>52.466</td>
    <td>52.723</td>
    <!-- --- -->
    <td>81.482</td>
    <td><b>0.313</b></td>
    <td><b>3.344</b></td>
    <td>56.405</td>
    <td>53.586</td>
  </tr>
  <tr>
    <td>DeTi<i>k</i>Zify<sub>v2.5</sub> (8b)</td>
    <td><b>90.889</b></td>
    <td><b>-0.047</b></td>
    <td>4.646</td>
    <td><b>51.824</b></td>
    <td><b>68.12</b></td>
    <!-- --- -->
    <td><b>83.74</b></td>
    <td>0.61</td>
    <td>1.976</td>
    <td><b>55.239</b></td>
    <td><b>78.908</b></td>
  </tr>
</table>

We observe similar trends when using our MCTS-based inference algorithm with a
time budget of 10 minutes. Compared to sampling-based inference,
DeTi*k*Zify<sub>v2.5</sub> (8b) noticeably improves its scores, illustrating
that MCTS on top of RLSF can still lead to additional gains. Additionally,
within the same timeframe, DeTi*k*Zify<sub>v2.5</sub> (8b) generates 25 more
outputs than DeTi*k*Zify<sub>v2</sub> (8b), supporting our hypothesis that the
generated programs are more concise. On reference figures,
DeTi*k*Zify<sub>v2.5</sub> (8b) scores better on both DreamSim and KID, with
the KID score even being slightly negative due to the high similarity of
distributions. For synthetic sketches, it achieves a higher DreamSim score but
performs worse on KID, indicating a prioritization of faithfulness to the
reference figure over just focusing on general aesthetics.

#### Inference with Ti*k*Zero Adapters
<table>
  <tr>
    <th></th>
    <th colspan="6">Captions</th>
  </tr>
  <tr>
    <th>Model</th>
    <th>DSim<sub>&uarr;</sub></th>
    <th>KID<sub>&darr;</sub></th>
    <th>CLIP<sub>&uarr;</sub></th>
    <th>cBLEU<sub>&uarr;</sub></th>
    <th>TED<sub>&darr;</sub></th>
    <th>MTE<sub>&uarr;</sub></th>
  </tr>
  <tr>
    <td>DeTi<i>k</i>Zify<sub>v2</sub> (8b)</td>
    <td>52.829</td>
    <td><b>5.103</b></td>
    <td><b>10.051</b></td>
    <td><b>1.603</b></td>
    <td>65.51</td>
    <td>82.291</td>
  </tr>
  <tr>
    <td>DeTi<i>k</i>Zify<sub>v2.5</sub> (8b)</td>
    <td><b>53.564</b></td>
    <td>7.471</td>
    <td>7.968</td>
    <td>0.732</td>
    <td><b>62.189</b></td>
    <td><b>100</b></td>
  </tr>
</table>

[Ti*k*Zero adapters](https://huggingface.co/nllg/tikzero-adapter) integrate
into the vision encoder of DeTi*k*Zify models, enabling them to be conditioned
on text in addition to images. Since we keep the vision encoder frozen, we can
evaluate DeTi*k*Zify<sub>v2.5</sub> (8b) on adapters trained for
DeTi*k*Zify<sub>v2</sub> (8b). Compared to our previous experiments, the
results are more varied. While DeTi*k*Zify<sub>v2.5</sub> (8b) achieves a
better DreamSim value and maintains a perfect MTE, it performs worse on
CLIPScore, suggesting difficulties in reproducing text from captions. This
could be due to an increased modality gap, as RLSF further refines the model
for image-only inputs. We plan to address this in future work by incorporating
caption inputs into RLSF training.

### Summary
Overall, RLSF greatly enhances model performance for most tasks. For image
and sketch inputs, DeTi*k*Zify<sub>v2.5</sub> (8b) emerges as the clear leader.
For text inputs via Ti*k*Zero adapters, the choice between model versions
depends on the specific use case, given the trade-offs involved.

### Acknowledgments
This model was trained using computational resources provided by the
bwForCluster Helix, as part of the bwHPC-S5 project. The authors acknowledge
support from the state of Baden-Württemberg through the bwHPC initiative and
the German Research Foundation (DFG) under grant INST 35/1597-1 FUGG. This
project was inspired by the paper [Rendering-Aware Reinforcement Learning for
Vector Graphics Generation](https://arxiv.org/abs/2505.20793).
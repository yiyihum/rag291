---
license: mit
language:
- en
- zh
pipeline_tag: text-generation
library_name: exllamav3
base_model: zai-org/GLM-4.6
base_model_relation: quantized
tags:
- exl3
---

exllamav3 quantizations of [zai-org/GLM-4.6](https://huggingface.co/zai-org/GLM-4.6).

## Optimized quants

[2.06 bpw h6](https://huggingface.co/MikeRoz/GLM-4.6-exl3/tree/2.06bpw_H6) 86.376 GiB    
[2.25 bpw h6](https://huggingface.co/MikeRoz/GLM-4.6-exl3/tree/2.25bpw_H6) 94.139 GiB    
Measurement file used in creation of the above: [measurement-20-vs-30.json](https://huggingface.co/MikeRoz/GLM-4.6-exl3/resolve/main/measurement-20-v-30.json?download=true) 

### Recipe

<details>
<summary>Expand for more details</summary>

exllamav3 includes a measurement script `util/measure.py` that will compare two exllamav3 models module by module against the original model. The goal is to see which modules are the most affected by the decrease in precision involved in going from a larger quant to a smaller quant.

The command is: 
```bash
python util/measure.py -l [level] -d [device] -ms [max_sys_memory] -i [path/to/quant1] [path/to/quant2] -r [path/to/original_model] -o [path/to/measurement.json]
```
Where:
* `level` is an integer between 0 and 3 that determines the resolution of the measurement. 0 is fastest but least granular, 2 is default, 3 is most granular and slowest.
* `device` is the index of the CUDA device that will perform the work
* `max_sys_memory` is the amount of memory that can be used for state data to speed things up, in GiB
* `path/to/quant1` and `path/to/quant2` are the paths to the two quants to compare
* `path/to/original_model` is the path to the original model
* `path/to/measurement.json` is the path to the resulting json measurement file

The masurement fie I created above compared my 2.0bpw_H6 and my 3.0bpw_H6 quants.

You can then feed this measurement file, along with the two quants, to `util/optimize.py` to create optimized quants that draw modules from both quants where appropriate to get the best result for a given bitrate.

The command is:
```bash
python util/optimize.py -i [path/to/quant1] [path/to/quant2] -o [path/to/resulting_model] -m [path/to/measurement.json] -b [target_bitrate]
```
Where:
* `path/to/quant1` and `path/to/quant2` are paths to the two source models
* `path/to/resulting_model` is the output path
* `target_bitrate` is the target bitrate as a number a decimal point

You can use a measurement script from one pair of quants with another pair of quants of the same model. When I tried to use 2.0bpw and 4.0bpw quants to create a 2.25bpw quant, the size of the resulting model was larger than requested because of the substitution at 2.48 bpw, but it was still an improvement over a straight 2.48bpw quant. An explicitly-requested 2.48bpw quant drawing from the 2.0bpw and 3.0bpw quants proved to be even better (in terms of k/l divergence). Finally, I tried creating a 3.25bpw quant from 3.0bpw and 4.0bpw quants, still using my 2.0-vs-3.0 measurement file. This was not as successful as the optimized 2.25bpw quant, and may have benefitted from a 'correct' measurement file that matched the two actual sources.
</details>

### K/L-D and PPL graphs

To compare the results of using the optimizer script versus just directly quantizing to the same bitrate, I created a number of 'straight' and 'optimized' quants at the same bitrates. Most of the optimized quants used my 2.0bpw_H6 and my 3.0bpw_H6 quants as sources. It appears that the optimizer script provides a dramatic improvement in K/L Divergence at lower bitrates.

If there is any interest in my uploading any of the quants in the chart that aren't already here, let me know.

![KLD Chart](glm46kld.png)
![PPL Chart](glm46ppl.png)

* The "EXL3 2.48bpw H6 optimize.py 2x4" quant was created by the optimize.py script using the 2.0bpw and 4.0bpw quants as inputs but the 2.0bpw vs 3.0bpw measurement file.
* The "EXL3 3.25bpw H6 optimize.py" quant was created by the optimize.py script using the 3.0bpw and 4.0bpw quants as inputs but the 2.0bpw vs 3.0bpw measurement file.

<details>
<summary>How to create ppl and k/l-d graphs using scripts included in exllamav3 (expand)</summary>
If your model is too large to load without quantization, you can run a script to generate logits which can then be passed into the comparison script.

First, you'll need to create a dataset spec file. I based mine on `eval/spec/wiki2_llama3_large.json`.
```json
{
    "tokenize_fn": "transformers",
    "tokenizer_dir": "path/to/full_model",
    "dataset": "wiki2",
    "eval_stride": 512,
    "eval_len": 2048,
    "max_rows": 100
}
```

I passed this into `eval/compare_q_logits.py` as follows:

```bash
python eval/compare_q_logits.py -m [path/to/full_model] -o [path/to/output_logits.safetensors] -d [path/to/dataset_spec.json] -rpb [rows_per_batch] -dev [device_index]
```
Where:
* `path/to/full_model` is the path to the model
* `path/to/output_logits.safetensors` is the path to the output logits file
* `path/to/dataset_spec.json` is the path to the dataset spec file described above
* `rows_per_batch` - I would run out of memory without this parameter. I set it to 32768.
* `device_index` - optional CUDA device index

Next, you'll need a model spec file that describes all the quants you want in the graph. You'll need to be able to load any model you'd like compared. Here's a sample of the one I used for my GLM-4.6 quants:
```json
[
    {
        "load_fn": "exllamav3",
        "fwd_fn": "exllamav3",
        "label": "EXL3 2.0bpw H6",
        "model_dir": "path/to/zai-org_GLM-4.6-2.0bpw-h6-exl3"
    },
    {
        "load_fn": "exllamav3",
        "fwd_fn": "exllamav3",
        "label": "EXL3 2.25bpw H6 optimize.py",
        "model_dir": "path/to/zai-org_GLM-4.6-2.25bpw-h6-exl3"
    }
]
```

This spec file can be passed in to the following command:
```bash
python eval/compare_q.py -d [path/to/dataset_spec.json] -m [path/to/model_spec.json] -lf [path/to/logits.safetensors] -p [-kld] -t [chart_title]
```
Where:
* `path/to/dataset_spec.json` is the path to the dataset spec file described above
* `path/to/model_spec.json` is the path to the model spec file described above
* `path/to/logits.safetensors` is the path to the full model's logits, created above
* `-kld` the script creates a perplexity chart by default, add this if you want K/L-d instead
* `chart_title` the chart title in the resulting plot

Note that there is currently a bug which prevents all memory from being released after each model - for me, the script would OOM after the first model. However, **results are cached after each run** so you just need to restart the script until every model has been tested. Also note that if you're running this via SSH like me, you may not see anything - the script uses `plt.show()`. I hacked in an extra arg and a `plt.savefig()` install instead.
</details>

## Straight quants

[2.00 bpw h6](https://huggingface.co/MikeRoz/GLM-4.6-exl3/tree/2.00bpw_H6) 84.517 GiB    
[3.00 bpw h6](https://huggingface.co/MikeRoz/GLM-4.6-exl3/tree/3.00bpw_H6) 125.398 GiB    
[4.00 bpw h6](https://huggingface.co/MikeRoz/GLM-4.6-exl3/tree/4.00bpw_H6) 166.280 GiB     
[5.00 bpw h6](https://huggingface.co/MikeRoz/GLM-4.6-exl3/tree/5.00bpw_H6) 207.162 GiB     
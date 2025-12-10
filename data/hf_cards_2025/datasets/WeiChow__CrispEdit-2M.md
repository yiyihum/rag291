---
license: cc-by-4.0
pretty_name: CrispEdit-2M
configs:
- config_name: default
  data_files:
  - split: train
    path: data/*
task_categories:
- image-to-image
language:
- en
size_categories:
- 1M<n<10M
tags:
- image
- image-editing
- instruction-tuning
- instruction-guided
- multimodal
library_name: datasets
---

CrispEdit-2M have 7 type, which is saved in file data:
| filename prefix & type in parquet | type name |
|-------|------|
| color | color alter |
| motion change | motion change |
| style | style change |
| replace | replace |
| remove | remove |
| add | add |
| background change | background change |

CrispEdit-2M is stored in parquet format, and each parquet has 256 items.
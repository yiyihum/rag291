---
base_model:
- huihui-ai/Mistral-Small-24B-Instruct-2501-abliterated
- PocketDoc/Dans-DangerousWinds-V1.1.1-24b
- trashpanda-org/MS-24B-Instruct-Mullein-v0
library_name: transformers
tags:
- mergekit
- merge
- dark
- roleplay
- negative
language:
- en
- ru
---
# merge

This is a merge of pre-trained language models.

This merge is better than v1. v1 machina will be deleted tomorrow.

Has neutral or negative bias, if prompt is good enough model can be evil and cruel. maybe even too cruel.

Main idea is to merge base mistral with something, and preserve base's ability to write on russian.

Secondary idea was to create model that will be not "friendship is magic" thing, to use in more "dark" scenarios. 

Judging by the tests, i've succeeded with both ideas.

Model was tested on russian and on english with ~1000 responses, was stable and seems that it not lose original's "intellectual abilities", but maybe i'm just very lucky.  

With char cards that have first message on russian, but whole description on english, model have some difficulties, but still able to answer on desired language.

With full ru cards model performs without issues.

Tested on T1.01 ChatML

I reccomend to use sphiratrioth666/SillyTavern-Presets-Sphiratrioth, for me it works very good with minor adjustments.
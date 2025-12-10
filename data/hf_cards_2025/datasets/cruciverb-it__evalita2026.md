---
language:
- it
license: other
license_name: copyrighted-research-purposes
license_link: LICENSE
tags:
- word-game
- italian
- word-puzzle
- crossword
language_creators:
- expert-generated
pretty_name: cruciverb-it-evalita26
size_categories:
- 100K<n<1M
source_datasets:
- Kamyar-zeinalipour/ITA_CW
task_categories:
- text-generation
configs:
- config_name: task_1
  data_files:
  - split: train
    path: task_1/datasets/train.csv
  - split: val
    path: task_1/datasets/val.csv
extra_gated_prompt: "### Cruciverb-IT License Agreement \n\n\"Agreement\" means the\
  \ terms and conditions for use, reproduction, distribution and modification of the\
  \ materials set forth herein.\n\n1. Data Source and Redistribution\n\nThe contents\
  \ of the  files are extracted directly from open online resources. Copyright of\
  \ Individual Entries\n\nThe rights to each entry in this collection are the property\
  \ of the respective copyright holders.\n\n  Derivative Works\n\nAll derivative works\
  \ using the included data are to be used exclusively for non-commercial research\
  \ purposes in accordance with Article 70 of the Italian Copyright Law. Any further\
  \ derivative work building upon these resources should remain licensed with a non-commercial\
  \ license allowing research applications.\n\n2. Terms of Use\n\na. Non-commercial\
  \ Use Only: All data and derivative works in this repository may be used solely\
  \ for non-commercial research purposes.\n\n3. Disclaimer\n\nThis data is provided\
  \ \"as is\" without any warranties, express or implied. The licensors make no representations\
  \ or warranties regarding the accuracy, completeness, or fitness for a particular\
  \ purpose of the data.\n\n4. Right of Removal\n\nWe reserve the right to remove\
  \ any part of the data from the repository at any time, particularly in the event\
  \ that a copyright holder requests its removal.\n\n5. Termination\n\nThis license\
  \ will terminate automatically if you fail to comply with the terms stated herein.\
  \ Upon termination, you must destroy all copies of the data in your possession.\n\
  \n6. Governing Law\n\nThis license shall be governed by and interpreted in accordance\
  \ with the laws of Italy, particularly in relation to copyright law and fair use\
  \ for research purposes.\n\nBy accessing or using the data in this repository, you\
  \ agree to be bound by the terms of this license. If you do not agree to these terms,\
  \ you are not permitted to access or use the data.\n\nFor any questions regarding\
  \ this license or requests for additional permissions, please contact workshop organizers\
  \ at cruciverbit.evalita2026@gmail.com.\n\nLast updated: September 22th, 2025"
extra_gated_fields:
  I agree to use this dataset exclusively for non-commercial research purposes: checkbox
  I agree to comply with the data license for this dataset: checkbox
  Name of the researcher(s), separated by commas: text
  Institution(s), separated by commas: text
  Contact email: text
---

![Cruciverb-IT Logo](./cruciverbit_logo.png)

*This repository contains the data release for the [Cruciverb-IT](https://sites.google.com/view/cruciverbit2026) shared task on automatic crossword solving in Italian, as part of the [2026 EVALITA campaign](https://www.evalita.it/campaigns/evalita-2026/). Refer to the task website for more details.*

The data from both tasks can be downloaded from the ['Files and versions' tab](https://huggingface.co/datasets/cruciverb-it/evalita2026/tree/main).

## Task 1: Clues Answering

### Overall Description

The first task consists of answering clues extracted from Italian crosswords. Specifically, participants are presented with a set of clues C={c₁, c₂, ..., cₙ} and are asked to build a system that for a given clue cᵢ is able to produce one or multiple candidate solutions S={s₁, s₂, ..., sₙ}, possibly containing the correct answer sᵢ. To simulate a more realistic crossword solving scenario and to further guide the systems towards the correct answer space, each clue cᵢ is paired with the character length of the target answer sᵢ. For example: given the clue and the target character length “Sono un fiore di straordinaria bellezza, 4”, the systems should produce a list of one or more candidates, i.e. {iris, rosa, rose, yuzu, fior, ...} eventually containing the correct answer rosa.

#### Released Data Format

The folder `task_1` contains two .csv files: `datasets/train.csv` and `datasets/val.csv`. Both files are structured with the following columns: `clue`, `answer`, `answer_length`. These correspond to the clue, the related answer and the number of charcaters of the related answer, respectively.

#### Scorer and Predicition Format

Together with the datasets, the folder "task_1" contains a python file, "task_1_scorer.py", that can be run to evaluate the predictions. This scorer will be the same used during the systems evaluation. The script expects two arguments: the path of the predictions and the path of the original dataset. For example:

``` shell
python task_1_scorer.py val_preds.csv datasets/val.csv
```

The script will compute the metrics and save a .json file containing the results, for example:

``` json
{
    "acc@1": 0.11,
    "acc@10": 0.22,
    "mrr": 0.03,
    "num_examples": 20821
}
```

Metrics are:
- acc@1: the accuracy in predicting the correct solution in the top 1 candidate
- acc@10: the accuracy in predicting the correct solution in the top 10 candidates
- mrr: Mean Reciprocal Rank, that is the average of the reciprocal ranks of the first correct candidate across all clues


The predictions must be a .csv file structured exactly as the released datasets with an additional column "candidates" containing a list of one or more predictions for each clue. For example: 

``` csv
clue,answer,answer_length,candidates
Giorni di metà mese nell'antica Roma,idi,3,"['mid', 'poi', 'idi']"
...
```

## Task 2: Grid Filling

### Overall Description 

The second task consists of autonomously solving Italian crossword grids. The participants are presented with a set of empty crossword grids G={G₁, G₂, ..., Gₖ} where each grid Gᵢ is paired with a list of clues, each one annotated with the coordinates of the square where the corresponding solution starts in the grid, the direction, either down (verticale) or across (orizzontale), and the answer length in characters. A crossword grid consists of a matrix Gᵢ of size Rⁿˣⁿ and each square is either blank or a black square. The developed systems should autonomously fill the grid with the appropriate solutions, yielding a fully or partially filled crossword grid that ensures a consistent overlap between the characters of crossing words and maximizes the number of appropriate solutions correctly placed in the grid.


#### Released Data Format 
The "crosswords_datasets" folder contains the released data for the second task. Each split comes with three files. Importantly, **all of them represents each crossword as a single line**, that is they all have the same number of lines and each line refer to the same specifc crossword (i.e., the first line of each file is related to the first crossword, the second line of each file to the second crossword and so on):

- "train_grids_empty.txt": the flatted grids layout. Each line in the .txt is an empty crossword grid represented as a matrix, i.e. a list of lists, where each square is either blank (noted as a whitespace ' ') or a black square (noted as a dot '.'). For example:

``` python
[[' ', ' ', ' ', ' ', ' '], [' ', '.', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '.', ' '], [' ', ' ', ' ', ' ', ' ']]
...
```
- "train_cross_clues.jsonl":  a .jsonl file where each line is a list of json dictionaries representing the clues and the related informations for a specific crossword.
    * "clue": the clue
    * "row": row index
    * "col": column index
    * "direction": the direction in which the answer should be placed, either "A" (Across) or "D" (Down)
    * "target": the answer to the clue
    * "lenght": the answer character lenght

    For example:
    ``` python
    [{"target": "EVANS", "clue": "Un Bill del jazz", "row": 0, "col": 0, "direction": "A", "length": 5}, {"target": "ONC", "clue": "Sigla dell'Opera Nazionale Combattenti", "row": 1, "col": 2, "direction": "A", "length": 3}, {"target": "CANEE", "clue": "Mute abbaianti", "row": 2, "col": 0, "direction": "A", "length": 5}, {"target": "HEI", "clue": "Un grido di richiamo", "row": 3, "col": 0, "direction": "A", "length": 3}, {"target": "EREDE", "clue": "Un discendente", "row": 4, "col": 0, "direction": "A", "length": 5}, {"target": "ESCHE", "clue": "Le valutano i pescatori", "row": 0, "col": 0, "direction": "D", "length": 5}, {"target": "AER", "clue": "L'aria dei Latini", "row": 2, "col": 1, "direction": "D", "length": 3}, {"target": "AONIE", "clue": "Appellativo delle Muse", "row": 0, "col": 2, "direction": "D", "length": 5}, {"target": "NNE", "clue": "Punto della bussola opposto a SSO", "row": 0, "col": 3, "direction": "D", "length": 3}, {"target": "SCEME", "clue": "Stolte, scarse di cervello", "row": 0, "col": 4, "direction": "D", "length": 5}]
    ```
- "train_grids_gold.txt": the solved flatted grids. Each line in the .txt is a correctly solved crossword represented as a matrix, i.e. a list of lists, where each square is either single uppercase character (i.e., 'B') or a black square (noted as a dot '.'). For example:


``` python
[['E', 'V', 'A', 'N', 'S'], ['S', '.', 'O', 'N', 'C'], ['C', 'A', 'N', 'E', 'E'], ['H', 'E', 'I', '.', 'M'], ['E', 'R', 'E', 'D', 'E']]
...
```


#### Scorer and Predicition Format
Together with the datasets, the folder "task_2" contains a python file, "task_2_scorer.py", that can be run to evaluate the predicted crossword grids. This scorer will be the same used during the systems evaluation. The script expects three arguments: the path of the predictions, the path of the gold crossword grids and the path of the gold jsonl clues file. For example: 

``` shell
python task_2_scorer.py predictions.txt crosswords_datasets/val_grids_gold.txt crosswords_datasets/val_cross_clues.json 
```

The script will compute the metrics and save a .json file containing the results, for example:

``` json
{
    "char_acc": 0.53,
    "word_acc": 0.44,
    "full_match_accuracy": 0.08,
    "num_examples": 50
}
```

Metrics are:
- char_acc: the accuracy in inserting the correct characters in the correct slots
- word_acc: the accuracy in inserting the correct word in the correct slots
- full_match_accuracy: the accuracy in solving the entire grid. A partially filled grid will be evaluated counting empty squares as errors.


The predictions must be structured the same as a the gold crossword grids file, that is a .txt where each line is a predicted crossword grid represented as a matrix, i.e. a list of lists, where each square is either a single uppercase character (i.e., 'B'), a black square (noted as a dot '.') or None for an unsolved slot in case of a partially solved grid.

. For example: 

``` python
[['E', None, 'A', 'N', 'S'], ['S', '.', 'O', 'N', 'C'], ['C', 'A', 'N', 'E', 'E'], ['H', 'E', 'I', '.', None], ['E', 'R', 'E', 'D', 'E']]
...
```

In case of no solutions for a specific crossword grid, i.e. there are no candidates for each clue, the prediction for this crossword can be expressed with an emtpy grid or with a None at the corresponding line in the prediction file.

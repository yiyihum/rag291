---
language:
- de
size_categories:
- 10K<n<100K
task_categories:
- text-generation
pretty_name: gulaschnascher4000 Twitch Stream Dataset 0-2
tags:
- not-for-all-audiences
- stram
- chat
dataset_info:
  features:
  - name: instruct
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 650051
    num_examples: 4295
  - name: test
    num_bytes: 509844
    num_examples: 3375
  download_size: 708470
  dataset_size: 1159895
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
---


#### Who are the source data producers?

[Alle im Stream Chat aktiven Zuschauer]

Danke an alle die, die diesen Datensatz ermöglicht haben.
Ebenso bedanke ich mich bei allen die den Stream finanziell unterstützt haben. 
Wie versprochen, hab ich das Geld für 'unnützes' rausgeworfen. (in diesem Falle für Rechenleistung :-D )

(Für eventuelle Interessierten: 'by me a coffee on Twitch')




## Dataset Details

Als 'input' wurde sich nach den Zuschauernachrichten gerichtet. 
'instruct' und 'output' wurden 100% Ki generiert. 

Info zum Inhalt: 
- es wurden bewusst keine Nachrichten irgendwelcher Benutzer gefiltert. (Pure as fuck...)
- die Generierung für 'output' wurde bewusst 'böse', 'sarkastisch' und 'satirisch' erzeugt.
  Da es jedoch mit einem 'normalen' Model erzeugt wurde, sollte sich nichts rechtswidriges darin befinden.




### Dataset Description

Basierend auf dem Chatverlauf, des Twitch-Livestreams von 'gulaschnascher4000'
Es wurde bewusst auf kurze 'output' wertgelegt.
Genutzte Modelle: phi4, phi4:14b-q8_0



- **Funded by:** gulaschnascher4000
- **Language(s) (NLP):** [german]

### Dataset Sources [optional]

- **Repository:** [https://www.twitch.tv/gulaschnascher4000]

## Dataset Structure


Instruction:
Input:
Output:


## Dataset Card Authors [optional]

[gulaschnascher4000]

## Dataset Card Contact

https://www.twitch.tv/gulaschnascher4000
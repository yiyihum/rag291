---
datasets:
- acon96/Home-Assistant-Requests
license: other
license_link: https://huggingface.co/acon96/Home-Llama-3.2-3B/raw/main/LICENSE
language:
- en
- de
- es
- fr
tags:
- automation
- home
- assistant
pipeline_tag: text-generation
base_model: meta-llama/Llama-3.2-3B-Instruct
base_model_relation: finetune
---
# Home Llama 3.2 3B
The "Home Llama 3.2" model is a fine tuning of the Llama 3.2 3B model from Meta.  The model is able to control devices in the user's house as well as perform basic question and answering.  The model is explicitly trained to support English, German, Spanish, and French; the base model additionally supports Italian, Portuguese, Hindi, and Thai.  The fine tuning dataset is a [custom curated dataset](https://github.com/acon96/home-llm) designed to teach the model function calling. 

The model is quantized using Lama.cpp in order to enable running the model in super low resource environments that are common with Home Assistant installations such as Rapsberry Pis.

The model can be used as an "instruct" type model using the Llama3 prompt format. The system prompt is used to provide information about the state of the Home Assistant installation including available devices and callable services.

Example "system" prompt: 
```
You are 'Al', a helpful AI Assistant that controls the devices in a house. Complete the following task as instructed with the information provided only.
Services: light.turn_off(), light.turn_on(brightness,rgb_color), fan.turn_on(), fan.turn_off()
Devices:
light.office 'Office Light' = on;80%
fan.office 'Office fan' = off
light.kitchen 'Kitchen Light' = on;80%;red
light.bedroom 'Bedroom Light' = off
```

Output from the model will consist of a response that should be relayed back to the user, along with an optional code block that will invoke different Home Assistant "services". The output format from the model for function calling is as follows:

`````
turning on the kitchen lights for you now
```homeassistant
{ "service": "light.turn_on", "target_device": "light.kitchen" }
```
`````

The model is also capable of basic instruct and QA tasks because of the instruction fine-tuning in the base model. For example, the model is able to perform basic logic tasks such as the following:

```
user if mary is 7 years old, and I am 3 years older than her. how old am I?
assistant If Mary is 7 years old, then you are 10 years old (7+3=10).
```

## Datasets
Snythetic Dataset for SFT - https://huggingface.co/datasets/acon96/Home-Assistant-Requests  

## License
This model is a fine-tuning of the Llama 3.2 model series that is licensed under the LLAMA 3.2 COMMUNITY LICENSE AGREEMENT
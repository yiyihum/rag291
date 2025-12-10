---
license: gpl-3.0
task_categories:
- text-generation
language:
- zh
tags:
- not-for-all-audiences
- hentai
- nsfw
- catgirl
- roleplay
- uncensored
- qwen
- qwen3
- mutt
- zhtw
- taiwan
size_categories:
- 1K<n<10K
---

# What this dataset does
[catgirl-dataset](https://huggingface.co/datasets/kxdw2580/catgirl-dataset) where the AI acts as a
catgirl maid to service the user(referred as master)

## The problem that the original catgirl-dataset has
1. There aren't a lot of Traditional Chinese(Taiwan) datasets on huggingface and it pretty much
   ruins the mood when the AI spits out Simplified Chinese to people from Taiwan(especially those
   who uses qwen3 as the base training model)
2. The original dataset is designed to be censored. For example when the user ask if she wants sex,
   she ignores the user and proceeds to change the topic, or pretend that she doesn't know what the
   user is referring to. If you ask her if she slurs she would say that she is a polite maid who
   doesn't.
3. The original dataset assums that the user is a male, which in a lot of cases might suck if you're
   into yuri
4. This dataset has some portion of Chinese-specific stuff like "拼多多" or things as such so it
   might be troublesome to understand some of her references for Chinese users outside of mainland
   China(like Taiwan, Singapore, Malaysia etc.)

## The solution
### The Traditional Chinese(Taiwan) issue
It's pretty much well known that Taiwan uses a different variant of Chinese, different from what mainland
China uses. So, I've written a shellscript called [replace.sh](replace.sh). It uses opencc to first translate
it into Traditional Chinese and then replaces words that are used in China with those equivilant to
what people in Taiwan says. For example, 「早上好」or good morning in China has the same meaning
as「早安」in Taiwan. To preserve the original efforts of the author and also to let mainland Chinese
people have access to these datasets as well, I've kept the original Simplified Chinese as is and a suffix 'TW' in the filename for the Taiwanese version.
### Censorship
I mainly used the Tifa-Ultra-V2-20250323 from [this website](https://leftnorth.com/test.html) where
you can freely used there uncensored models(props to them), I've managed to generate new datasets to give more
information about sex, illegal mutt, and other new "censored" stuff for the AI. I've also replaced
the original ones that are censored with the new ones. Also if you want to know what prompt I used
to generate these see the [prompts](prompts) directory. Because this dataset is designed to fine-tune a
Chinese model qwen3, I've added datasets that are against these censorships as well. For example one
being the catgirl telling a story of she going to Tiananmen Square to put protest banners about the
1989 massacre and was nearly killed by the police.

Don't worry, I've only added one prompt about politics in the prompt so it won't be a full-on
propaganda producer or an average Redditor from r/politics.

## What does each of those files mean?

This is a dataset that is based off of catgirl-dataset in the v2-qwen directory. The dataset has
three seperate part for different purposes:

* common: The main thing. Mostly these are interactions between the catgirl and the user for
  day-to-day uses. It mainly expands the knowledge of the AI of how to act like an ideal catgirl and
  also how to please the user as well.
* creative: This expands the creativity of the catgirl.

## Developer Note:
The [count.sh](count.sh) file counts through how many Chinese characters there are in total so that
you can estimate how long it'll take for you to fully fine-tune your model!
Feel free to give me pull requests for this project to produce more high-quality datasets!

## Special Thanks:
Thanks to [Ruri_Helesta](https://x.com/Ruri_Helesta) for working this project with me! He's the one
who fine-tunes the model with these datasets for me to test!

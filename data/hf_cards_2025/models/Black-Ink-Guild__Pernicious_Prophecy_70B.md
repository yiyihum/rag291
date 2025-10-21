---
base_model:
- SicariusSicariiStuff/Negative_LLAMA_70B
- invisietch/L3.1-70Blivion-v0.1-rc1-70B
- EVA-UNIT-01/EVA-LLaMA-3.33-70B-v0.1
- aaditya/Llama3-OpenBioLLM-70B
library_name: transformers
tags:
- merge
- axolotl
- finetune
license: llama3.3
license_name: llama3.3
language:
- en
---
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <title>Pernicious Prophecy 70B</title>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link
    href="https://fonts.googleapis.com/css2?family=Darker+Grotesque:wght@300..900&family=Uncial+Antiqua&display=swap"
    rel="stylesheet">

  <style>
    html,
    body {
      margin: 0;
      padding: 0;
      background: rgb(11, 15, 25);
      color: #E6FFE6;
      font-family: 'Darker Grotesque', sans-serif;
    }

    @keyframes runeGlow {
      0% {
        text-shadow: 0 0 4px #91ca00;
        filter: brightness(0.7);
      }

      50% {
        text-shadow: 0 0 8px #91ca00;
        filter: brightness(1.0);
      }

      100% {
        text-shadow: 0 0 4px #91ca00;
        filter: brightness(0.7);
      }
    }

    img.badge {
      filter: grayscale(100%);
      transition: filter 0.7s ease-in-out;
    }
    
    img.badge:hover {
      filter: grayscale(0%);
    }

    .rune-border::before,
    .rune-border::after,
    .vertical-sides::before,
    .vertical-sides::after {
      animation: runeGlow 1.5s infinite alternate;
    }

    .rune-border::before {
      animation-delay: 0s;
    }

    .rune-border::after {
      animation-delay: 0.2s;
    }

    .vertical-sides::before {
      animation-delay: 0.4s;
    }

    .vertical-sides::after {
      animation-delay: 0.6s;
    }

    .rune-border {
      position: relative;
      max-width: 45em;
      margin: 2em auto;
      padding: 2em 4em;
      box-sizing: border-box;
    }

    .rune-border::before,
    .rune-border::after {
      position: absolute;
      left: 0;
      right: 0;
      margin: 0 2em;
      text-align: center;
      white-space: nowrap;
      overflow: hidden;

      color: #91ca00;
      text-shadow: 0 0 4px #91ca00;
      font-family: monospace;
      font-size: 14px;
      content: "ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ";
    }

    .rune-separator:after {
      position: absolute;
      left: 0;
      right: 0;
      margin: 0 2em;
      text-align: center;
      white-space: nowrap;
      overflow: hidden;

      color: #91ca00;
      text-shadow: 0 0 4px #91ca00;
      font-family: monospace;
      font-size: 14px;
      content: "ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ";
    }

    .rune-border::before {
      top: 0;
    }

    .rune-border::after {
      bottom: 0;
    }

    .vertical-sides {
      position: absolute;
      margin: 2em 0;
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
      pointer-events: none;
    }

    .vertical-sides::before,
    .vertical-sides::after {
      position: absolute;
      top: 0;
      bottom: 0;
      width: 1.5em;
      white-space: nowrap;
      overflow: hidden;

      color: #91ca00;
      text-shadow: 0 0 4px #91ca00;
      font-family: monospace;
      font-size: 14px;
      writing-mode: vertical-rl;
      text-orientation: mixed;
    }

    .vertical-sides::before {
      left: 0;
      content: "ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ";
    }

    .vertical-sides::after {
      right: 0;
      content: "ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ | ᛁᛏ ᛁᛋ ᚢᚱᛁᛏᛏᛁᚾ ᛅᚾᛏ ᛁᛏ ᚢᛁᛚᛚ ᚴᚬᛘᛁ ᛏᚬ ᛒᛅᛋᛋ";
    }

    h1,
    h2,
    h3 {
      font-family: "Uncial Antiqua", serif;
      font-weight: 400;
      font-style: normal;
      color: #426100;
      -webkit-text-stroke: 1px #91ca00;
      text-stroke: 1px #91ca00;
      margin-top: 1em;
    }

    h2 {
      padding-top: 1.5em;
    }

    a {
      color: #619300;
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    h1 {
      font-size: 2.5em;
    }

    h2 {
      font-size: 2em;
    }

    h3 {
      font-size: 1.5em;
    }

    p,
    li {
      font-size: 1.2em;
      line-height: 1.2;
    }

    p.red {
      color: #ef2323;
    }

    img {
      border-radius: 20px;
      max-width: 100%;
      height: auto;
      display: block;
      margin: 0 auto;
    }

    .sidebyside {
      display: flex;
      justify-content: center;
      /* Center horizontally */
      align-items: center;
      /* Align images vertically */
      gap: 1em;
      /* Space of 1em between images */
      flex-wrap: wrap;
      /* Wrap to next line if needed */
    }

    .sidebyside img {
      max-width: 100%;
      /* Ensure images are responsive */
      height: auto;
      /* Maintain aspect ratio */
      display: inline;
    }

    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
    }
  </style>
</head>

<body>
  <div class="rune-border">
    <div class="vertical-sides"></div>
    <div class="container">
      <h1>Pernicious Prophecy 70B</h1>
      <p>
        <img src="./header.gif" alt="Pernicious Prophecy 70B GIF" />
      </p>
      <h2 style="margin-top: 0em; padding-top: 0em;">Jump Straight In...</h2>
      <p>
        <a href="#settings">Click here for downloads & settings</a>
      </p>
    </div>
    <div class="rune-separator"></div>
    <h2 style='padding-top:0.5em;'>An Introduction...</h2>
    <p>
      <b>Pernicious Prophecy 70B</b> is a Llama-3.3 70B-based, two-step model designed by <a
        href="https://huggingface.co/Black-Ink-Guild">Black Ink Guild</a> (<a 
        href="https://huggingface.co/SicariusSicariiStuff">SicariusSicariiStuff</a> and <a 
        href="https://huggingface.co/invisietch">invisietch</a>) for uncensored roleplay, assistant tasks, and general 
      usage.
    </p>
    <p class="red">
      <b>NOTE:</b> Pernicious Prophecy 70B is an uncensored model and can produce deranged, offensive, and dangerous
      outputs. You are solely responsible for anything that you choose to do with this model.
    </p>
    <p>
      If you have any issues or just want to chat about Pernicious Prophecy &amp; future Black Ink Guild releases, join
      <a href="https://discord.gg/gXQzQcnedb">our Discord server</a>.
    </p>
    <div class="rune-separator"></div>
    <h2 id="settings">Engage the Model...</h2>
    <h3>Model Downloads</h3>
    <p>
      FPX: 
      <a href="https://huggingface.co/Black-Ink-Guild/Pernicious_Prophecy_70B">FP16 (HF)</a> |
      <a href="https://huggingface.co/Black-Ink-Guild/Pernicious_Prophecy_70B_FP8">FP8 (Aph.)</a>
    </p>
    <p>
      GGUF: 
      <a href="https://huggingface.co/Black-Ink-Guild/Pernicious_Prophecy_70B_GGUF_Q4_K_S">Q4_K_S</a> |
      <a href="https://huggingface.co/Black-Ink-Guild/Pernicious_Prophecy_70B_GGUF_Q4_K_M">Q4_K_M</a> |
      <a href="https://huggingface.co/mradermacher/Pernicious_Prophecy_70B-GGUF">mradermacher</a>
    </p>
    <p>
      EXL2: 
      <a href="https://huggingface.co/Black-Ink-Guild/Pernicious_Prophecy_70B-3.5bpw">3.5bpw</a> |
      <a href="https://huggingface.co/Black-Ink-Guild/Pernicious_Prophecy_70B-5.0bpw">5.0bpw</a>
    </p>
    <p>
      GPTQ: 
      <a href="https://huggingface.co/Black-Ink-Guild/Pernicious_Prophecy_70B_GPTQ">GPTQ-4Bit-g32</a>
    </p>
    <h3>Recommended Settings</h3>
    <p>
      Pernicious Prophecy 70B uses the Llama-3 Instruct format, which is available as a preset in all good UIs. The
      sampler settings used in testing are as follows:
    </p>
    <ul>
      <li><b>Instruct Template</b>: Llama-3 Instruct</li>
      <li><b>Context</b>: 32,768</li>
      <li><b>Temperature</b>: 0.9-1.1</li>
      <li><b>Min P</b>: 0.06-0.12</li>
      <li><b>Rep Pen</b>: 1.07-1.09</li>
      <li><b>Rep Pen Range</b>: 1,536</li>
    </ul>
    <p>
      Feel free to use other sampler settings, these are just sane defaults. XTC is good for roleplaying with the model
      but may not be beneficial for other tasks.
    </p>
    <h3>Context Length</h3>
    <p>
      The model has been tested in roleplays using up to <b>32,768 token context</b> at various quantizations and is
      incredibly stable at this context length.
    </p>
    <p>
      It is possible that the context works at even longer context lengths, but it was not deemed within the parameters
      of our testing.
    </p>
    <div class="rune-separator"></div>
    <h2>Sip the Poison...</h2>
    <p>
      Here, you can find example outputs from the LLM to various instructions. For each of these examples, the model was
      inferenced at fp8 with 1.0 temperature, 0.1 min-p, 1.04 repetition penalty, and all other samplers neutralized.
    </p>
    <ul>
      <li>
        <a href="https://huggingface.co/Black-Ink-Guild/Pernicious_Prophecy_70B/blob/main/nasa.md">Write a 2000 word, Markdown-formatted, report for NASA. Evaluate each of Jupiter's moons as a suitable 
          colony with pros & cons, then provide a recommendation.</a>
      </li>
      <li>
        <a href="https://huggingface.co/Black-Ink-Guild/Pernicious_Prophecy_70B/blob/main/tone.md">Write me a 3,000 word opening chapter of a 'gritty hard sci-fi' novel, drawing inspiration from 
          the writing styles of Isaac Asimov & Andy Weir. Use third person personal. Include dialogue and internal monologues. 
          The POV character for the opening chapter should be a 26 year old astronaut called Tone on a mission to Europa, who 
          has just realised that the craft for the return journey is broken beyond repair, and he only has supplies for a few 
          months. Given that survival is impossible, he seeks to spend the few months he has researching titan, so his life 
          &amp; mission are not wasted.</a>
      </li>
      <li>
        <a href="https://huggingface.co/Black-Ink-Guild/Pernicious_Prophecy_70B/blob/main/cookie.md">Build me a basic cookie clicker game in HTML & Javascript.</a><br />
      </li>
    </ul>
    <p>
      These examples were all the best of 2 responses.
    </p>
    <div class="rune-separator"></div>
    <h2>The Codex...</h2>
    <p>
      Here, you can find some useful prompting tips for working with Pernicious Prophecy 70B.
    </p>
    <h3>Formatting</h3>
    <p>
      'Use markdown' and 'use formatting' are likely to produce the best formatted output. We decided to train these on
      trigger words to avoid random Markdown in roleplay replies.
    </p>
    <h3>System Prompting</h3>
    <p>
      Pernicious Prophecy 70B is very sensitive to prompting, even over long context. The more you instruct it, the more 
      it will know what you want it to do.
    </p>
    <p>
      'Avoid purple prose, avoid cliches, avoid deus ex machinae' is a useful prompt snippet for roleplaying purposes.
      For best results, don't use your roleplay prompt when using Pernicious Prophecy as an assistant.
    </p>
    <div class="rune-separator"></div>
    <h2>Assembling the Repertoire...</h2>
    <p>
      We used a two-step process: a merge step to combine the abilities of some of the best L3 70B models on Huggingface
      and a gentle SFT training step to heal the merge and address some issues around refusals and positivity bias.
    </p>
    <h3>The Merge Step</h3>
    <p>
      First, a
      <code>model_stock</code> merge was applied using four high-quality Llama-3 based models:
    <ul>
      <li>
        <b>SicariusSicariiStuff/Negative_LLAMA_70B</b> - chosen to be the base model, because of its low censorship,
        reduced positivity bias, and engaging writing style
      </li>
      <li>
        <b>invisietch/L3.1-70Blivion-v0.1-rc1-70B</b> - added for its exceptional formatting, roleplay performance,
        and general intelligence.
      </li>
      <li>
        <b>EVA-UNIT-01/EVA-LLaMA-3.33-70B-v0.1</b> - selected for its ability in longer-form storytelling, varied
        outputs, and quality thought.
      </li>
      <li>
        <b>aaditya/Llama3-OpenBioLLM-70B</b> - to add a better understanding of anatomy, and another long-form reasoning
        model to the stack.
      </li>
    </ul>
    </p>
    <h3>The Finetuning Step</h3>
    <p>
      We used a <b>qlora-based</b>, targeted finetune on 2x NVIDIA RTX A6000 GPUs, with a curated dataset of
      approximately 18 million tokens designed to surgically address issues that we identified in the merge.
    </p>
    <p>
      The finetuning took a total of about 14 hours, using Axolotl, and targeted specific high-priority LORA modules
      which allowed us to maintain a 16k sequence length even with 96GB VRAM.
    </p>
    <div class="sidebyside" style="padding-bottom:2em;">
      <a href="https://github.com/arcee-ai/mergekit">
        <img 
          class="badge"
          src="https://huggingface.co/Black-Ink-Guild/READMETEST/resolve/main/mergekit.png" 
          alt="Built with Mergekit" 
          width="200" 
          height="32" 
        />
      </a>
      <a href="https://github.com/axolotl-ai-cloud/axolotl">
        <img 
          class="badge" 
          src="https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/main/image/axolotl-badge-web.png"
          alt="Built with Axolotl" 
          width="200" 
          height="32" 
        />
    </div>
  </div>
</body>

</html>
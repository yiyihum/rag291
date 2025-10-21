---
license: mit
library_name: transformers
datasets:
- R2E-Gym/R2E-Gym-Subset
language:
- en
base_model:
- Qwen/Qwen3-32B
pipeline_tag: text-generation
---

<!-- Header Section -->
<div align="center" style=" padding: 1.5em 1.5em;  margin-bottom: 1em;">

  <!-- Logo and Title -->
  <div style="display: flex; align-items: center; justify-content: center; gap: 1em; margin-bottom: 0.5em;">
    <div style="width: 2.5em; height: 2.5em; border-radius: 1em; display: flex; align-items: center; justify-content: center;">
      <img src="https://hebbkx1anhila5yf.public.blob.vercel-storage.com/IMG_3783-N75vmFhDaJtJkLR4d8pdBymos68DPo.png" alt="DeepSWE logo" style="width: 2.5em; height: 2.5em;">
    </div>
    <h1 style="font-size: 2.5em; font-weight: 150; margin: 0; font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', sans-serif; letter-spacing: -0.02em;">DeepSWE-Preview</h1>
  </div>

  <!-- Subtitle -->
  <p style="font-size: 1em; color: #a1a1aa; margin: 0 0 0 0; font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif; line-height: 1.5; font-weight: 400;">
    Democratizing Reinforcement Learning for LLM Agents
  </p>


</div>

<div align="center" style="line-height: 1;">
  <!-- Trained with rLLM Badge -->
  <a href="https://github.com/agentica-project/rllm" style="margin: 2px;">
  <div style="display: inline-flex; align-items: center; gap: 0.5em; background: rgba(255, 255, 255, 0.1); padding: 0.5em 1em; backdrop-filter: blur(0.5em); transition: all 0.3s ease;">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
    </svg>
    <span style="font-size: 0.75em; font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif; font-weight: 500; letter-spacing: 0.02em;">Trained with rLLM</span>
  </div>
  </a>

  <a href="https://pretty-radio-b75.notion.site/DeepSWE-Training-a-Fully-Open-sourced-State-of-the-Art[%E2%80%A6]-by-Scaling-RL-22281902c1468193aabbe9a8c59bbe33" target="_blank" style="margin: 2px;">
    <img alt="Blog" src="https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://x.com/Agentica_" style="margin: 2px;">
    <img alt="X.ai" src="https://img.shields.io/badge/Agentica-white?style=for-the-badge&logo=X&logoColor=000&color=000&labelColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://huggingface.co/agentica-org" style="margin: 2px;">
    <img alt="Hugging Face" src="https://img.shields.io/badge/Agentica-fcd022?style=for-the-badge&logo=huggingface&logoColor=000&labelColor" style="display: inline-block; vertical-align: middle;"/>
  </a>
    <a href="https://www.together.ai" style="margin: 2px;">
    <img alt="Together AI" src="https://img.shields.io/badge/-Together_AI%20-white?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAUAAAAFACAMAAAD6TlWYAAAC7lBMVEUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8AAAAPb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8Pb%2F8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADIBDt6AAAA%2BnRSTlMAAiQEKgcdKQwiHBMUzrtSUEmjhmZGH96yv8n1ey7nL3y1U%2FZfCaIo1WFg1NrcsHYrA2%2Fv80J%2BMeilnpefqKw%2B64%2BQlSbYZGVnBGkCV%2BxW8XJube6WJ9kZF9bSzBALRynPQfLhIjvwyBEAXOTLp3o%2FJA9Y9%2F7%2F9FEKDhIVFo4GHkVzjGz8icrHzY39iHR1i0M8Jj14LLZUvb7DxMXGoQEFeQcgSBOHaPvm4uOdRLMMqcDTLbcII0sNuVn4TKaRd6RKIeDd37Svra6xuLpaW17lXUAlHh8WGxUPIS4JGQoFECMsBg4gFwsRJRIrCC0oAycaFC8NMDIzMRgBsVt9rwAAD25JREFUeNrs3QVzG0kWB%2FA3ikHhZeYwk3LMbF7GcBasOGw9hb3MzLyKw8zMzMx2rsokhySNY2mmR1N4xXV3a7sHuzWu%2BX2Ef3XPG%2Br3wOVyuVwul8vlcrlcLpfL5XK5dOlXOHTIvLnb27Xd%2FasBvrt9A%2B7r1bbdTTffcmuXwhzgTYwk6q%2BHr2RWlcclRYqXV2VeCV%2Bvr4mIkCJKZ83uc9NLC0fMD%2BD%2FCswfMfLtzh%2FeelsJcKJW19SG66KSTP6fLEXrwrU11Srw5Z8zbuzePcUBbFyg%2BPY7Pv%2Bs0A%2Bsid7ayiqFNEWp8iS9Ir%2F0Cl957bkRAaQLFLz15sBBfpbpJc7FJKKFFGuV4JJh6N573g6idr7vP%2F8iC9iI1NZJRDupLnlRBbaW3XjTfQHUJ3D8d68MBtsJiTNRold5uEYAdibkHgqiESMefGi9zfFVeCRihOS5LLJafV99XYxGddgwabKt8SmEyEQ%2FmRDlSoUA9gsNvKMDmhE8MC4L7OFtSYmPFmFlAmzm%2F9tfH0Oz8v6yFmxQ3SpOiY8eYTwjHew0%2BB9%2FD6B5ga4dLd%2FHQus0SnzaIrzWWgDb9P19MVqjw01dwFLpYYVYQymLgD1Kjj6J1umaHwLLqJfpy0%2FHIryqgg2mvetDKxXMnQMWEa9LxEpSqxZguS%2B%2BfA%2Bt9cZBi7ZxeqVMX376FqEnAtbyv7ISrTfspB%2FM82bq3r70BNMSYKV%2Bo4rQDiPzc8Csy1Fih%2BhVsE7o0cfQHnn%2FygJz6uNEJtaTSfy8ChYpnelDuxQ8HAIT1LOS8fwoCSq1FiVYcs%2FdaJ%2FgNhMJqrWKqfwoCSYtSTA08260U%2FBh47v4LDU%2F%2FgnmPOJDexX86ycwpp6yf80neB7M8o96DO2Wl2%2Bw%2FlLrh%2FlKYroW31qE9ht5EgzwRs3nR00wmgBTVq1EFtp2Ad0imdbkR0kwLQImTP8S2eg9B3QSKwkbHhPPxSUzAsjGe3P1luLrMmGklQpGjfIhKwU6C8llibBJUCaS4UKy6klkp0cX0CE9zcr8KAlei4Ahy36PLHXuBJqpYcJSmQBG3LIJWerQETS7qhCWlHowoMvfka2Va0Gjaus3MGUTp4NuWY8ja3%2FuB9q0IqydBt1eeQxZ%2B9MfQRNvnLAWT%2BiuIEuRvT9MBg3UlkQmbMmkUgB9cjsge8EbQIMLCmFPuQy6DPoGeVi9HqgED5EJazL5VAQ9Nm5CHjq0B6oKhZCUX4LrNyAfSycDhVBJZMKeTK4IoN26IPJRsAQoEhLhQ7kAmoV%2Bjbwspt0LniF8yKRMBa1%2B%2BSvkZVFfaFIkSngpvwha%2FQL56QNNqiX8%2FBs0mnMX8vPtBGiCWEf4iYmgzey7kZ8Rw6EJXonwo9SANn9GnuZCE84RnlqBJm3aIk8vFUKjxBjhKbMFaDHQhzy9%2BAI06pJEeJIS%2FGuwBn1M1WD%2BdXjNauSrdwk0Qq0kfHlUoFs7Evnq9TI0orqK8BVN1%2FIcvAn56vAKNCKhEDruz8NjkbdXOV4CKZJA1W8M8vbjT9CwMOGtDKjmjEbefpgCDRLqCB33p7kvipC3kc83UkOihLdohF5DfMjbiBf43UZTSPQq8vobyNsbudCgyzLhTT4PNK8hpmoZPkv4awU0y5G%2F1%2Fj90WG%2BDK9ATNX7mDDh71OgWYn83RHi9yRMkQY0I5G%2FOydDA4RPCX9RoMlD%2Fu6a0mCAMcJfHGh8yN%2BwqdAAMZPwJwFNB%2BRv5TRoQIs0wp%2FiiAB7TG%2B2Abor0L0GmiO5VdicuHsfaE7UfRIxJ80Rz8Kdnfss7L6NoShz8vvAWsLfOUe8kZ7o5DfSm1Pgm8gnTv4msqoIzXC%2FyrUZjWa434XdPxOoRZjiHjTD%2FTcGNm9Cg9y%2Fs9z%2FAymi1e4fqqZ4VPcfaQZnlQYGkacXP3H6X%2FrT2qIZ7jkR%2BAvy9L5jTyq5Z%2BUolBpHnNYc5PDTmubrsHtemOeJ9aJmcWI9tAV5%2BQ29Z4Kc%2Bj0TYHOQVwl5pVl07YD1h9EMt28MHOHUueihZtK5CArvRB4OTWkuvbNgYjGyF5wEGlQ4oXsbrF%2BK7O2fDBoIPPoHegQndLAc14w6WELot8jaX5pVD1Xo8iSy1WM8nzbcFMZbcf%2BLcR%2Fp7qBZayf0kYZly5GlzpOd3Mmcfy%2F9rl1AhwjTXvoXwaATDKc55Dp6mgP%2FeSLvZ4E%2B55wwTwSmr0Y2Djp6og3%2FmUrDhqbuTKWLYMqQ42i%2FkcNTdqpXeQ2Y4z82AO2Wl8txrpz5AkLRr38Q7TUiOydlJxueBfNCYzugnYKvOn62JkXpA3YmGPy8xPnTXanzhYP27d8PSvjPFzafH0Wov12VJC87ZSdcS2dVsEy%2FE8fRDgtznTFj3Tz%2FrT3QesOGO2bKv3mrVr%2BH1nrjjqFgiUilTGRr8%2FNEwHLTZ%2FisLR9vzgGLiOckYiWpVQuwQcmonmidZ3JDYBn1chohslXL79pVFWzh%2F2L5JrRG8fahYKlIWCHWUMoiYJtl%2F3wygOYFunabDBYTWmtdhJTlVy%2BAjfxPPP4YmpW3dTzYID0jTo%2BQEl88Ix1sFlqytAOacfe%2Bk1lgD29LxXiEMiFKZUIF%2By3L%2F6YYjSpu134w2EaouEKPsNH4rlwWgI0JEzcE0Qjfl19NAVsJFR6JGCF5LovAzrId2%2B8LoD6BBT8OGQy2E2rCUaJXebhGALZC9z%2FwUhC18%2F0wc1UWsBFJ1klEOymWvKgCe%2F7CW999xxdAusCI0R99PMgP7IiJczFJY3qtEiLw8tOckw88uKs40FR4xXuWzvzjVD%2BwJnqTlVUKaYpS5Ul6ReCsdOeOmVveKgq%2Bh%2F%2FvveCiu7Zvmz2rFDhRq2tqw7GoJJP%2FJ0vRWFmyplqF1NBv0KmTJz7fumX1d889%2B8yTzzz73Ldfbtm6bdS48RNygDcx3Xu1NqPMUxdLS7uWlhar85RlJK9600VIOf6c0mWDpj391NNtBg0uyfFDSlEF8T%2Ft3eFyqjwTwPGNiKq9eq%2BtqiCeoxZVEcRW4mK%2Bvc%2F5%2Bk7bBSDZOJPfFfwHWkEMG%2B%2BfXChwHMdxHMdxHMdxHMdxHMdxHIeV4yiR%2FyOUS6tHfBxP88Vse74N%2F7mdt7PF%2FHT8EFakbYg0XupvMZ%2Fddt%2F%2Ber27zebFX%2BXSfpQfD%2BMLsX7iMp4fc460%2BfgiqbSD1jSCGH1WXAV1v32OhOm0O1Yh9aUR0sNUYnVyekjBEH9eL%2B2mIY2gilmGdWXvhTKQNnpvkDYrBJgjNluJTchtIDSnBY3TNgLMUEGvbL4Qvhco3WkPbOS%2FNAEGjMay1bsEMjyCJsewXVo5HoFuH5P2b7OsJh9a0har1mn3tmkElXTzPlU%2FUd2nDfnTKH53b%2FTN%2FI7TZp2l7X3QZNPlO6X9jb1pJwUa5J8SuyQ%2Fc2vTFjl0zu%2F8vfrH2O8obdx52jaFjmmZ7HAdQQeOVw1pwxF0StNskd0GWtvsUIfsBB3SNt3m%2FgUtva1402jEfCXm%2BUBLjWkHBZ2gJ3zxHcG51JhWdnQENc%2BYk3O2vz%2F6CEJrBqYcyi9o6E172hJaMjJn876BRjYG0k7QiqFJr7tRo7SdgbSsgBaMzRoe%2BlCbfzWTlkILxqZdj%2FPaaWM0Y%2BtBUwbnrT8%2BoaZPY2kLBc2Ynfi%2FgVo2BtNO0JDRPSf6PtTgm0y7pNCI2KNJewWVqZnZNAH1md93J4HKEsNpb1Abw85P%2FQ%2Bo6GNoOs2H%2BgZo2gQqWqBpA6iNY%2Fe7EVRyXNm%2FMR%2FP%2FotjBRWokCFtK6AOrh1AA6ggkBxpG6hFnImzzLUFKNv2uOec5Q9Qw3kO7N%2BgmT7LjB81asuU1hNQXSyRhyyAULClxVDdHh%2FI4YEzIMzY0vZQWZQhlyyFX6V8aasIqnoinwP86oB8nlBRfkM%2Btxx%2BIaZWpNGf03zkCH4xYk0r7PiuTljALz6R0wQqya%2FI6ZrTHy78acS%2FCSd5hB8dmdNGdlyDCQfiGmz7dVhtkddWWZvWU0D72CGv3Qf84O%2BFP40Wl8irLOAHBXtaDLQDoq0fgnPk9gTaHrnt4Qcz5Bba8T2OcBPwLUGnWXAnmGbILfP5Lm%2BELLX3WSp9v3q0IC0GytcDuT1O8K2TBWlLq58kEJfhOfJbACVEfhN7z20IlDPy2xM3WIymQBkiv57i%2ByZM6ANlh%2FymAr6hpshvB5QVoqW3q%2BKK%2FO5AkchvmMM38iHyk0ApkV%2Ffg294feRXugPoDiCr0n0GtiPdVbid%2BwvfB4op8svcN5F2%2Bu67cDvTV34aM0F%2B4Ss%2FDzzYcW4JSwse%2Byav%2FETa4t9ERhakBS%2F9q5wFaRH%2F6kDaNbf3d2EPXuAyvLd30UQItCdyO9i7bOf5EquzYnvTgpdeH8iflvlAUz3kZf8KVcs%2FBJ%2F2rl1cQxWFvUvhR8xpBVThDfnvAu28SR16UMkEOS3sfdQxgGri0tp%2Fk0Lac39l6T%2FKLbd2AfLVg4rW9t7rPy24BtOiFXJZRda%2BTL%2F6A1Wp0N7BBHu2tFBBZUGJPGRs7QPfMrB9cBExnIV7pM1ZQA0nrvFA9qYlUEc%2B5R9QZddYrymdxn%2Bey5O9g%2BUSqEf0rB3SJ7YMaT0BNRUMEywLa9NkDHWpdzRtYO9413cFtaUXw6NyL76VA4abj%2BL%2BMjys%2BcvaEdePJTQhxmhSKGqkhWjSWEAj0cXagfWpybRdBA0lpbktExJrN5oo36ApNUFTJqpm2gJNGShozOuhGT3P2rSzBy1EfSMbF%2FVTqC01lBZBK%2FHK2q2zisxA2iqGlhKpf%2FO2pGHaXXuafOPfGZKMLJeMO0MSaXNoTz1LvRtYPhXftqlE2lpBB9SayOQ6fgDqqTXtk07jzKSPH00dpL60tbJ9h%2Bb2%2BzODWt7tSKM34tZhlUBrSaYn7Q06Ffc1bKXfj6EDhQ1ptOhcP5OI7EXQibTXedo5gs55gxK7VE68ztImstu0gQcaqGSH%2BOjqHF8S1WXapcO03ZsCPaLxA7tRhhF0Kg1L7MZjHIE24os%2B05X%2B%2FL6ErWm7pQCd0ndJdxKN93cfNPDf763T5CwFzVTcK%2BnOXxrLXqE0pRXbtmmxAv3EaUp3%2Ftg4PQlL0x7TRIAZeXIusYnyfMo1p50apyU5mCOCcIV1rcJA2J9mivqzvpZYXXldR8pQWlQ77Y8CBnk8GFYLlcNBnJtNmwwlVlH%2Bl%2BYBG69Yn7Py98Ksty48lrQemXY2kEZRfvAMr5l84P97yOwaPgNfWZq2NpZG86JgPhlP%2B9ldlo9S3rP%2BdDyZB5FnRdqygzTHcRzHcRzHcRzHcRzHcZz%2FAbyvLkVmYcs9AAAAAElFTkSuQmCC&link=https%3A%2F%2Fwww.together.ai" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>
</div>
</div>


## DeepSWE Overview
DeepSWE-Preview is a fully open-sourced, state-of-the-art coding agent trained with only reinforcement learning (RL) to excel at software engineering (SWE) tasks. DeepSWE-Preview demonstrates strong reasoning capabilities in navigating complex codebases and viewing/editing multiple files, and it serves as a foundational model for future coding agents. The model achieves an impressive **59.0%** on SWE-Bench-Verified, which is currently #1 in the open-weights category.

DeepSWE-Preview is trained on top of Qwen3-32B with thinking mode enabled. With just 200 steps of RL training, SWE-Bench-Verified score increases by ~20%.

Discover more about DeepSWE-Preview's development and capabilities in our [technical blog post](https://pretty-radio-b75.notion.site/DeepSWE-Training-a-Fully-Open-sourced-State-of-the-Art[%E2%80%A6]-by-Scaling-RL-22281902c1468193aabbe9a8c59bbe33).

<div style="margin: 0 auto;">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/654037be97949fd2304aab7f/FbSSr0XQRYfnoiczStZ-E.png" style="width: 100%;" />
  <p align="center" style="margin-top: 8px; font-style: italic; color: #666;">
    Figure 1: SWE-Bench-Verified Performance vs. Model Size for LLM Agents. Trained with only reinforcement learning (RL, no SFT), DeepSWE-Preview with test time scaling (TTS) solves 59% of problems, beating all open-source agents by a large margin. We note that DeepSWE-Preview's Pass@1 performance (42.2%, averaged over 16 runs) is one of best for open-weights coding agents.
  </p>
</div>

## Usage Recommendations

To get the best performance out of DeepSWE-Preview, we suggest setting:
- Temperature = 1
- Max tokens set to at least 32-64K.
- Use R2EGym's system/instance prompt and tools (`file_editor.py`, `execution_bash.py`, `search.py`, `finish.py`). See [here](https://github.com/agentica-project/R2E-Gym/blob/master/src/r2egym/agenthub/config/r2egym/edit_non_fn_calling.yaml) for more details.


## Training Recipe

<div style="margin: 0 auto;">
  <img src="./figures/swe_val_scores.png" style="width: 100%;" />
  <p align="center" style="margin-top: 8px; font-style: italic; color: #666;">
    Figure 2: Validation Score for SWE-Bench-Hard, where an agent receives positive reward if it submits the final answer and passes all tests. With just 200 steps of RL training, SWE-Bench-Verified score increases from 23→42% (+20%).
  </p>
</div>


### Data 🗄️

Our dataset contains 4.5K problems from a subset of `R2E-Gym`. To avoid data contamination during training, we filtered out problems that are derived from the same repositories as `SWE-Bench-Verified` , such as `sympy`. All problems map to individual Docker images.

### Environment 🌐

Our environment wraps around `R2E-Gym`, an existing Gym environment for scalable curation of high-quality executable SWE environments.

**State & Action.** `R2E-Gym` defines a set of four tools as part of the action space. The output of each tool (a Python program with stdout/stderr) represents the returned state. More specifically:

- **Execute Bash** - Outputs both stdout and stderr of an LLM-generated bash command.
- **Search** - Searches and returns all occurrences of an LLM-defined query in either a directory or a single file.
- **File Editor** - Allows for viewing, creating, replacing strings, inserting, and undoing edits to a specific file.
- **Finish/Submit** - LLM has decided that it has resolved the pull request, which terminates trajectory generation.

**Reward.** To keep things simple, our reward function employs a sparse Outcome Reward Model (ORM):

- `1` - LLM’s generated patch passes a selected sample of tests (Pass2Pass and Fail2Pass) within a time limit. To accelerate training, our max time limit is 5 minutes, while the official SWE-Bench evaluation is 30 minutes.
- `0` - We assign no reward if the LLM’s code fails on at least one test case or times out.

### RL Algorithm

We enhance the original GRPO algorithm, integrating insights from DAPO, Dr. GRPO, LOOP/RLOO, and our innovations to enable stable training and improved performance. Our final, amalgamate algorithm consists of:

- **Clip High (DAPO):** Increasing the upper bound of GRPO/PPO’s surrogate loss encourages exploration and stabilizes entropy.
- **No KL Loss (DAPO):** Eliminating KL loss prevents the LLM from being constrained to the trust region of the original SFT model.
- **No Reward Standard Deviation** **(Dr.GRPO):** Removing reward standard deviation removes difficulty bias in GRPO’s loss, ensuring hard and easy problems are better differentiated.
- **Length Normalization (Dr.GRPO):** Dividing surrogate loss by max context length removes length bias present in GRPO, which increases the length of incorrect responses.
- **Leave One Out (Loop/RLOO):** Removing one sample for advantage estimation reduces variance for policy gradient without introducing bias.
- **Compact Filtering** **(Us):** Inspired by DAPO, we mask the loss for trajectories that reach max context length, timeout during generation (20 minutes), or reach maximum steps.
- **No Entropy Loss (Us):** Entropy loss introduces higher instability and eventually leads to exponentially increasing entropy, which collapses training. Provided that the base model’s token-level entropy is within 0.3-1, entropy loss is not needed.

A more detailed description of the training recipe can be found in our [blog post](https://pretty-radio-b75.notion.site/DeepSWE-Training-a-Fully-Open-sourced-State-of-the-Art[%E2%80%A6]-by-Scaling-RL-22281902c1468193aabbe9a8c59bbe33).


## Evaluation

DeepSWE-Preview is evaluated via the official `R2E-Gym` codebase at 64k max context length and 100 max enviornment steps. DeepSWE's generated patches are then ported over to the offical SWE-bench repo to calculate final score. Below, We report Pass@1 accuracy averaged over 16 runs.

| Model | Scaffold | Type | SWE-Bench Verified (%) |
|-------|----------|------|------------------------|
| DeepSWE-Preview (32B) | R2E-Gym | Agent + Hybrid Best@16 | 59% |
| DeepSWE-Preview (32B) | R2E-Gym | Agent + Hybrid Best@8 | 57.9% |
| DeepSWE-Preview (32B) | R2E-Gym | Agent | 42.2% |
| Devstral-Small (24B) | OpenHands | Agent | 46.6% |
| Openhands-LM (32B) | OpenHands | Agent (Iterative) | 37.2% |
| SWE-Agent-LM (32B) | SWE-Agent | Agent | 40.2% |
| R2EGym-Agent (32B) | R2E-Gym | Agent | 34.4% |
| Skywork-SWE (32B) | OpenHands | Agent | 38.0% |
| Skywork-SWE (32B) | OpenHands | Agent + Execution-Free Best@8 | 47.0% |
| SkyRL-Agent (14B) | OpenHands | Agent | 21.6% |

### Test-time Scaling 

<div style="margin: 0 auto;">
  <img src="./figures/bestk_plot_agent.png" style="width: 100%;" />
  <p align="center" style="margin-top: 8px; font-style: italic; color: #666;">
    Figure 3: SWE-Bench Verified Performance w.r.t. different TTS strategies.  With hybrid TTS, DeepSWE-Preview achieves 59%, beating the current SOTA open-weights model (SkyWork + TTS, 47%) by 12%. We note that only using execution-based and execution-free verifiers is still effective and can bring 10+% performance.
  </p>
</div>


## Serving DeepSWE-Preview

Our model can be served using popular high-performance inference systems:
- vLLM
- Hugging Face Text Generation Inference (TGI)
- SGLang
- TensorRT-LLM

All these systems support the OpenAI Chat Completions API format.

### vLLM (Recommended)

We suggest using `vllm>=0.8.5` and enabling long context in VLLM to serve DeepSWE-Preview.

```bash
export MAX_CONTEXT_LEN=65536
export TENSOR_PARALLEL_SIZE=8
VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 vllm serve agentica-org/DeepSWE-Preview --tensor-parallel-size $TENSOR_PARALLEL_SIZE --max-model-len $MAX_CONTEXT_LEN   --hf-overrides '{\"max_position_embeddings\": $MAX_CONTEXT_LEN}' --enable_prefix_caching
```

## License
This project is released under the MIT License, reflecting our commitment to open and accessible AI development.
We believe in democratizing AI technology by making our work freely available for anyone to use, modify, and build upon.
This permissive license ensures that researchers, developers, and enthusiasts worldwide can leverage and extend our work without restrictions, fostering innovation and collaboration in the AI community.

## Acknowledgement
- Our training experiments are powered by [rLLM](https://github.com/agentica-project/rllm), which builds on top of [Verl](https://github.com/agentica-project/verl), an open-source RLHF library.
- Our model is trained on top of [`Qwen/Qwen3-32B`](https://huggingface.co/Qwen/Qwen3-32B).
- Our work is done as part of  [Berkeley Sky Computing Lab](https://skycomputing.berkeley.edu/) and [Berkeley AI Research](https://bair.berkeley.edu/).

## Citation 
```bibtex
@misc{deepswe2025,
  title={DeepSWE: Training a State-of-the-Art Coding Agent from Scratch by Scaling RL},
  author={Michael Luo, Naman Jain, Jaskirat Singh, Sijun Tan, Ameen Patel, Qingyang Wu, Alpay Ariyak, Colin Cai, Tarun Venkat, Shang Zhu, Ben Athiwaratkun, Manan Roongta, Ce Zhang, Li Erran Li, Raluca Ada Popa, Koushik Sen, Ion Stoica},
  howpublished={\url{N/A}},
  note={Notion Blog},
  year={2025}
}
```

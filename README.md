# **TETR.IO Connected Skin Generator**
Generate a Tetr.io connected skin from minimal input as possible. You only had to draw each piece of mino and garbage to generate connected skin.

You're still required to use [TETR.IO PLUS](https://gitlab.com/UniQMG/tetrio-plus) to be able to use skins.

# Tutorial Video
Coming soon

# Usage Guide
If you don't fancy installing python yourself or are unfamiliar with python, you may try using one of the executables that are available on the [releases](https://github.com/Trisnox/tetrio-connected-skin-generator/releases) tab, just run the executable and follow/input the interactive message, simple as that.

Linux was packaged on WSL using pyinstaller and never tested before since I don't use any linux os, I can't guarantee if this works for you.

Otherwise follow along this guide.

## Requirements
- [Python](https://www.python.org/) 3.7+
- [pillow](https://pypi.org/project/Pillow/)

## Installation
After you downloaded python, make sure to check [Add Python to PATH](https://cdn.discordapp.com/attachments/558246912982122526/990973262999744522/unknown.png) before installation.

After python is installed on your machine, open command prompt and type:
```
pip install pillow
```

And then, download this repository as zip. [If you don't know how to](https://cdn.discordapp.com/attachments/558246912982122526/990994256862789662/unknown.png)

## Usage
Assuming you already created your skin from the template that I provided and have installed python, simply type:
```
[windows] python main.py
[linux]   python3 main.py
```
on the current folder where this script is located. An interactive message will then appears for you to follow/input.

The result should look like [this](https://cdn.discordapp.com/attachments/558246912982122526/990968622585376838/result_1x.png) and/or [this, for disabled](https://cdn.discordapp.com/attachments/558246912982122526/990968622837030942/disabled.png).

## Help
If you require further assistance, you can contact me through my discord (K·#4963) or any [social media](https://web.tris07.repl.co/) that I had.

# to-do
- Advanced connected skin generation which consists of 2-4 image pieces per mino for better result.
- Universal skin generation which only takes 4-5 input/images, similiar to standard but only generate a single chunk of block (similiar to how disabled was generated).
- Since the way how singular block (1x1) generated was messy, it would be wise to make it as optional input.
- Either a standalone app (.exe) with a GUI or a web to generate skin instead of CLI.

# Notes
If there's a folder in the current directory where this script is run, you can choose a folder without having to drag & drop, this process is instantaneous if there's only a single folder within the directory.

On windows, you can click on the address bar on file explorer and then type `cmd` to open command prompt in the current directory.

Some part of the skin were intentionally left empty because only couple portion are visible when rotated/skimmed.

I was using Python 3.8 and Pillow 9.1.1 for this script, result might differ if you use a lower version than this. This isn't the case if you used the executable.
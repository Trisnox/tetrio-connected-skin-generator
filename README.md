# **TETR.IO Connected Skin Generator**
Generate a Tetr.io connected skin from minimal input as possible. You only had to draw each piece of mino and garbage to generate connected skin.

You're still required to use [TETR.IO PLUS](https://gitlab.com/UniQMG/tetrio-plus) to be able to use skins.

# Tutorial Video
Coming soon

# Usage Guide
## Requirements
- [Python](https://www.python.org/) 3.7+
- [pillow](https://pypi.org/project/Pillow/)

## Installation
After you downloaded python, make sure to check [Add Python to PATH](https://cdn.discordapp.com/attachments/558246912982122526/990973262999744522/unknown.png) before installation.

After python is installed on your machine, open command prompt and type:
```
python -m pip install pillow
```

And then, download this repository as zip. [If you don't know how to](https://cdn.discordapp.com/attachments/558246912982122526/990994256862789662/unknown.png)

## Usage
Assuming you already created your skin from the template that I provided and have installed python, simply type:
```
python main.py
```
on the current folder where this script is located. An interactive message will then appears for you to follow/input.

The result should look like [this](https://cdn.discordapp.com/attachments/558246912982122526/990968622585376838/result_1x.png) and/or [this, for disabled](https://cdn.discordapp.com/attachments/558246912982122526/990968622837030942/disabled.png).

## Help
If you require further assistance, you can contact me through my discord (K·#4963) or any [social media](https://web.tris07.repl.co/) that I had.

# to-do
- Non trivially connected skin generation which consists of 2-4 image pieces per mino for better result.
- Either a standalone app (.exe) or a web to generate skin instead of CLI.

# Notes
If there's a folder in the current directory where this script is run, you can choose a folder without having to drag & drop, this process is instantaneous if there's only a single folder within the directory.

On windows, you can click on the address bar on file explorer and then type `cmd` to open command prompt in the current directory.

Some part of the skin were intentionally left empty because only couple portion are visible when rotated/skimmed.

I was using Python 3.8 and Pillow 9.1.1 for this script, result might differ if you use a lower version than this.
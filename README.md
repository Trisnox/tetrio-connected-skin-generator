# **TETR.IO Connected Skin Generator**
Generate a Tetr.io connected skin from minimal input as possible. You only had to draw each piece of mino and garbage to generate connected skin.

You're still required to use [TETR.IO PLUS](https://gitlab.com/UniQMG/tetrio-plus) to be able to use skins.

# Tutorial Video
Coming soon

# Usage Guide
If you don't fancy installing python yourself or are unfamiliar with python, you may try using one of the executables that are available on the [releases](https://github.com/Trisnox/tetrio-connected-skin-generator/releases) tab, just run the executable, GUI will then appear, simple as that.

Linux was packaged on WSL using pyinstaller and never tested before since I don't use any linux os, I can't guarantee if this works for you.

Otherwise follow along this guide.

# Running from source
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
on the current folder where this script is located. A GUI will then appear.

# Name Keys
Skin files should be named correctly in order for the script to detect and use them, it only support `.png` and `.jpg` formats. You can find example skin for each method in the [example_skin](https://github.com/Trisnox/tetrio-connected-skin-generator/tree/main/example_skin) folder.

Here are the list of name keys.

| Method | Essential | Optional | Input | Output | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| Universal | `s` `t` `o` `i` | `singular` `3x3` | ![input](https://cdn.discordapp.com/attachments/558246912982122526/992806646231351426/quilt.png) | ![chunk.png](https://cdn.discordapp.com/attachments/558246912982122526/991660114635391047/result.png) ![garbage](https://cdn.discordapp.com/attachments/558246912982122526/992806237794226247/garbage.png) | `3x3` will be used for garbage, otherwise, it will use `o` and `i`.<br/><br/>All images must be symmetrical and identical, garbage is not required to be identical but requires symmetrical<br/><br/>After the image is generated, you had to color and merge the result/garbage on your own.<br/><br/>Singular will be generated if you didn't provide one. |
| Standard | `s` `z` `l` `j` `t` `o` `i` `gb` `gbd`  | `u_disabled` `s_singular` `z_singular` `l_singular` `j_singular` `t_singular` `o_singular` `i_singular` `gb_singular` `gbd_singular` | ![input](https://cdn.discordapp.com/attachments/558246912982122526/991660772759445564/quilt.png) | ![result_1x.png](https://cdn.discordapp.com/attachments/558246912982122526/991653621206896691/result_1x.png) | `u_disabled` is a chunk that was generated by the `Universal` method or through the `chunk` disabled generation option, you can use this result for the disabled, otherwise, one will be generated depending on the choice that you picked.<br/><br/>Each pieces/images must be symmetrical.<br/><br/>Each minos may have different variation.<br/><br/>Singular will be generated if you didn't provide one. |
| Mixed | `s1` `s2` `t1` `t2` `t3` `t4` `o1` `i1` `i2` | `3x3_1` `3x3_2` `3x3_3` `gb_singular`<br />`singular` | ![input](https://cdn.discordapp.com/attachments/558246912982122526/992805698431881216/quilt.png) | ![result_1x.png](https://cdn.discordapp.com/attachments/558246912982122526/992805776903123056/chunk_1x.png) ![garbage](https://cdn.discordapp.com/attachments/558246912982122526/992806072643506258/garbage.png) | `3x3` and `gb_singular` will be used for garbage, otherwise, it will use `o` `i` and/or `singular`.<br/><br/>Symetric is not needed for this one, but identical is required.<br/><br/>Singular won't be generated if not provided. |
| Advanced | `s1` `s2`<br />`z1` `z2`<br />`l1` `l2` `l3` `l4`<br />`j1` `j2` `j3` `j4`<br />`t1` `t2` `t3` `t4`<br /> `o1` `o2` `o3`<br />`i1` `i2`<br />`gb1` `gb2` `gb3`<br /> `gbd1` `gbd2` `gbd3` | `t5` `t6` `t7` `t8` `t9` `t10` `u_disabled` `s_singular` `z_singular` `l_singular` `j_singular` `t_singular` `o_singular` `i_singular` `gb_singular` `gbd_singular` | ![input](https://cdn.discordapp.com/attachments/558246912982122526/992521911680643073/quilt.png) | ![result_1x.png](https://cdn.discordapp.com/attachments/558246912982122526/992522394239520828/result_1x.png) | `u_disabled` is a chunk that was generated by the `Universal` method or through the `chunk` disabled generation option, you can use this result for the disabled, otherwise, one will be generated depending on the choice that you picked.<br/><br/>Symmetric and identic are not needed for this method.<br/><br/>`t5-10` are used for corner turn for T-shape, it won't be generated if not provided.<br/><br/>Singular won't be generated if not provided.|

# GUI info
## Generate
Generate skin based on the skin location and options that you selected.

## Merge
Merge `result.png` and `disabled.png`, by default this uses export location instead of the skin location. This is optional for `Standard` and `advanced` as you can provide `u_disabled` instead.

## Skin Generation Method
By default, this uses automatic, which guess what kind of skin you are trying to export by preserving file names. Refer to the [name keys](https://github.com/Trisnox/tetrio-connected-skin-generator#name-keys) for more info on each method.

## Disabled Generation
Wherever to generate or use flat color for disabled mino. This option is ignored for universal and standard (if you have `u_disabled` file).

## Export 1x
Small QOL as TETR.IO PLUS fails to import if you try to drag and drop the 2x file.

# Help
If you require further assistance, you can contact me through my discord (K·#4963) or any [social media](https://web.tris07.repl.co/) that I had.

# to-do
- Possibly a web.

# Notes
GUI will autofill the `Skin location` if there's only a single folder inside the directory. This, however, does not have checks unlike the CLI version.

Some part of the skin were intentionally left empty because only couple portion are visible when rotated/skimmed.

I was using Python 3.8 and Pillow 9.1.1 for this script, result might differ if you use a lower version than this. This isn't the case if you used the executable.

# Changelogs
July 2 2022:
- Added `Mixed` example skin
- Added an example skin of ghost minos
- Add support for singular garbage for `Mixed` method
- Bug fixes: `ValueError: bad transparency mask` when tried to paste RGB on RGBA images, oversight on `Mixed` method checks

July 1 2022:
- Added `Mixed` skin generation method
- Added `Advanced` skin generation method and example skin
- First major release as all essential features have been added
- Code improvement
- Bug fixes: checks will start from longest name first as it conflict with others, double append that caused by `automatic` method which result in double `s` name keys

June 29 2022:
- Added GUI. Since I'm using WSL, I can no longer try to run the linux executable
- Added `Universal` skin generation method

June 28 2022:
- Attempted cross platform support (windows/linux)
- Bundled an executable for windows and linux, both were tested and works

June 27 2022:
- Initial release
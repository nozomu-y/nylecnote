# nylecnote

LaTeX style for note taking.

## Requirements

### Packages

All of these packages are contained in TeX Live.

- amsmath
- amssymb
- amsthm
- atbegshi
- graphix
- hyperref
- listings
- mathtools
- pxjahyper
- tcolorbox
- tikz
- tikzpagenodes
- tikzscale
- titlesec
- titletoc
- varwidth
- xcolor-material

### Images

nylecnote needs the following images.  
Please download the png from the following link and rename them.

- [Lightbulb](https://www.silhouette-illust.com/illust/23161)
  : rename it to `lightbulb.png`
- [Pencil](https://www.silhouette-illust.com/illust/14517)
  : rename it to `pencil.png`
- [Treble Clef](https://www.silhouette-illust.com/illust/20231)
  : rename it to `treble_clef.png`
- [Eighth Note](https://www.silhouette-illust.com/illust/21129)
  : rename it to `eighth_note.png`

Put the files you downloaded in the `icons` folder.

#### change_color.py

In the `icons` folder, you can find `change_color.py`.  
Running this python file will convert the color of your images.

```
cd icons/
python3 change_color.py
```

## Installation

In order to use the package, you will need to place `nylecnote.sty` and `icons` file in the appropriate directory.  
In the command line, execute

```
> kpsewhich multicol.sty
/usr/local/texlive/2020/texmf-dist/tex/latex/tools/multicol.sty
```

This command tells you where `multicol.sty` is placed.  
Now, since you know where to place the files, execute the following commands.

```
> cd /usr/local/texlive/2020/texmf-dist/tex/latex/
> mkdir nylecnote
```

In the `nylecnote` folder, place `nylecnote.sty` and `icons` folder.
Your folder should look like this.

```
nylecnote
├── icons
│   ├── change_color.py
│   ├── eighth_note.png
│   ├── exclamation.png
│   ├── lightbulb.png
│   ├── pencil.png
│   └── treble_clef.png
└── nylecnote.sty
```

Finally, execute the following commands.

```
# MacOS
> sudo mktexlsr

# Windows
> mktexlsr
```

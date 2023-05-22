## highyield <a href="https://kenf1.github.io/Rendered/highyield%20Documentation/"><img src="https://raw.githubusercontent.com/kenf1/Rendered/main/Hex_Sticker/High-Yield.png" align="right" height="138.5" /></a>

[![PyPI](https://img.shields.io/pypi/v/highyield.svg)](https://pypi.org/project/highyield) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-brightgreen.svg)](https://www.gnu.org/licenses/gpl-3.0) [![](https://img.shields.io/badge/-Documentation-yellow)](https://kenf1.github.io/Rendered/highyield%20Documentation/)

`highyield` is a Python package containing a collection of high-yield functions (grouped by modules) intended to simplify and automate specific tasks.

This package requires Python >= 3.8 due to reliance on [`pandas` package](https://pypi.org/project/pandas/).

### Install

To install, open the terminal and type in the following.

For Windows and Linux:

```{python}
pip install highyield
```

For macOS:

```{python}
python3 -m pip install highyield
```

### Dependencies

The table below lists the dependencies for each module within this package:

| Module    | Packages             |
| --------- | -------------------- |
| basics    | os, requests         |
| converter | os, pandas, docx2pdf |
| copy      | os, shutil, pandas   |
| create    | os, shutil           |
| imports   | importlib, pandas    |
| pdf       | os, pypdf            |
| rename    | os, re               |
| tts       | pyttsx3, pandas      |

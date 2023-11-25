## highyield <a href="https://vignettes.netlify.app/highyield"><img src="https://vignettes.netlify.app/hexsticker/highyield.png" align="right" height="138.5" /></a>

[![PyPI](https://img.shields.io/pypi/v/highyield.svg)](https://pypi.org/project/highyield) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-brightgreen.svg)](https://www.gnu.org/licenses/gpl-3.0) [![](https://img.shields.io/badge/-Documentation-yellow)](https://vignettes.netlify.app/highyield)

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

|Module|Module description|Dependencies|
|---|---|---|
|basics|Automation tasks|os, requests|
|converter|Convert from 1 file format to another|os, pandas, docx2pdf|
|copy|Copy & paste local files|os, shutil, pandas|
|create|Create folder(s) + structure from template|os, shutil|
|ds|Data Science|seaborn|
|imports|Import packaged files|importlib, pandas|
|pdf|Work with pdf files|os, pypdf|
|rename|Automate renaming files|os, re|
|tts|Text to speech|pyttsx3, pandas|

# VividHues :rainbow: :paintbrush: :package:

[![Publish VividHues to PyPI & TestPyPI](https://github.com/KennyOliver/VividHues/actions/workflows/publish_to_test_pypi.yml/badge.svg)](https://github.com/KennyOliver/VividHues/actions/workflows/publish_to_test_pypi.yml)

![CodeFactor](https://www.codefactor.io/repository/github/KennyOliver/vividHues/badge?style=for-the-badge)
![Latest SemVer](https://img.shields.io/github/v/tag/KennyOliver/vividHues?label=version&sort=semver&style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/KennyOliver/vividHues?style=for-the-badge)
![Total Lines](https://img.shields.io/tokei/lines/github/KennyOliver/vividHues?style=for-the-badge)

<!-- [![repl](https://repl.it/badge/github/KennyOliver/vividHues)](https://repl.it/@KennyOliver/vividHues) -->

**VividHues is a lightweight Python package for coloured strings in the Python console!**

<a href="https://pypi.org/project/VividHues/"><img src="https://img.shields.io/badge/PyPi-3775A9?style=for-the-badge&logo=pypi&logoColor=white" /></a>

## :hammer_and_wrench: Official Installation
Use this command to install VividHues.
```bash
pip install vividhues
```
Or, alternatively, add it as a dependency.

## :toolbox: Python Example

<img src="vividhues-demo.jpg" align="right" />

```python
from VividHues import Clr


# f-strings Recommended Method
print(f"{Clr.BOLD + Clr.UNDERLINE + Clr.LIME}I love VividHues!{Clr.RESET}")
any_string = f"{Clr.BOLD + Clr.CYAN}Hello {Clr.GREEN}earthlings!{Clr.RESET}"
print(any_string)


# Alternatives
name = input(Clr.PINK + "What's your name?\n\t--> " + Clr.RESET + Clr.UNDERLINE)
print(Clr.RESET + Clr.BOLD + "Hello,", Clr.RED + Clr.UNDERLINE + name + Clr.RESET)
```

<details><summary>:rainbow: Available colours:</summary>

#### _COLOURS_
* RED
* ORANGE
* YELLOW
* LIME
* GREEN
* BLUE
* CYAN
* PURPLE
* PINK
* BLACK
* WHITE

#### _FORMATTING_
* UNDERLINE
* BOLD
* RESET

</details>

---
Kenny Oliver ©2021

# VividHues :rainbow: :paintbrush: :package:

[![Publish VividHues to PyPI & TestPyPI](https://github.com/KennyOliver/VividHues/actions/workflows/publish_to_test_pypi.yml/badge.svg)](https://github.com/KennyOliver/VividHues/actions/workflows/publish_to_test_pypi.yml)

![CodeFactor](https://www.codefactor.io/repository/github/KennyOliver/vividHues/badge?style=for-the-badge)
![Latest SemVer](https://img.shields.io/github/v/tag/KennyOliver/vividHues?label=version&sort=semver&style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/KennyOliver/vividHues?style=for-the-badge)
![Total Lines](https://img.shields.io/tokei/lines/github/KennyOliver/vividHues?style=for-the-badge)

<!-- [![repl](https://repl.it/badge/github/KennyOliver/vividHues)](https://repl.it/@KennyOliver/vividHues) -->

**VividHues is a lightweight Python package for coloured strings in the Python console!**
Check it out on PyPi

## Official Installation
```python
from VividHues import Clr
```

## :toolbox: How to use VividHues

<img src="vividhues-demo.png" align="right" />

```python
# Recommended Method
print(f"{Clr.BOLD + Clr.UNDERLINE + Clr.GREEN}I love VividHues!{Clr.RESET}")
any_string = f"{Clr.BOLD + Clr.CYAN}Hello {Clr.GREEN}earthlings!{Clr.RESET}"


# Alternatives
print(Clr.RED + "I love VividHues!" + Clr.RESET)
name = input(Clr.CYAN + "What's your name?\n\t--> " + Clr.RESET)
# For input() use plusses, not commas!
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

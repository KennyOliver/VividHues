# VividHues :rainbow: :paintbrush: :package:

[![VividHues](https://github.com/KennyOliver/VividHues/actions/workflows/publish_to_test_pypi.yml/badge.svg)](https://github.com/KennyOliver/VividHues/actions/workflows/publish_to_test_pypi.yml)

![CodeFactor](https://www.codefactor.io/repository/github/KennyOliver/vividHues/badge?style=for-the-badge)
![Latest SemVer](https://img.shields.io/github/v/tag/KennyOliver/vividHues?label=version&sort=semver&style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/KennyOliver/vividHues?style=for-the-badge)
![Total Lines](https://img.shields.io/tokei/lines/github/KennyOliver/vividHues?style=for-the-badge)

<!-- [![repl](https://repl.it/badge/github/KennyOliver/vividHues)](https://repl.it/@KennyOliver/vividHues) -->

**VividHues: super lightweight package for coloured strings in Python!**

<a href="https://pypi.org/project/VividHues/"><img src="https://img.shields.io/badge/PyPi-3775A9?style=for-the-badge&logo=pypi&logoColor=white" /></a>

## :hammer_and_wrench: Official Installation
Use this command to install VividHues.
```bash
pip install VividHues
```

### :bricks: Dependency
_requirements.txt_
```VividHues>=2.7.9```

_Dependabot.yml_
```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "daily"
```


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
print(Clr.RESET + Clr.BOLD + "Hello,", Clr.RED + Clr.UNDERLINE + name)
```

## :rainbow: Available colours:

| Colour Codes | Formatting Codes |
| :----------: | :--------------: |
| Clr.RED      | Clr.UNDERLINE    |
| Clr.ORANGE   | Clr.BOLD         |
| Clr.YELLOW   | Clr.RESET        |
| Clr.LIME     |                  |
| Clr.GREEN    |                  |
| Clr.BLUE     |                  |
| Clr.CYAN     |                  |
| Clr.PURPLE   |                  |
| Clr.PINK     |                  |
| Clr.BLACK    |                  |
| Clr.WHITE    |                  |

---
Kenny Oliver ©2021

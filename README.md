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
```
VividHues>=2.7.9
```

_Dependabot.yml_
```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "daily"
```

_Dockerfile_
```dockerfile
RUN pip install VividHues

# or

COPY requirements.txt .
RUN pip install -r requirements.txt
```


## :toolbox: Python Example

<img src="vividhues-demo.jpg" align="right" />

```python
from VividHues import Clr


# f-strings - recommended
print(f"{Clr.BO + Clr.UNDERLINE + Clr.LIME}I love VividHues!{Clr.RS}")
any_string = f"{Clr.BO + Clr.CYAN}Hello {Clr.GREEN}earthlings!{Clr.RS}"
print(any_string)


# alternatives
name = input(Clr.PINK + "What's your name?\n\t--> " + Clr.RS + Clr.UL)
print(Clr.RS + Clr.BO + "Hello,", Clr.RED + Clr.UL + name)
```

## :rainbow: Available colours:

| Colour Codes | Formatting Codes | Formatting Code Abbreviations |
| :----------: | :--------------: | :---------------------------: |
| Clr.RED      | Clr.UNDERLINE    | Clr.UL |
| Clr.ORANGE   | Clr.BOLD         | Clr.BO |
| Clr.YELLOW   | Clr.RESET        | Clr.RS |
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

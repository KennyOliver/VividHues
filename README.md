# VividHues :rainbow: :package:

![CodeFactor](https://www.codefactor.io/repository/github/KennyOliver/vividHues/badge?style=for-the-badge)
![Latest SemVer](https://img.shields.io/github/v/tag/KennyOliver/vividHues?label=version&sort=semver&style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/KennyOliver/vividHues?style=for-the-badge)
![Total Lines](https://img.shields.io/tokei/lines/github/KennyOliver/vividHues?style=for-the-badge)

<!-- [![repl](https://repl.it/badge/github/KennyOliver/vividHues)](https://repl.it/@KennyOliver/vividHues) -->

VividHues is a lightweight Python package for coloured strings in the Python console!


## :package: Installation & Update:
### Step 1
![Bash](https://img.shields.io/badge/GNU%20Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)
```bash
# Use this in a Bash file - e.g. '.replit'
pip install git+https://github.com/KennyOliver/VividHues.git#VividHues
```

### Step 2
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
```python
from VividHues import Clr
```

## :toolbox: How to use VividHues:
```python
# Recommended Method
print(f"{Clr.Bold + Clr.UNDERLINE + Clr.GREEN}I love VividHues!{Clr.RESET}")

# Alternatives
print(Clr.RED + "I love VividHues!" + Clr.RESET)
name = input(Clr.CYAN + "What's your name?\n\t--> " + Clr.RESET)
# For input() use plusses, not commas!
```

<details><summary>:rainbow: Available colours:</summary>

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
* UNDERLINE
* BOLD
* RESET

</details>

---
Kenny Oliver ©2021

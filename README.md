# VividHues :rainbow: :package:

[![VividHues](https://github.com/KennyOliver/VividHues/actions/workflows/python-publish.yml/badge.svg)](https://github.com/KennyOliver/VividHues/actions/workflows/python-publish.yml)

![CodeFactor](https://www.codefactor.io/repository/github/KennyOliver/vividHues/badge?style=for-the-badge)
![Latest SemVer](https://img.shields.io/github/v/tag/KennyOliver/vividHues?label=version&sort=semver&style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/KennyOliver/vividHues?style=for-the-badge)
![Total Lines](https://img.shields.io/tokei/lines/github/KennyOliver/vividHues?style=for-the-badge)

<!-- [![repl](https://repl.it/badge/github/KennyOliver/vividHues)](https://repl.it/@KennyOliver/vividHues) -->

**VividHues: super lite package for colored strings in Python!**

<a href="https://pypi.org/project/VividHues/"><img src="https://img.shields.io/badge/PyPi-3775A9?style=for-the-badge&logo=pypi&logoColor=white" /></a>

<img src="repo-imgs/vividhues-example.png" width="30%" align="none" />

---

## :hammer_and_wrench: Official Installation
###### Use this command, in your command line, to install VividHues.
```bash
pip install VividHues
```

### :bricks: Dependency
#### _requirements.txt_ (Highly Recommended!)
###### Append this to your Python packages requirements file.
```python
VividHues>=2.7.9  # only has Clr codes
VividHues>=4.1.0  # has new features such as abbreviations & Clr.rainbow()
```

#### _Dependabot.yml_ (optional)
###### Create this file, to add your GitHub repo as a dependent.
```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "daily"
```

#### _Dockerfile_ (optional)
###### If you have a Docker container. :whale2:
```dockerfile
# recommended
COPY requirements.txt .
RUN pip install -r requirements.txt

# alternatively...
RUN pip install VividHues
```

---

## :snake: Python Example

<img src="repo-imgs/vividhues-example.png" width="30%" align="right" />

```python
print(Clr.BO + Clr.UL + Clr.rainbow('I love VividHues!') + Clr.RS)
print(f"{Clr.RED}It's got my fave color!{Clr.RS}")
print(f"Soooo {Clr.jazzy('jazzy')}")
#                          ^^^
# you'll get an error using "" in f-string interpolations
```

## :rainbow: Available Clr codes:
#### Just put a color in the gap ```Clr.___```
###### RED, ORANGE, YELLOW, LIME, GREEN, BLUE, CYAN, PURPLE, PINK, BLACK, WHITE
#### Or use a formatter
###### UNDERLINE, UL, BOLD, BO, RESET, RS


### :magic_wand: Magic Functions

#### :game_die: Clr.random()
```python
print(Clr.random(string))
```
###### Picks a random Clr code.

#### :saxophone: Clr.jazzy()
```python
print(Clr.jazzy(string))
```
###### Jazzes up your console by giving each letter of the string passed a random color!
###### It's a total gamble, that's guaranteed to be ugly! :)

#### :rainbow: Clr.rainbow()
```python
print(Clr.rainbow(string))
```
###### Makes any string colored in a rainbow pattern.


---
Kenny Oliver ©2021

# VividHues :rainbow: :package:

[![VividHues](https://github.com/KennyOliver/VividHues/actions/workflows/python-publish.yml/badge.svg)](https://github.com/KennyOliver/VividHues/actions/workflows/python-publish.yml)
[![Downloads](https://static.pepy.tech/personalized-badge/vividhues?period=total&units=international_system&left_color=gray&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/vividhues)
[![Downloads](https://static.pepy.tech/personalized-badge/vividhues?period=month&units=international_system&left_color=gray&right_color=blue&left_text=Past%20Month)](https://pepy.tech/project/vividhues)
[![Downloads](https://static.pepy.tech/personalized-badge/vividhues?period=week&units=international_system&left_color=gray&right_color=blue&left_text=Past%20Week)](https://pepy.tech/project/vividhues)

![CodeFactor](https://www.codefactor.io/repository/github/KennyOliver/vividHues/badge?style=for-the-badge)
![Latest SemVer](https://img.shields.io/github/v/tag/KennyOliver/vividHues?label=version&sort=semver&style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/KennyOliver/vividHues?style=for-the-badge)
![Total Lines](https://img.shields.io/tokei/lines/github/KennyOliver/vividHues?style=for-the-badge)


**<big>VividHues:</big> &nbsp;&nbsp; super lite package for colored strings in Python!**

<a href="https://pypi.org/project/VividHues/"><img src="https://img.shields.io/badge/PyPi-3775A9?style=for-the-badge&logo=pypi&logoColor=white" /></a>
<a href="https://test.pypi.org/project/VividHues/"><img src="https://img.shields.io/badge/Test%20PyPi-white?style=for-the-badge&logo=pypi&logoColor=3775A9" /></a>

<img src="https://user-images.githubusercontent.com/70860732/162396475-b2c511af-0ddd-4e85-8d17-b62b3d732e78.png" width="50%" align="none" />

---

## :hammer_and_wrench: Official Installation

> ### :runner: Shortcut!
> #### _You can install with a Bash script if you'd like!_
> 
> <a href="./installer.sh" download><img src="https://img.shields.io/badge/Download%20Installer%20Script-4EAA25?style=for-the-badge&logo=windowsterminal&labelColor=black&logoColor=white" /></a>

##### Pop this command in your CLI/shell/terminal to install VividHues.
```bash
$ pip install VividHues
```

##### Stick this wherever you need VividHues!
```py
from VividHues import Clr
```

### :bricks: Dependency
#### _`requirements.txt`_ (Highly Recommended!)
###### Append the following to your Python packages `requirements.txt`...
```python
VividHues>=5.3.0
```
###### Changelog:
```py
VividHues>=3.0.0    #  basics: only has Clr codes
VividHues>=4.1.0    #  new: abbreviations & "Magic Functions"
VividHues>=5.2.0    #  Magic Function: Clr.pattern()
VividHues>=5.3.0    #  all Magic Functions no longer leak color
VividHues>=5.4.0    #  Clr.delPrevLine()
```

#### _`.github/Dependabot.yml`_ (optional, but needs `requirements.txt`)
###### First, if you don't already have a `.github` directory, create one.
###### Then, add a `Dependabot.yml` file to it.
```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "daily"
```

#### _`Dockerfile`_ :whale: (optional)
###### You can use this if you have a Docker container.
```dockerfile
# recommended
COPY requirements.txt .
RUN pip install -r requirements.txt
```
```dockerfile
# alternatively...
RUN pip install VividHues
```

---

## :snake: Python Example

<img src="https://user-images.githubusercontent.com/70860732/162396475-b2c511af-0ddd-4e85-8d17-b62b3d732e78.png" width="30%" align="right" />

```python
print(Clr.BO + Clr.UL + Clr.rainbow('I love VividHues!'))
print(Clr.RED + "It's got my fave color!" + Clr.RS)
print(f"Soooo {Clr.jazzy('jazzy')}")
#                          ^^^
# you'll get an error using "" in f-string interpolations
print(Clr.pattern("Kenny Oliver", Clr.PURPLE, Clr.CYAN, Clr.LIME))
```

---

## :warning: Preventing Color Leakage!

### What is color leakage??? :thinking:

:point_right: **Color leakage is when you have forgotten to use `Clr.RS`/`Clr.RESET`** :point_left: to reset the formatting after the last character printed to the standard output!

It results in any trailing characters, in the output stream, to continue to have the same formatting.

**This is an intentional feature,** because it allows for the formatting of entire chunks of code in one go.
See the example

> #### :pencil: Note!
> As of `VividHues>=5.3.0`, <big>ALL</big> magic functions do not leak color.
> 
> Previously, it was only `Clr.random()`!

### How do I prevent/solve this? :tada:

#### :a: End <kbd>print()</kbd> with <kbd>Clr.RS</kbd>/<kbd>Clr.RESET</kbd> &nbsp; — &nbsp; Short 'n' Sweet! :candy:
```py
print(... + Clr.RS)  # recommended!

print(..., Clr.RS)

print(..., end=Clr.RS+"\n")
```

#### :b: Format chunks of code &nbsp; — &nbsp; Highly Recommended! :thumbsup:
```py
# start formatting here
print(Clr.BOLD + Clr.RED, end="")


if something:
  print(Clr.BLUE + "blah blah blah" + Clr.RS)
else:
  for x in range(100):
    # lots of print statements


# end formatting here
print(Clr.RS, end="")
```

> #### :bulb: Tip!
> These solutions also prevent the leakage of other formatting
> 
> (e.g. `Clr.BO`, `Clr.BOLD`, `Clr.UL`, `Clr.UNDERLINE`)

---

## :rainbow: Available `Clr` codes:
#### Just put a code in the gap <kbd>Clr.___</kbd>

###### <big>Clr:</big> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; RED, ORANGE, YELLOW, LIME, GREEN, BLUE, CYAN, PURPLE, PINK, BLACK, WHITE
###### <big>Formatter:</big> &nbsp;&nbsp;&nbsp;&nbsp; UNDERLINE, UL, BOLD, BO
###### <big>Reset:</big> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; RESET, RS

> ##### :pencil: Note!
> ###### In order to make your life easy, when reading the documentation,
> ###### Your import statement should be the following... :point_down:
> `from VividHues import Clr` so that you can use `Clr.___`

---

## :wastebasket: Erasing the previous line

VividHues provides you with a quick way to erase the last line of the CLI!

```py
# Delete the last printed line of the CLI
Clr.delPrevLine()
```

```py
# Delete the last  5  printed lines
Clr.delPrevLine(5)
```

---

## :magic_wand: Magic Functions!!!

> ##### :bulb: TIP!
> ###### Magic Functions do not leak color (as of `VividHues>=5.3.0`)

#### :game_die: Clr.random()

<img src="https://user-images.githubusercontent.com/70860732/162318600-f533f919-7119-4027-9f37-4a51da22051d.png" width="40%" align="right" />

> ```python
> print(  Clr.random(string)  )
> ```
> ###### Paints your string in a random Clr code.

#### :saxophone: Clr.jazzy()

<img src="https://user-images.githubusercontent.com/70860732/162393890-7af20eae-501e-4a2c-aeef-9cdabb01f759.png" width="40%" align="right" />

> ```python
> print(  Clr.jazzy(string)  )
> ```
> ###### Paints each letter in jazzy random colors! It's a total gamble, that's guaranteed to be ugly! :)

#### :rainbow: Clr.rainbow()

<img src="https://user-images.githubusercontent.com/70860732/162399848-590a5864-6547-418d-9768-40d36dc839c0.png" width="40%" align="right" />

> ```python
> print(  Clr.rainbow(string)  )
> ```
> 
> ###### Paints your string in a rainbow pattern.

#### :test_tube: Clr.pattern()

<img src="https://user-images.githubusercontent.com/70860732/162422427-ef00dc83-7b08-4c72-9677-c4ea3b019ff2.png" width="40%" align="right" />

> ```python
> print(  Clr.pattern(string, *color)  )
> ```
> ###### Paint your letters in a repeating pattern, by specifying an unlimited amount of Clr codes!

---

## :muscle: How VividHues stacks up...
| Feature | [VividHues](https://pypi.org/project/VividHues/) | [Colorama](https://pypi.org/project/colorama/) | [termcolor](https://pypi.org/project/termcolor/) |
| :--------------------:  | :---------------: | :------:   | :--------: |
| Simplicity/Abstraction  | :star:            | :star:     | :star:     |
| Font Colors             | :star:            | :star:     | :star:     |
| Background/Highlight    | :crossed_fingers: | :star:     | :star:     |
| Bold/Underline          | :star:            |            | :star:     |
| Most Lightweight        | :star:            |            |            |
| Auto-Reset              | :star:            | :star:     | :star:     |
| Cursor Positioning      |                   | :star:     |            |
| Special/Unique Features | :star:            |            | :star:     |
| <b>Total</b>            | <b>6/8</b>        | <b>5/8</b> | <b>6/8</b> |

Potentially, VividHues will have more features than the alternatives if they are implemented.

___

## :mag_right: Getting Package Info

```py
import VividHues  # different import this time!


print(VividHues.__author__)
# Kenneth Oliver ©2022

print(VividHues.__desc__)
# Super lite package for colored strings in Python! 🌈 📦

print(VividHues.__homepage__)
# https://github.com/KennyOliver/VividHues

print(VividHues.__package__)
# VividHues

print(VividHues.__pypi__)
# https://pypi.org/project/VividHues/

print(VividHues.__name__)
# VividHues
```

---
Kenny Oliver ©2021

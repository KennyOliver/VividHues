<p align="center">
 <img src="https://user-images.githubusercontent.com/70860732/163634874-9e86d5b1-ada9-4761-baeb-5a175def5795.png" width="75%" />
</>
<!-- <img src="https://user-images.githubusercontent.com/70860732/163634932-35a6577b-7c79-4dfd-8eb1-fbb68c7e1ff6.png" /> -->
<h1 align="center">🌈 VividHues 📦</h1>

<p align="center">
 <b>Super light Python string formatter!</b>
 <br /><br />
 <img src="https://custom-icon-badges.herokuapp.com/github/workflow/status/KennyOliver/VividHues/VividHues?logo=rocket&logoColor=white&&style=for-the-badge" />
 <img src="https://www.codefactor.io/repository/github/KennyOliver/vividHues/badge?style=for-the-badge" />
 <img src="https://custom-icon-badges.herokuapp.com/github/license/KennyOliver/VividHues?logo=repo&style=for-the-badge" />
 <br />
 <img src="https://custom-icon-badges.herokuapp.com/github/v/tag/KennyOliver/VividHues?style=for-the-badge&logo=tag&logoColor=white&label=version" />
 <img src="https://img.shields.io/tokei/lines/github/KennyOliver/vividHues?style=for-the-badge" />
 <img src="https://img.shields.io/github/repo-size/KennyOliver/vividHues?style=for-the-badge" />
 <img src="https://custom-icon-badges.herokuapp.com/github/languages/code-size/KennyOliver/VividHues?logo=file-code&logoColor=white&style=for-the-badge" />
 <br />
 <a href="https://pepy.tech/project/VividHues">
  <img src="https://static.pepy.tech/personalized-badge/vividhues?period=total&units=international_system&left_color=gray&right_color=blue&left_text=Total%20Downloads" />
  <img src="https://static.pepy.tech/personalized-badge/vividhues?period=month&units=international_system&left_color=gray&right_color=blue&left_text=Past%20Month" />
  <img src="https://static.pepy.tech/personalized-badge/vividhues?period=week&units=none&left_color=gray&right_color=blue&left_text=Past%20Week" />
 </a>
 <br /><br />
 <a href="https://pypi.org/project/VividHues/">
  <img src="https://img.shields.io/badge/PyPi-3775A9?style=for-the-badge&logo=python&logoColor=white&labelColor=303030" />
 </a>
 <a href="https://test.pypi.org/project/VividHues/">
  <img src="https://img.shields.io/badge/Test%20PyPi-E8C541?style=for-the-badge&logo=python&logoColor=white&labelColor=303030" />
 </a>
 <br /><br />
 <span align="center">
  👉
  <kbd>
   <a href="https://gitcdn.link/cdn/KennyOliver/VividHues/main/install_vividhues.sh" download>
    <img src="https://custom-icon-badges.herokuapp.com/badge/-Instant%20Installer-FFD700?style=for-the-badge&logo=zap&logoColor=FFD700&labelColor=303030" />
   </a>
  </kbd>
  👈
 </span>
</p>

---

## :hammer_and_wrench: Official Installation

### :zap: _Instant Installer + Updater_

<img src="https://user-images.githubusercontent.com/70860732/163634599-31351517-3333-43f5-b2c2-87408522aefe.png" width="70%" />

<big>&nbsp; :point_right: &nbsp; </big><kbd><a href="https://gitcdn.link/cdn/KennyOliver/VividHues/main/install_vividhues.sh" download><img src="https://custom-icon-badges.herokuapp.com/badge/-Instant%20Installer-FFD700?style=for-the-badge&logo=zap&logoColor=FFD700&labelColor=303030" /></a></kbd><big> &nbsp; :point_left:</big>

#### :page_with_curl: Instant Installer &nbsp; — &nbsp; Instructions

##### **Once you've downloaded `install_vividhues.sh`...**
###### Run the command `bash install_vividhues.sh` in your shell/CLI. (Or... double click the `install_vividhues.sh` file)

> :memo: **Note!**
> 
> This requires Bash to be installed on your OS.
> Git Bash or WSL are two of many to pick from!

#### :cyclone: Replit Installation

<details>
<summary>👉 <i><b>Replit instructions in here!</i></b> 👈</summary>

1. Upload the installer script to your project's file system
<img src="https://user-images.githubusercontent.com/70860732/162637390-af2be82f-929a-4053-a5f5-ce788bf7f9c4.png" /> 

2. Run `bash install_vividhues.sh` in the _**shell**_
<img src="https://user-images.githubusercontent.com/70860732/162637572-f096ccf2-2ff3-4fee-8028-2432fc31806b.png" /> 
</details>

#### :shell: Manual Shell Installation

<details>
<summary>👉 <i><b>Manual instructions in here!</i></b> 👈</summary>

##### Pop this command in your CLI/shell/terminal to install VividHues.
```bash
$ pip install VividHues
```
 
> #### :bulb: Tip
> ###### Use this command to update
> ```bash
> pip install --upgrade VividHues
> ```


## :ship: Importing
##### Stick this wherever you need VividHues!
```py
from VividHues import Clr
```
</details>

---

## :bricks: Dependency
#### _`requirements.txt`_ &nbsp;&nbsp; _(Highly Recommended!)_
###### Append the following to your Python packages `requirements.txt`...
```python
VividHues>=5.4.0
```
> ###### Changelog :newspaper:
> ```py
> VividHues>=3.0.0    #  basics: only has Clr codes
> VividHues>=4.1.0    #  new: abbreviations & "Magic Functions"
> VividHues>=5.2.0    #  Magic Function: Clr.pattern()
> VividHues>=5.3.0    #  all Magic Functions no longer leak color
> VividHues>=5.4.0    #  Clr.delPrevLine()
> ```

#### _`.github/Dependabot.yml`_ &nbsp;&nbsp; _(optional, but needs `requirements.txt`)_
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

#### _`Dockerfile`_ :whale: &nbsp;&nbsp; _(optional)_
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

<img src="https://user-images.githubusercontent.com/70860732/163634451-66f6b96b-7e64-4a29-8883-55f23d72206a.png" width="30%" align="right" />

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

> #### :memo: Note!
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

> ##### :memo: Note!
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

<br />

#### :saxophone: Clr.jazzy()

<img src="https://user-images.githubusercontent.com/70860732/162393890-7af20eae-501e-4a2c-aeef-9cdabb01f759.png" width="40%" align="right" />

> ```python
> print(  Clr.jazzy(string)  )
> ```
> ###### Paints each letter in jazzy random colors! It's a total gamble, that's guaranteed to be ugly! :)

<br />

#### :rainbow: Clr.rainbow()

<img src="https://user-images.githubusercontent.com/70860732/162399848-590a5864-6547-418d-9768-40d36dc839c0.png" width="40%" align="right" />

> ```python
> print(  Clr.rainbow(string)  )
> ```
> 
> ###### Paints your string in a rainbow pattern.

<br />

#### :test_tube: Clr.pattern()

<img src="https://user-images.githubusercontent.com/70860732/162422427-ef00dc83-7b08-4c72-9677-c4ea3b019ff2.png" width="40%" align="right" />

> ```python
> print(  Clr.pattern(string, *color)  )
> ```
> ###### Paint your letters in a repeating pattern, by specifying an unlimited amount of Clr codes!

<br />
<br /><br />

---

## :muscle: How VividHues stacks up...
| Feature | [VividHues](https://pypi.org/project/VividHues/) | [colorama](https://pypi.org/project/colorama/) | [termcolor](https://pypi.org/project/termcolor/) |
| :---------------------: | :---------------: | :--------: | :--------: |
| Simplicity/Abstraction  | :star:            | :star:     | :star:     |
| Font Colors             | :star:            | :star:     | :star:     |
| Background/Highlight    | :crossed_fingers: | :star:     | :star:     |
| Bold/Underline          | :star:            |            | :star:     |
| Most Lightweight        | :star:            |            |            |
| Auto-Reset              | :star:            | :star:     | :star:     |
| Cursor Positioning      |                   | :star:     |            |
| Special/Unique Features | :star:            |            | :star:     |
| Dependencies            | :star:            |            |            |
| <b>Total</b>            | <b>7/9</b>        | <b>6/9</b> | <b>6/9</b> |

Potentially, VividHues will have more features than the alternatives if they are implemented.

___

## :mag_right: Getting Package Info

VividHues comes with a variety of 'dunder' values that you can check out.

An important example is checking out the current version: `VividHues.__version__`

> ##### :memo: Note!
> ###### The import is different this time!
> 
> ```py
> import VividHues
> ```

#### Dunders Command

You can use the following command to find out all the possible dunders!

```py
VividHues.dunders()
```

<img src="https://user-images.githubusercontent.com/70860732/168440207-bbfd0297-3132-43de-8139-5db03fd47359.png" />

#### Dunder Values

| Dunder | What It Does | Expected Output |
| :----: | :----------: | :-------------: |
| `__author__`   | author          | "Kenneth Oliver ©2022" |
| `__desc__`     | description     | "Super light Python string formatter! 🌈 📦" |
| `__homepage__` | GitHub URL      | "https://github.com/KennyOliver/VividHues" |
| `__package__`  | package name    | "VividHues" |
| `__pypi__`     | Pypi URL        | "https://pypi.org/project/VividHues/" |
| `__version__`  | current version | (whatever the current version is!) |

###### For example, using `print(VividHues.__version__)` will display the current version.

---
## :raised_hands: Wanna contribute?

#### Contribute here :point_right: [Click me!](docs/CONTRIBUTING.md)
#### :warning: Make sure that you read the Code of Conduct :point_right: [Click me!](docs/CODE_OF_CONDUCT.md)

---
Kenny Oliver ©2022

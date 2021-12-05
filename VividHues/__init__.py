import os
import random

os.system("")  # allows colours to be displayed in the console


class Clr:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    ORANGE = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    LIME = "\033[92m"
    YELLOW = "\033[93m"
    PINK = "\033[95m"

    UNDERLINE = "\033[4m"
    UL = UNDERLINE
    BOLD = "\033[01m"
    BO = BOLD
    RESET = "\033[0m"
    RS = RESET

    @classmethod
    def random_color(cls):
        colors = []  # List of all the colors in the class Clr
        for key in Clr.__dict__.keys():
            if key == "UNDERLINE":  # Once we got to UNDERLINE, there is no more color
                break
            else:
                colors.append(Clr.__dict__[key])
        colors.pop(0)  # Remove the first key of (Clr.__dict__.keys()). Not a color
        return colors[random.randint(0, len(colors) - 1)]


def print_string_rainbow_colors(string_to_print):
    for letter in string_to_print:
        print(f'{Clr.random_color()}' + letter, end="")
    print("")


def print_string_random_color(string_to_print):
    print(f'{Clr.random_color()}' + string_to_print)

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

    @classmethod
    def random(cls, string_to_color: str):
        print(f'{Clr.random_color()}' + string_to_color)

    @classmethod
    def jazzy(cls, string_to_color: str):
        for letter in string_to_color:
            print(f'{Clr.random_color()}' + letter, end="")
        print("")

    @classmethod
    def rainbow(cls, string_to_color: str):
        rainbow_colors = [Clr.RED, Clr.ORANGE, Clr.YELLOW, Clr.GREEN, Clr.LIME, Clr.CYAN, Clr.BLUE, Clr.PURPLE,
                          Clr.PINK]
        string_index = 0
        colors_index = 0
        while string_index <= len(string_to_color) - 1:
            print(f'{rainbow_colors[colors_index]}' + string_to_color[string_index], end="")
            string_index += 1
            colors_index += 1
            if colors_index == 9:
                colors_index = 0
        print("")


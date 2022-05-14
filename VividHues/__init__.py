import os
import random
os.system("")  # allows colours to be displayed in the CLI


def dunders() -> None:
    """ prints out the available dunders """

    print()
    print("\t" + "╔" + "═" * 42 + "╗", end="")
    print(
        f"""
    ║                                          ║
    ║       • {Clr.BO}{Clr.rainbow("VividHues Dunders Guide")}{Clr.RS} •        ║
    ║                                          ║
    ║     {Clr.RED   }__author__     author{Clr.RS}                ║
    ║     {Clr.ORANGE}__desc__       description{Clr.RS}           ║
    ║     {Clr.YELLOW}__homepage__   GitHub URL{Clr.RS}            ║
    ║     {Clr.LIME  }__package__    package name{Clr.RS}          ║
    ║     {Clr.CYAN  }__pypi__       PyPi URL{Clr.RS}              ║
    ║     {Clr.BLUE  }__name__       package name{Clr.RS}          ║
    ║     {Clr.PURPLE}__version__    current version{Clr.RS}       ║
    ║                                          ║
    ║     Access this again:                   ║
    ║     {Clr.PINK}VividHues.dunders(){Clr.RS}                  ║
    ║                                          ║
    ║     Read the docs for more:              ║
    ║     {Clr.UL + Clr.GREEN}github.com/KennyOliver/VividHues{Clr.RS}     ║
    ║                                          ║"""
        )
    print("\t" + "╚" + "═" * 42 + "╝")
    print()

__author__    = "Kenneth Oliver ©2022"
__desc__      = "Super lite package for colored strings in Python! 🌈 📦"
__homepage__  = "https://github.com/KennyOliver/VividHues"
__package__   = "VividHues"
__pypi__      = "https://pypi.org/project/VividHues/"
__version__   = "5.9.2"


class Clr:
    BLACK  = "\033[30m"
    RED    = "\033[31m"
    GREEN  = "\033[32m"
    ORANGE = "\033[33m"
    BLUE   = "\033[34m"
    PURPLE = "\033[35m"
    CYAN   = "\033[36m"
    WHITE  = "\033[37m"
    LIME   = "\033[92m"
    YELLOW = "\033[93m"
    PINK   = "\033[95m"
    
    UNDERLINE = "\033[4m"
    UL        = UNDERLINE
    BOLD = "\033[01m"
    BO   = BOLD
    RESET = "\033[0m"
    RS    = RESET

    
    @classmethod
    def random_color(cls) -> str:
        """ returns a random Clr code """
        
        colors = []  # List of all the colors in the class Clr
        for key in Clr.__dict__.keys():
            if key == "UNDERLINE":  # Once we got to UNDERLINE, there is no more color
                break
            else:
                colors.append(Clr.__dict__[key])
        colors.pop(0)  # Remove the first key of (Clr.__dict__.keys()). Not a color
        return colors[random.randint(0, len(colors) - 1)]


    @classmethod
    def random(cls, string_to_color: str) -> str:
        """ chooses a random Clr code """
      
        return f'{Clr.random_color()}' + string_to_color + Clr.RS


    @classmethod
    def jazzy(cls, string_to_color: str) -> str:
        """ gives each letter a random color """
      
        jazzy_str = ""

        for letter in string_to_color:
            jazzy_str += Clr.random_color() + letter

        return jazzy_str + Clr.RS


    @classmethod
    def rainbow(cls, string_to_color: str) -> str:
        """ colors each letter in a rainbow pattern """
      
        rainbow_colors = [Clr.RED, Clr.ORANGE, Clr.YELLOW, Clr.GREEN, Clr.LIME, Clr.CYAN, Clr.BLUE, Clr.PURPLE, Clr.PINK]

        rainbow_str = ""
        string_index = 0
        colors_index = 0

        while string_index <= len(string_to_color) - 1:
            rainbow_str += rainbow_colors[colors_index] + string_to_color[string_index]
            string_index += 1
            colors_index += 1
            if colors_index == 9:
                colors_index = 0
        
        return rainbow_str + Clr.RS
    
    @classmethod
    def pattern(cls, string_to_color: str, *chosen_clrs) -> str:
        """ allow custom definitions of Clr patterns """

        if len(chosen_clrs) < 1:
            raise ValueError(
                Clr.CYAN
              + f"Expected some Clr codes, but was povided {len(chosen_clrs)}!"
              + Clr.RS
            )
      
        pattern_str = ""
        string_index = 0
        colors_index = 0

        while string_index <= len(string_to_color) - 1:
            pattern_str += chosen_clrs[colors_index] + string_to_color[string_index]
            colors_index += 1
            string_index += 1
            if colors_index == len(chosen_clrs):
              colors_index = 0
        
        return pattern_str + Clr.RS

    
    def delPrevLine(repeat: int = 1) -> None:
        ''' erases the previous line in the CLI '''

        if repeat < 0:
            raise ValueError(
                Clr.CYAN
              + f"Expected a positive value for repeat, but was povided {repeat}!"
              + Clr.RS
            )

        import sys
        
        CURSOR_UP_ONE = '\x1b[1A' 
        ERASE_LINE    = '\x1b[2K'
        for _ in range(int(repeat)):
            sys.stdout.write(CURSOR_UP_ONE + ERASE_LINE)

#!/usr/bin/env python3

ANSI_base = '\033['

class ANSI_Code_output():
    def __init__(self):
        for name_code, value in vars(self.__class__).items():
            if isinstance(value, int) and not name_code.startswith("_"):
                setattr(self, name_code, f'{ANSI_base}{value}m')
        
class ANSI_Codes_Foreground(ANSI_Code_output):

    # Standart
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    PURPLE = 35
    CYAN = 36
    WHITE = 37

    # Bright Standart not for stupid terminals and term env
    GRAY = 90
    LIGHTRED = 91
    LIGHTGREEN = 92
    LIGHTYELLOW = 93
    LIGHTBLUE = 94
    LIGHTPURPLE = 95
    LIGHTCYAN = 96
    LIGHTWHITE = 97

    RESET = 0

class ANSI_Codes_Background(ANSI_Code_output):

    # Standart
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    PURPLE = 45
    CYAN = 46
    WHITE = 47

    # Bright Standart not for stupid terminals and term env
    GRAY = 100
    LIGHTRED = 101
    LIGHTGREEN = 102
    LIGHTYELLOW = 103
    LIGHTBLUE = 104
    LIGHTPURPLE = 105
    LIGHTCYAN = 106
    LIGHTWHITE = 107

    RESET = 0


class TEXT_STYLE(ANSI_Code_output):

    BOLD = 1 
    DIM = 2 
    ITALIC = 3 
    UNDERLINE = 4
    BLINK = 5
    REVERSE = 7
    OVERLINE = 53

    RESET = 0


def Foreground_256Colors(color_value):
    if not color_value > 256:
        return f'{ANSI_base}38;5;{color_value}m'
    else:
        invalid_value = f'{FG.RED}{ST.UNDERLINE}{ST.ITALIC}color_value = {color_value}{FG.RESET}'
        return f'{FG.RED}IndexError: {invalid_value}{FG.RED} . Index out of range 256'

def Background_256Colors(color_value):
    if not color_value > 256:
        return f'{ANSI_base}48;5;{color_value}m'
    else:
        invalid_value = f'{FG.RED}{ST.UNDERLINE}{ST.ITALIC}color_value = {color_value}{FG.RESET}'
        return f'{FG.RED}IndexError: {invalid_value}{FG.RED} . Index out of range 256'


BG = ANSI_Codes_Background()
FG = ANSI_Codes_Foreground()
ST = TEXT_STYLE()
FG256 = Foreground_256Colors
BG256 = Background_256Colors

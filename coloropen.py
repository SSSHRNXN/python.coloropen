#!/usr/bin/env python3

ANSI_base = '\033['

class ANSI_Code_output():
    def __init__(self):
        for name_code in dir(self):
            if not name_code.startswith("_"):
                setattr(self, name_code, f'{ANSI_base}{getattr(self, name_code)}m')
        
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

    REVERSE = 7
    
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
    OVERLINE = 53

    RESET = 0

BG = ANSI_Codes_Background()
FG = ANSI_Codes_Foreground()
ST = TEXT_STYLE()

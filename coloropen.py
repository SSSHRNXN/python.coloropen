#!/usr/bin/env python3

ANCI_base = '\033['

class ANSI_Code_output():
    def __init__(self):
        for name_code in dir(self):
            if not name_code.startswith("_"):
                setattr(self, name_code, f'{ANCI_base}{getattr(self, name_code)}m')
        
class ANSI_Codes_Foreground(ANSI_Code_output):

    # Standart
    Black = 30
    Red = 31
    Green = 32
    Yellow = 33
    Blue = 34
    Purple = 35
    Cyan = 36
    White = 37

    # Bright Standart not for stupid terminals and term env
    LIGHTBlack = 90
    LIGHTRed = 91
    LIGHTGreen = 92
    LIGHTYellow = 93
    LIGHTBlue = 94
    LIGHTPurple = 95
    LIGHTCyan = 96
    LIGHTWhite = 97

    RESET = 0

class ANSI_Codes_Background(ANSI_Code_output):

    # Standart
    Black = 40
    Red = 41
    Green = 42
    Yellow = 43
    Blue = 44
    Purple = 45
    Cyan = 46
    White = 47

    # Bright Standart not for stupid terminals and term env
    LIGHTBlack = 100
    LIGHTRed = 101
    LIGHTGreen = 102
    LIGHTYellow = 103
    LIGHTBlue = 104
    LIGHTPurple = 105
    LIGHTCyan = 106
    LIGHTWhite = 107

    RESET = 0

BG = ANSI_Codes_Background()
FG = ANSI_Codes_Foreground()

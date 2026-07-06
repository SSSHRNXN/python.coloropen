#!/usr/bin/env python3

from datetime import date, datetime
from re import T
import shutil

ANSI_base = '\033['

class ANSI_Code_output():
    def __init__(self):
        for name_code, value in vars(self.__class__).items():
            if isinstance(value, int) and not name_code.startswith("_"):
                setattr(self, name_code, f'{ANSI_base}{value}m')


class TTY_Stat():
    COLUMNS, LINES = shutil.get_terminal_size()
        
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
    if color_value > 256:
        invalid_value = f'{FG.RED}{ST.UNDERLINE}{ST.ITALIC}color_value = {color_value}{FG.RESET}'
        return f'{FG.RED}IndexError: {invalid_value}{FG.RED} . Index out of range 1-256'
    elif color_value < 1:
        invalid_value = f'{FG.RED}{ST.UNDERLINE}{ST.ITALIC}color_value = {color_value}{FG.RESET}'
        return f'{FG.RED}IndexError: {invalid_value}{FG.RED} . Index out of range 1-256'
    else:
        return f'{ANSI_base}38;5;{color_value}m'

def Background_256Colors(color_value):
    if color_value > 256:
        invalid_value = f'{FG.RED}{ST.UNDERLINE}{ST.ITALIC}color_value = {color_value}{FG.RESET}'
        return f'{FG.RED}IndexError: {invalid_value}{FG.RED} . Index out of range 1-256'
    elif color_value < 1:
        invalid_value = f'{FG.RED}{ST.UNDERLINE}{ST.ITALIC}color_value = {color_value}{FG.RESET}'
        return f'{FG.RED}IndexError: {invalid_value}{FG.RED} . Index out of range 1-256'
    else:
        return f'{ANSI_base}48;5;{color_value}m'

BG = ANSI_Codes_Background()
FG = ANSI_Codes_Foreground()
ST = TEXT_STYLE()
FG256 = Foreground_256Colors
BG256 = Background_256Colors

def ColorLogger(message, level="INFO"):
    date = datetime.now().strftime("%Y-%M-%d %H:%M:%S")
    log_levels = {
            'INFO' : FG.GREEN,
            'INF' : FG.GREEN,
            'WARNING' : FG.YELLOW,
            'ERROR' : FG.RED,
            'CRITICAL' : FG.RED + ST.BLINK + ST.BOLD + ST.UNDERLINE,
            'DEBUG' : FG.GRAY
            }

    lenghlevel = len(max(log_levels, key=len))
    color = log_levels.get(level.upper(), FG.WHITE)
    if level.upper() == "CRITICAL":
        return f'{FG.CYAN}[{date}]  {color}{level.upper():^{lenghlevel}}{FG.RESET}  {color}{message}{FG.RESET}'
    else:
        return f'{FG.CYAN}[{date}] {color}[{level.upper():^{lenghlevel - 1}}] {message}{FG.RESET}'

clog = ColorLogger


class Text_Alignment():
    from coloropen import TTY_Stat

    def CENTER(message, borders=False):
        message_len = len(message)
        print(TTY_Stat.COLUMNS, TTY_Stat.LINES, f'Center alignment work in progress')

        if borders:
            print("─" * TTY_Stat.COLUMNS)
        
        print(f'{" " * (((TTY_Stat.COLUMNS) // 2 ) - message_len // 2 )}{message}')

        if borders:
            print("─" * TTY_Stat.COLUMNS)
        

ALIGN = Text_Alignment

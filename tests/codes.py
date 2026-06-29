#!/usr/bin/env python3

from pathlib import Path
import sys
sys.path.insert(0, str(Path.cwd().resolve().parent))
from coloropen import BG, FG



spaces = ' ' * 3
colors = (
    'Black' ,
    'Red' ,
    'Green' ,
    'Yellow' , 
    'Blue' ,
    'Purple' ,
    'Cyan' ,
    'White' ,
    'LIGHTBlack' ,
    'LIGHTRed' ,
    'LIGHTGreen' ,
    'LIGHTYellow' ,
    'LIGHTBlue' ,
    'LIGHTPurple' ,
    'LIGHTCyan' ,
    'LIGHTWhite'
        )
crange = len(max(colors, key=len))
for color in colors:
    if color != 'Black' and color != 'LIGHTBlack':
        print(f'{spaces}{getattr(BG, color)}{FG.Black} {color:^{crange}} {BG.RESET}  │  {getattr(FG, color)} {color:^{crange}} {FG.RESET}')
    else:
        print(f'{spaces}{getattr(BG, color)}{FG.White} {color:^{crange}} {BG.RESET}  │  {getattr(FG, color)} {color:^{crange}} {FG.RESET}')

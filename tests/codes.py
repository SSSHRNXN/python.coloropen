#!/usr/bin/env python3

from pathlib import Path
import sys
sys.path.insert(0, str(Path.cwd().resolve().parent))
from coloropen import BG, FG, ST



spaces = ' ' * 3
colors = (
    'BLACK' ,
    'RED' ,
    'GREEN' ,
    'YELLOW' , 
    'BLUE' ,
    'PURPLE' ,
    'CYAN' ,
    'WHITE' ,
    'GRAY' ,
    'LIGHTRED' ,
    'LIGHTGREEN' ,
    'LIGHTYELLOW' ,
    'LIGHTBLUE' ,
    'LIGHTPURPLE' ,
    'LIGHTCYAN' ,
    'LIGHTWHITE'
        )

styles = (
        'BOLD',
        'DIM',
        'ITALIC',
        'UNDERLINE',
        'BLINK',
        'OVERLINE'
        )
crange = len(max(colors, key=len))
for color in colors:
    if color != 'BLACK' and color != 'LIGHTBLACK':
        print(f'{spaces}{getattr(BG, color)}{FG.BLACK} {color:^{crange}} {BG.RESET}  │  {getattr(FG, color)} {color:^{crange}} {FG.RESET}')
    else:
        print(f'{spaces}{getattr(BG, color)}{FG.WHITE} {color:^{crange}} {BG.RESET}  │  {BG.WHITE}{getattr(FG, color)} {color:^{crange}} {FG.RESET}')

print(spaces)

for style in styles:
    print(f'{spaces}{getattr(ST, style)} {style:^{crange}} {ST.RESET}')

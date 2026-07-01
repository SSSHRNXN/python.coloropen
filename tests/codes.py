#!/usr/bin/env python3

from pathlib import Path
import sys
sys.path.insert(0, str(Path.cwd().resolve().parent))
from coloropen import BG, BG256, FG, FG256, ST


spaces = ' ' * 3

def Hat_print(TEXT_MESSAGE):
    print(f'{spaces}{BG.WHITE}{FG.BLACK}{TEXT_MESSAGE:^{(len(spaces) + crange * 2) + 6}}{BG.RESET}')
    print(" ")

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
        'REVERSE',
        'BLINK',
        'OVERLINE'
        )
crange = len(max(colors, key=len))

Hat_print("Standart colors")
for color in colors:
    if color != 'BLACK' and color != 'LIGHTBLACK':
        print(f'{spaces}{getattr(BG, color)}{FG.BLACK} {color:^{crange}} {BG.RESET}  │  {getattr(FG, color)} {color:^{crange}} {FG.RESET}')
    else:
        print(f'{spaces}{getattr(BG, color)}{FG.WHITE} {color:^{crange}} {BG.RESET}  │  {BG.WHITE}{getattr(FG, color)} {color:^{crange}} {FG.RESET}')

print(spaces)

for style in styles:
    print(f'{spaces}{getattr(ST, style)} {style:^{crange}} {ST.RESET}')

print(spaces) 
Hat_print("256Color Mode")
COLOR256_DEMO = f'{spaces}{BG256(123)}{FG.BLACK} {"BG256(123)":^{crange}} {FG.RESET}  │  {FG256(123)} {"FG256(123)":^{crange}} {FG.RESET}'
print(COLOR256_DEMO)
print(FG256(257))


#!/usr/bin/env python3

from pathlib import Path
import sys
sys.path.insert(0, str(Path.cwd().resolve().parent))
from coloropen import BG, BG256, FG, FG256

n = 15
def hat(message):
    print(" ")
    print(f'{BG.WHITE}{FG.BLACK}{message:^{n * 5}}{FG.RESET}')
    print(" ")

hat("BG256 colors")
text_color = FG.BLACK
bg_colors = [f'{BG256(color)}{text_color}{color:^5}{FG.RESET}' for color in range(1, 257)]
for i in range(0, len(bg_colors), n):
    print(''.join(bg_colors[i:i+n]))

hat("FG256 colors")
fg_colors = [f'{FG256(color)}{color:^5}{FG.RESET}' for color in range(1, 257)]
for i in range(0, len(fg_colors), n):
    print(''.join(fg_colors[i:i+n]))

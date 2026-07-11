#!/usr/bin/env python3

from coloropen.coloropen import BG, BG255, FG, FG255

n = 15
def hat(message):
    print(" ")
    print(f'{BG.WHITE}{FG.BLACK}{message:^{n * 5}}{FG.RESET}')
    print(" ")

hat("BG255 colors")
text_color = FG.BLACK
bg_colors = [f'{BG255(color)}{text_color}{color:^5}{FG.RESET}' for color in range(1, 256)]
for i in range(0, len(bg_colors), n):
    print(''.join(bg_colors[i:i+n]))

hat("FG255 colors")
fg_colors = [f'{FG255(color)}{color:^5}{FG.RESET}' for color in range(1, 256)]
for i in range(0, len(fg_colors), n):
    print(''.join(fg_colors[i:i+n]))

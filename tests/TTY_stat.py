#!/usr/bin/env python3

from pathlib import Path
import sys
sys.path.insert(0, str(Path.cwd().resolve().parent))
from coloropen import FG, TTY_Stat, BG

style = f'{BG.WHITE}{FG.BLACK}'
print(f' {style} TTY Columns: {BG.RESET} {TTY_Stat.COLUMNS} | {style} TTY Lines: {BG.RESET} {TTY_Stat.LINES} {BG.RESET}')

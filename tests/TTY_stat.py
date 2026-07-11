#!/usr/bin/env python3

from pathlib import Path
import sys
sys.path.insert(0, str(Path.cwd().resolve().parent))
from coloropen import FG, TTY_Stat, BG, ALIGN

style = f'{BG.WHITE}{FG.BLACK}'
message = f' {style} TTY Columns: {BG.RESET} {TTY_Stat.COLUMNS} | {style} TTY Lines: {BG.RESET} {TTY_Stat.LINES} {BG.RESET}'
ALIGN.CENTER(str(message), borders=True, debug=True)


#!/usr/bin/env python3

from pathlib import Path
import sys
sys.path.insert(0, str(Path.cwd().resolve().parent))
from coloropen import ALIGN, TTY_Stat

ALIGN.CENTER("TEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEST", borders=True)
Text_for_cut = f'TE{"E" * (TTY_Stat.COLUMNS + 3)} ST'
ALIGN.CENTER(Text_for_cut, borders=True, cut=True)
ALIGN.CENTER(Text_for_cut, borders=True, shift_value=20, debug=True)

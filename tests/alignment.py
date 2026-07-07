
#!/usr/bin/env python3

from pathlib import Path
import sys
sys.path.insert(0, str(Path.cwd().resolve().parent))
from coloropen import ALIGN, BG, BG256, FG, FG256, ST

ALIGN.CENTER("TEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEST", borders=True)

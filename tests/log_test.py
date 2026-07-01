#!/usr/bin/env python3 

from pathlib import Path
import sys
sys.path.insert(0, str(Path.cwd().resolve().parent))
from coloropen import ColorLogger as clog

test_message = "This is Test message!"

print(clog(test_message, level="INFO"))
print(clog(test_message, level="WARNING"))
print(clog(test_message, level="ERROR"))
print(clog(test_message, level="CRITICAL"))
print(clog(test_message, level="DEBUG"))

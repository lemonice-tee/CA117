#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip()
  if len(line) % 2 != 0:
    middle = line[len(line) // 2]
    print(middle)
  else:
    print("No middle character!")

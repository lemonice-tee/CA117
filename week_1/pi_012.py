#!/usr/bin/env python3

import sys

from math import pi

line = sys.stdin.readlines()
for n in line:
  n = n.strip()
  n = int(n)
  print(f'{pi:.{n}f}')

#!/usr/bin/env python3

import sys

for lines in sys.stdin:
  line = lines.strip().split()
  line = sorted(line, reverse=True)
  cakes = []
  i = 0
  while i < len(line):
    if i % 3 == 2:
      pass
    else:
      cakes.append(int(line[i]))
    i += 1
  print(sum(cakes))

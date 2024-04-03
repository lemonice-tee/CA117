#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip().split()
  #print(line)
  for word in line:
    if len(word) < 3:
      pass
    else:
      print(word[1:-1])

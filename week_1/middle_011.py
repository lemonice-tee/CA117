#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip().split()
  for word in line:
    if len(word) % 2 == 0:
      print('No middle character!')
    else:
      print(word[len(word) // 2])

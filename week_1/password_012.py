#!/usr/bin/env python3

import sys

for line in sys.stdin:
  word = line.strip()
  i = 0
  u = 0
  l = 0
  d = 0
  s = 0
  for c in word:
    if c.isupper():
      u = 1
    elif c.islower():
      l = 1
    elif c.isdigit():
      d = 1
    elif not c.isalnum():
      s = 1
    i += 1
  print(u + l + s + d)

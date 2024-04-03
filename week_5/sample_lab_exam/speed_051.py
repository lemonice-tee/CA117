#!/usr/bin/env python3

import sys

pt = 0
pd = 0
max_speed = 0
lines = sys.stdin.readlines()

for line in lines[1:]:
  ct, cd = line.strip().split()
  ct = int(ct)
  cd = int(cd)
  t = ct - pt
  d = cd - pd
  s = d // t
  if s > max_speed:
    max_speed = s
  pd = cd
  pt = ct

print(max_speed)

#!/usr/bin/env python3

import sys

line = sys.stdin.readlines()
for l in line:
  x, y = [int(z) for z in l.split()]
  if x > 0 and y > 0:
    print(1)
  elif x > 0 and y < 0:
    print(2)
  elif x < 0 and y < 0:
    print(3)
  else:
    print(4)

#for line in sys.stdin:
#  x, y = line.strip().split()
#  x = int(x)
#  y = int(y)
#  if int(x) > 0 and y > 0:
#    print(1)
#  if x > 0 and y < 0:
#    print(2)
#  if x < 0 and y < 0:
#    print(3)
#  else:
#    print(4)

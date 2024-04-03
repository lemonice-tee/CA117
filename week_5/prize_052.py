#!/usr/bin/env python3

import sys

"""
if letter = "A":
   d[1], d[2] = d[1], d[2]
"""

def cup_swap(p, swap):
  for x in swap:
    if p == 1:
      if x == "A":
        p == 2
      elif x == "B":
        pass
      else:
        p == 3
    elif p == 2:
      if x == "A":
        p == 1
      elif x == "B":
        p == 3
      else:
        pass
    else:
      if x == "A":
        pass
      elif x == "B":
        x == 2
      else:
        x == 1
  print(p)
#list called poosition qw [000]
  #for l = 1, 1st ==       100

line = sys.stdin.readlines()
p = line[0].strip()
swap = line[1].strip()
cup_swap(p, swap)

#!/usr/bin/env python3

import sys

def contains(left, right):
  # search thru to see if r[i] is in any position in l at all
  # repeat for r[i+1] etc
  # if false for any, return "False" // else return "True"
  for x in left:
    if x not in right and len(right) != len(left):
      return False
    else:
      right = right.replace(x,  "", 1)
      # RETURN TRUE
      # RETURN RIGHT == ""
  if right:
    return False
  else:
    return True


for line in sys.stdin:
  left,right = line.strip().lower().split()
  print(contains(left, right))

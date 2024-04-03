#!/usr/bin/env python3

import sys

import math

def get_roots(integers):
  a = int(integers[0])
  b = int(integers[1])
  c = int(integers[-1])

  try:
    pos = (-b + ((b * b) - (4 * a * c) ** (0.5))) // (2 * a)
    neg = (-b - ((b * b) - (4 * a * c) ** (0.5))) // (2 * a)
  except TypeError:
    return None

for line in sys.stdin:
  integers = line.strip().split()
  print(get_roots(integers))

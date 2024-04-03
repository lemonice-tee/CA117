#!/usr/bin/env python3

import sys

def unique_character(line):
  for l in line:
    uniques = [l for l in line if line.count(l)==1]

  print(max(uniques, default="none"))

  #print(uniques)
  #print(max(uniques))


for line in sys.stdin:
  line = line.strip().split()
  unique_character(line)

#!/usr/bin/env python3

import sys

def line_comparison(line):
  line_1 = line[0].strip()
  line_2 = line[1].strip()
  comp_result = []
  i = 0
  while i < len(line_1):
    if line_1[i] == line_2[i]:
      comp_result.append("-")
    else:
      comp_result.append("*")
    i += 1
  print(line_1)
  print(line_2)
  print("".join(comp_result))

line = sys.stdin.readlines()
line_comparison(line)


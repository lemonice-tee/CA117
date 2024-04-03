#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
  for char in line:
    if char == "m":
      line = line.replace(char, "M", 1)
      break
  print(line.strip("\n"))
#    while i < len(line):
#      mline = line.split("m")
#      mline[1].captalize()
#    print(line)

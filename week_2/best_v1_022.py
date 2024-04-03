#!/usr/bin/env python3

import sys

try:
  with open (sys.argv[1]) as f:
    line = f.readlines()

  for x in line:
    x = x.split()
    score = int(x[0])
    
    mark = 0
    i = 0
    while i < len(line):
      if mark > score:
        mark == score
      i += 1
  print(mark)

  i = 0
  while i < len(line):
    x = line[1].split()
    if int(x[0]) == mark:
      print(f'Best student: {x[1:]}')
      print(f'Best mark: {x[0]}')
      i = len(line)
    i += 1

except FileNotFoundError:
  print(f'The file {sys.argv[1]} does not exist.')

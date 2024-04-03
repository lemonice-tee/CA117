#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip().lower().split()
  line = "".join(line)
#  for x in line and y in line:
#    if x != -y:
#      return False
#    else:

  i = 0
  while i < len(line):
    if not line[i].isalnum():
      line = line.replace(line[i], "", 1)
    i += 1
  print(line == line[::-1])
# if any character not .isalnum:
#                  x -> // <- y
#                       ^
#  if both are unequal, end search and return false

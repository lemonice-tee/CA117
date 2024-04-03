#!/usr/bin/env python3

import sys

from string import punctuation

seen = {}
def line_frequencies(line):
  for word in line:
    word = word.strip(punctuation)
    if word not in seen:
      seen[word] = 1
    else:
      seen[word] += 1

# for item in seen:
#   seen = sorted(seen.items())
#   print(f'{item} : {seen[item]}')


for line in sys.stdin:
  line = line.strip().lower().split()
  line_frequencies(line)

for item in sorted(seen):
  print(f'{item} : {seen[item]}')

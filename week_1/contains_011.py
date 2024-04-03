#!/usr/bin/env python3

import sys

def contains(l_word, r_word):
  for l in l_word:
    if l not in r_word:
      return False
    else:
      r_word = r_word.replace(l, '', 1)
  return True

for line in sys.stdin:
  line = line.strip().split()
  l_word = line[0].upper()
  r_word = line[-1].upper()
  print(contains(l_word, r_word))

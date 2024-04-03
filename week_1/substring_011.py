#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip().split()
  f_word = line[0].lower()
  l_word = line[-1].lower()
  if f_word in l_word:
    print('True')
  else:
    print('False')

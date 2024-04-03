#!/usr/bin/env python3

import sys

from string import punctuation

words = sys.stdin.readlines()
seen = []
final = []


for w in words:
  w = w.split()
  fsentence = []
  for v in w:
    fv = v
    v = v.lower().strip(punctuation)
    if v in seen:
      fsentence.append('.')
    else:
      fsentence.append(fv)
      seen.append(v)
  fsentence = ' '.join(fsentence)
  final.append(fsentence)
#for p in fi
#  "\ n".join(w)
print("\n".join(final))
#print(final)

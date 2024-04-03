#!/usr/bin/env python3

import sys

names = sys.stdin.readlines()

#print(names)
even_index = []
odd_index = []

i = 0
while i < len(names):
  if i % 2 == 0:
    even_index.append(names[i].strip())
  else:
    odd_index.append(names[i].strip())
  i += 1

for n in even_index:
  print(n)
for m in odd_index[::-1]:
  print(m)

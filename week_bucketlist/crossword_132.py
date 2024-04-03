#!/usr/bin/env python3

import sys

shared_letter = []
def make_crossword(a, b):
  for c in a:
    if c in b:
      shared_letter.append(c)
  x = shared_letter[-1]
  #print(shared_letter)
  index_a = a.rfind(x)
  index_b = b.rfind(x)
  #print(index_a)
  #print(index_b)
  i = 0
  while i < len(a):
  #when index_a is == i then print out my b
    if i == index_a:
      print(b)
    else:
      print("." * len(b[:index_b]) + a[i] + "." * len(b[index_b:-1]))
    i += 1
line = sys.stdin.readline().strip().split()
a = line[0]
b = line[-1]
make_crossword(a, b)
  #print(a)
  #print(b)
  #print(line)

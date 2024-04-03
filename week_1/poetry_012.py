#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()

long = 0
lines = []

for i in range(len(words)):
   line = words[i].strip()

   if len(line) > long:
      long = len(line)
   lines.append(line)

for i in lines:
   print(f"{i: ^{long}}")

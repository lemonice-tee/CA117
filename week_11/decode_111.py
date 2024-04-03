#!/usr/bin/env python3

import sys

vowels = 'aeiou'
for words in sys.stdin:
  words = words.strip()
  i = 0
  while i < len(words):
    if words[i] in vowels:
      words = words[:i] + words[i + 2:]
    i += 1
  print(words)


#vowels = "aeiou"
#for line in sys.stdin:
#  line = line.strip()
#  i = 0
#  while i < len(line):
#    if line[i] in vowels:
#      line = line[:i] + line[i + 2:]
#    i += 1
#  print(line)

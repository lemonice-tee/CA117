#!/usr/bin/env python3

import sys

from string import punctuation

vowels = {}
vowel_set = set("aeiou")

def value(item):
  return item[1]

def vowel_frequencies(c):
  if c in vowel_set:
    if c not in vowels:
      vowels[c] = 1
    else:
      vowels[c] += 1


text = sys.stdin.read()

for word in text:
  for c in word:
    vowel_frequencies(c.lower())

max_2 = len(str(max(vowels.values())))
max_2 = int(max_2)
#print(max_2)

for key, value in sorted(vowels.items(), key=value, reverse=True):
  print(f'{key} : {value:>{max_2}}')

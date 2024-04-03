#!/usr/bin/env python3

import sys

vowels = ['a', 'e', 'i', 'o', 'u']

def tagger(object):
  return object[1]

has_vowels = {}

def most_vowels(word):
  i = 0
  j = 0
  while i < len(word) - 1:
#    print(word[i], word[i + 1])
    if word[i] == word[i + 1]:
      if word[i] in vowels:
        j += 1
        has_vowels[word] = j
 #       print(word)
    else:
      pass
    i += 1

for line in sys.stdin:
  word = line.strip()
  most_vowels(word)

print(max(sorted(has_vowels.items()), key=tagger)[0])

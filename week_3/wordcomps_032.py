#!/usr/bin/env python3

import sys

def word_comps(word):
  vowel = "aeiou"
  c = 10
  e = 0
  i = 1000
  smallest = ""
  sword_vowel = []
  wordend_iary = []
  wordcont_e = []
  sword_vowel = [x.strip() for x in word if ("a" in x and "e" in x and "i" in x and "o" in x and "u" in x)]

  for x in sword_vowel:
    if len(x) < i:
      i = len(x)
      smallest = x


  wordend_iary = [x for x in word if x.strip().endswith("iary")]

  for x in word:
    if x.lower().count("e") > e:
      e = x.lower().count("e")
  wordcont_e = [x.strip() for x in word if x.lower().count("e") == e]

  print(f"Shortest word containing all vowels: {smallest}")
  print(f"Words ending in iary: {len(wordend_iary)}")
  print(f"Words with most e's: {wordcont_e}")

word = sys.stdin.readlines()
word_comps(word)


#!/usr/bin/env python3

import sys

for line in sys.stdin:
  letter = line.strip()
  nes = ["ch", "sh", "s", "z", "x"]
  nc = ["a", "e", "i", "o", "u"]
  nfe = ["f", "fe"]
  if letter[-2:] in nes:
    letter = letter +"es"
  elif letter[-1] in nes:
    letter = letter + "es"
  elif letter[-2] not in nc and letter[-1] == "y":
    letter = letter[:-1]
    letter = letter + "ies"
  elif letter[-2:] in nfe:
    letter = letter[:-2]
    letter = letter + "ves"
  elif letter[-1] in nfe:
    letter = letter[:-1]
    letter = letter + "ves"
  elif letter[-1] == "o":
    letter = letter + "es"
  else:
    letter = letter + "s"
  print(letter)

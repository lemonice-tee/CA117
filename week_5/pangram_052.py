#!/usr/bin/env python3

import sys

from string import punctuation

nums = "0123456789"
def pangram_detect(line):
  for x in line:
    if x in punctuation or x in nums:
      line = line.replace(x, "", 1)
    elif x == " ":
      line = line.replace(x, "", 1)
  return(line)



def alpha_count(newline):
  letters = "abcdefghijklmnopqrstuvwxyz"
  for i in newline:
    if i in letters:
      letters = letters.replace(i, "", 1)
    else:
      pass

  if len(letters) != 0:
    missing = sorted(letters)
    print(f'missing {"".join(missing)}')
  else:
    print("pangram")


for line in sys.stdin:
  line = line.strip().lower()
  #print(line)
  newline = pangram_detect(line)
  alpha_count(newline)

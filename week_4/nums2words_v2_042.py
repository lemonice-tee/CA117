#!/usr/bin/env python3

import sys

d = {
"0" : "zero",
"1" : "one",
"2" : "two",
"3" : "three",
"4" : "four",
"5" : "five",
"6" : "six",
"7" : "seven",
"8" : "eight",
"9" : "nine",
"10" : "ten"
}

def num_to_words(num):
  nums = []
  for n in num:
    if n in d:
      nums.append(d[n])
    else:
      nums.append("unknown")
  print(" ".join(nums))


for line in sys.stdin:
  num = line.strip().split()
  num_to_words(num)


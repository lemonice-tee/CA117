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
  print(" ".join(nums))

  
  #for num in range(0,(10 + 1)):
    # create list of nums(int)
    #          "         (words)
    # create dictionary
    # key=int
    # val=words
    # for word == key:
    #   print(item)


for line in sys.stdin:
  num = line.strip().split()
  num_to_words(num)

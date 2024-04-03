#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
dictionary = {}
letters = "A, B, C, D, E, F"
letters = letters.split(", ")

def tagger(item):
  return item[1]
#def abc_order(nums):
 # abc = {}
 # for x in nums.sorted():
first_line = lines[0].strip().split()
numbers = []
for number in first_line:
  number = int(number)
  numbers.append(number)
numbers = (sorted(numbers))
i = 0
while i < len(numbers):
  dictionary[letters[i]] = numbers[i]
  i += 1

second_line = lines[1].strip()
output = []
for c in second_line:
  output.append(str(dictionary[c]))
print(" ".join(output))

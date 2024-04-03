#!/usr/bin/env python3

import sys

def product(num):
  for n in num:
    nums = [int(n for n in num and n != 0)]
    print(nums)
  for d in nums:
    total = total * d
    return total

for line in sys.stdin:
  num = line.strip().split()
  print(num)
  product(num)

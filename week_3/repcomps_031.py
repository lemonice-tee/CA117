#!/usr/bin/env python3

import sys

def re_comps(num):
  num += 1
  multiples_of_3 = []
  multiples_of_3 = [n if n % 3 == 0 else 0 for n in range(1, num)]

  print(f'Non-multiples of 3 replaced: {multiples_of_3}')

for line in sys.stdin:
  line = line.strip().split()
  nums = [int(n) for n in line]
  for num in nums:
    re_comps(num)

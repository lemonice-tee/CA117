#!/usr/bin/env python3

import sys

def num_comps(num):
  num += 1
  primes = []
  primes = [n if n == 2 elif n == 3 elif n % 2 != 0 elif n  n for n in range(1, num)]

  print(f'Primes: {primes}')
#is_prime


for line in sys.stdin:
  line = line.strip().split()
  nums = [int(n) for n in line]
  for num in nums:
    num_comps(num)

#!/usr/bin/env python3

import sys

def num_comps(num):
  num += 1
  multiples_of_3 = []
  squaremultiple_of_3 = []
  doublemultiple_of_4 = []
  multiples_3_or_4 = []
  multiples_3_and_4 = []
  multiples_of_3 = [n for n in range(1, num) if  n % 3 == 0]
  squaremultiple_of_3 = [n*n for n in range(1, num) if n % 3 == 0]
  doublemultiple_of_4 = [n*2 for n in range(1, num) if n % 4 == 0]
  multiples_3_or_4 = [n for n in range(1, num) if n % 3 == 0 or n % 4 == 0]
  multiples_3_and_4 = [n for n in range(1, num)  if n % 3 == 0 and n % 4 == 0]

  print(f'Multiples of 3: {multiples_of_3}')
  print(f'Multiples of 3 squared: {squaremultiple_of_3}')
  print(f'Multiples of 4 doubled: {doublemultiple_of_4}')
  print(f'Multiples of 3 or 4: {multiples_3_or_4}')
  print(f'Multiples of 3 and 4: {multiples_3_and_4}')

for line in sys.stdin:
  line = line.strip().split()
  nums = [int(n) for n in line]
  for num in nums:
    num_comps(num)

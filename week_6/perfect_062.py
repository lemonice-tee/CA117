#!/usr/bin/env python3

import sys

numbers = []

def get_divisors(integer):
  numbers = [n for n in range(1, (integer + 1)) if integer % n == 0]
  return numbers

def get_proper_divisors(integer):
  numbers = [n for n in range(1, integer) if integer % n == 0]
  return numbers

total = 0
def is_perfect(integer):
  numbers = [n for n in range(1, integer) if integer % n == 0]
  total = sum(numbers)
  if integer == total:
    return True
  return False

for line in sys.stdin:
  integer = int(line.strip())
  #print(integer)
  print(get_divisors(integer))
  print(get_proper_divisors(integer))
  print(is_perfect(integer))

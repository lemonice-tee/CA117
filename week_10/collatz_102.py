#!/usr/bin/env python3

def collatz(n):
  print(n)
  if n == 1:
    return n
  elif n > 1:
    if n % 2 == 0:
      return collatz(n // 2)
    return collatz((3 * n) + 1)
  return collatz(n)
#  elif n == 1:
#    return 1
#  else:
#    return collatz(n // 2) if n % 2 == 0
#    return collatz((n * 3) + 1) if n % 2 == 1

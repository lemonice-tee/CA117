#!/usr/bin/env python3

m = 0
def minimum(n=[], m=20):
  if n == []:
    return m
  elif m > n[-1]:
    m = n[-1]
  return minimum(n[:-1], m)

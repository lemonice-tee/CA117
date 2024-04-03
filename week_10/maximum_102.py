#!/usr/bin/env python3

def maximum(n=[], m=0):
  if len(n) == 0:
    return m
  elif m < n[-1]:
    m = n[-1]
  return maximum(n[:-1], m)

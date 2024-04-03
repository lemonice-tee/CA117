#!/usr/bin/env python3

def count(s=(), n=0):
  if s == '':
    return n
#  elif s!= ():
#    s = s[:-1]
#    n += 1
  return count(s[:-1], n + 1)

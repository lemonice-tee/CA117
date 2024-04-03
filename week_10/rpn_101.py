#!/usr/bin/env python3

class Stack(object):
  def __init__(self):
    self.s = []
  def push(self, item):
    return self.s.append(item)
  def pop(self):
    return self.s.pop()
  def top(self):
    return self.s[-1]
  def is_empty(self):
    return len(self.s) == 0
  def __len__(self):
    return len(self.s)


import sys

from math import sqrt

def calculator(object):
  binops = {
  '+': float.__add__,
  '-': float.__sub__,
  '*': float.__mul__,
  '/': float.__truediv__
  }

  uniops = {
  'n': float.__neg__,
  'r': sqrt
  }

#  object = sys.stdin.readlines()
#  expression = object.()
  expression = object
  s = Stack()
  expression = expression.split()
  for e in expression:
    #if e not in binops and e not in uniops:
    #  s.push(float(e))
    if e in binops:
      right = s.pop()
      left = s.pop()
      s.push(binops[e](left, right))
    elif e in uniops:
      top = s.pop()
      s.push(uniops[e](top))
    else:
      s.push(float(e))
  return s.pop()

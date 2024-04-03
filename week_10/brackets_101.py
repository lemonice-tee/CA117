#!/usr/bin/env python3

class Stack(object):

  def __init__(self):
    self.l = []

  def pop(self):
    return self.l.pop()

  def push(self, e):
    return self.l.append(e)

  def top(self):
    return self.l[-1]

  def is_empty(self):
    return len(self.l) == 0

  def __len__(self):
    return len(self.l)


def matcher(bstring):
  d = {')' : '(', ']' : '[', '}' : '{'}
  bstack = Stack()
  #if (len(bstring) % 2) == 1:
  #  return False
  #else:
  for bracket in bstring:
    try:
      if bracket not in d:
        bstack.push(bracket)
      else:
        if bstack.top() == d[bracket]:
          bstack.pop()
    except IndexError:
      return False
  return bstack.is_empty()
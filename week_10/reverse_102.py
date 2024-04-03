#!/usr/bin/env python3

def reverse(l, nl=None):
  if nl == None:
    nl = []
  if l == []:
    return nl
  nl.append(l[-1])
  return reverse(l[:-1], nl)

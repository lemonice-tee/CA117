#!/usr/bin/env python3

import math

class Student(object):

  def __init__(self, name, sid, modlist=None):
    self.name = name
    self.sid = sid
    self.modlist = [] if modlist is None else modlist

  def average_mark(self, modlist):
    i = 0
    for m in modlist:
      i += m[-1]
    mark = i / len(modlist)
    return math.ceil(mark)

  def __str__(self):
    lines = []
    lines.append(f'Name: {self.name}\nID: {self.sid}')
    lines.append(f'Modules: {", ".join(sorted([x[0] for x in self.modlist]))}')
    lines.append(f'Average mark: {self.average_mark(self.modlist)}')
    return '\n'.join(lines)

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

def tagger(item):
    return item[1]
class Classlist(object):

  def __init__(self, students=None):
    if students is None:
        self.students = {}
    else:
        self.students = students
  def sort(self, other):
    i = 0
    for marks in self.modlist:
      self.students =sorted(self.student(), value = self.modlist.average_marks, reverse=True)
  def __eq__(self, other):
    return self.modlist.average_mark() == other.modlist.average_mark()

  def __gt__(self, other):
    return self.modlist.average_mark() > other.modlist.average_mark()

  def __ge__(self, other):
    return self.modlist.average_mark >= other.modlist.average_mark()

  def add(self, student):
    self.students[student] = student.average_mark(student.modlist)
  def __str__(self):
    output = []
    for k, v in sorted(self.students.items(), key=tagger, reverse=True):
       output.append(str(k))
    x = "\n".join(output)
    return f'{x}'

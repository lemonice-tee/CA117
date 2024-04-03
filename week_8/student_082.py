#!/usr/bin/env python3

class Student(object):

  def __init__(self, sid, name, modlist=None):
    self.sid = sid
    self.name = name
    if modlist is None:
        self.modlist = []
    else:
        self.modlist = modlist

  def add_module(self, module):
    if module not in self.modlist:
      self.modlist.append(module)
    else:
      pass

  def del_module(self, module):
    if module in self.modlist:
      self.modlist.remove(module)
    else:
      pass

  def __str__(self):
    return f'ID: {self.sid}\nName: {self.name}\nModules: {", ".join(sorted(self.modlist))}'

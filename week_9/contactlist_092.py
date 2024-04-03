#!/usr/bin/env python3

class Contact(object):

  def __init__(self, name, phone, email):
    self.name = name
    self.phone = phone
    self.email = email

  def __str__(self):
    return f'{self.name} {self.phone} {self.email}'

class Contactlist(object):

  def __init__(self, d=None):
    if d is None:
      self.d = {}
    else:
      self.d = d

  def add(self, contact):
    if contact.name in self.d:
       self.d[contact.name] = contact
    else:
       self.d[contact.name] = contact

  def remove(self, name):
    if name in self.d:
      del self.d[name]

  def get(self, name):
    if name in self.d:
      return self.d[name]
    else:
       return None

  def __str__(self):
    lines =[]
    lines.append(f'Contact list\n------------')

    for k, v in sorted(self.d.items()):
      lines.append(f'{v}')
    return '\n'.join(lines)
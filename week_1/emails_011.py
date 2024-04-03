#!/usr/bin/env python3

import sys

def get_name(f_name, s_name):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  for c in s_name:
    if c not in alpha:
      s_name.replace(c, '', 1)
    else:
      pass
  name = []
  name.append(f_name.capitalize())
  name.append(s_name.capitalize())
  #for append(f_name.capitalize() + ' ' + s_name)
  return name

for line in sys.stdin:
  line = line.strip().split('.')
  f_name = line[0]
  s_name = line[1]
  print(get_name(f_name, s_name))

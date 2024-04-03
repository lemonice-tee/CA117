#!/usr/bin/env python3

def swap_keys_values(d):
  keys = []
  values = []
  for k, v in d.items():
    keys.append(k)
    values.append(v)
  reverse = {}
  i = 0
  while i < len(keys):
    reverse[values[i]] = keys[i]
    i += 1
  return reverse
# for line in sys.stdin:
#   k, v = line.strip().split()
#   d = {(k),(v)}
#  swap_key_values(d)

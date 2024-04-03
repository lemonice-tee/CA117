#!/usr/bin/env python3

import sys

litres = sys.stdin.readline().strip()
buckets = sys.stdin.readline().strip()

buckets = buckets.split()

i = 0
for x in buckets:
  if int(litres) >= int(x):
    litres = int(litres) - int(x)
    i += 1
  else:
    break

print(i)

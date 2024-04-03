#!/usr/bin/env python3

import sys

def cal_count(calories):
  if calories <= 400:
    return (calories // 400) + 1
  elif calories > 400:
    if calories % 400 == 0:
      return (calories // 400)
    else:
      return (calories // 400) + 1

for line in sys.stdin:
  calories = line.strip()
  calories = int(calories)
  print(cal_count(calories))

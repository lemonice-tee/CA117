#!/usr/bin/env python3

import sys, math

line = int(sys.stdin.readline())
output_len = int(round(math.log(line, 2), 0))
start_pt = 2 ** output_len - 1
if start_pt == 0:
  start_pt = 1
pos = line - start_pt
binaryN = str(bin(pos))[2:]
if len(binaryN) != output_len:
  pads = output_len - len(binaryN)
  binaryN = ('0' * pads) + binaryN
binaryN = binaryN.replace('0', '3')
binaryN = binaryN.replace('1', '9')

print(binaryN)

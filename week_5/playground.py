#!/usr/bin/env python2

d = {1: "prize", 2: "none", 3: "none"}
print(d)

letter = "A"

if letter == "A":
   d[1], d[2] = d[2], d[1]

print(d)

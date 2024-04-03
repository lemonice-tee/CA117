#!/usr/bin/env python3

import sys

d = {
"0" : "zero",
"1" : "one",
"2" : "two",
"3" : "three",
"4" : "four",
"5" : "five",
"6" : "six",
"7" : "seven",
"8" : "eight",
"9" : "nine",
"10" : "ten"
}
e = {
"11" : "eleven",
"12" : "twelve",
"13" : "thirteen",
"14" : "fourteen",
"15" : "fifteen",
"16" : "sixteen",
"17" : "seventeen",
"18" : "eighteen",
"19" : "nineteen",
"20" : "twenty"
}
f = {
"2" : "twenty",
"3" : "thirty",
"4" : "forty",
"5" : "fifty",
"6" : "sixty",
"7" : "seventy",
"8" : "eighty",
"9" : "ninety",
}

def num_to_words(num):
  nums = []
  for n in num:
    if len(n) == 1:
      nums.append(d[n])
    elif len(n) > 1 and len(n) < 3 and int(n) <= 20:
       nums.append(e[n])
    elif len(n) > 1 and len(n) < 3 and int(n) > 20 and str(n[-1]) != "0":
       nums.append(f[n[0]] + "-" +  d[n[1]])
    elif len(n) > 1 and len(n) < 3 and int(n) > 20 and str(n[-1]) == "0":
       nums.append(f[n[0]])
    else:
       nums.append("one hundred")
  print(" ".join(nums))

for line in sys.stdin:
  num = line.strip().split()
  num_to_words(num)

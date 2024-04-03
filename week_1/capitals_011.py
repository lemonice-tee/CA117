#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip().split()
  for word in line:
    f_letter = word[0].capitalize()
    l_letter = word[-1].capitalize()
    print(f_letter + word[1:-1] + l_letter)
#    
#    first_letter = line[0]
#    last_letter = line[-1]
#    print(first_letter)
#    print(last_letter)

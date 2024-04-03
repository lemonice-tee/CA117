#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip().split(' ')
  x = line[0]
  y = line[1]
  n = line[-1]
  #print()
  for number in range(1, (int(n) + 1)):
    if int(number) % int(x) == 0 and int(number) % int(y) != 0:
      print('fizz')
    elif int(number) % int(y) == 0 and int(number) % int(x) != 0:
      print('buzz')
    elif int(number) % int(x) == 0 and int(number) % int(y) == 0:
      print('fizzbuzz')
    else:
      print(int(number))

# elif int(number) % int(x) != 0:
#   print(number)
# elif int(number) % int(y) != 0:
#   print(number)


#!/usr/bin/env python3

import sys

def binsearch(query, sorted_list):

    '''Return True if query in sorted_list else False'''

    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        # print(f'{low} {mid} {high}')

        if sorted_list[mid] < query:
            # Search RHS
            low = mid + 1

        elif sorted_list[mid] > query:
            # Search LHS
            high = mid - 1

        else:
            # Found it
            return True

    # Not found
    return False
    
def reverse_comp(word):
  seen = [x.strip() for x in word if len(x.strip()) >= 5]
  lower5 = [x.lower() for x in seen]

  # if the word > 5// ::-1 not in seen, append to seen
    # strip all of the words smaller than 5// keep words >=5
  # if the word is in seen and word::-1 is found, append to reverse
  reverse = [x for x in seen if binsearch(x.lower()[::-1], lower5)]
  return reverse


word = sys.stdin.readlines()
print(reverse_comp(word))

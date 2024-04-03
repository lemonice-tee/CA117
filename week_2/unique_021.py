#!/usr/bin/env python3

import sys

def unique_words(word):
  seen = []
  for x in word:
    seen = [x.strip().lower() for x in word and x.isalnum()]

    print(seen)

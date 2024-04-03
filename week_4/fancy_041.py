#!/usr/bin/env python3

import sys


file_name = sys.argv[1]

contacts = {}

def contact_dictionary(line):
  name = line[0]
  number = line[1]
  email = line[-1]
  contacts[name] = (number, email)
  return contacts
with open(file_name) as f:
  lines = f.readlines()
  for line in lines:
    line = line.strip().split(" ")
    contacts = contact_dictionary(line)
def locate_contact(line):
    name = line[0]
    if name in contacts:
      print(f'Name: {name}')
      numb = contacts[name][0]
      print(f'Phone: {numb}')
      email = contacts[name][-1]
      print(f'Email: {email}')
    else:
      print(f'Name: {name}')
      print("No such contact")


for line in sys.stdin:
  line = line.strip().split()
  locate_contact(line)

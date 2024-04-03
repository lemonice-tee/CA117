#!/usr/bin/env python3

import sys

import calender

import datetime

def birthdays(line):
  line = datetime.date(line)
  date = line.weekday()
  mon_date = []
  tue_date = []
  wed_date = []
  thu_date = []
  fri_date = []
  sat_date = []
  sun_date = []
  for x in date:
    mon_date = ["Monday" for int(x) == 0 and x in date]
    tue_date = ["Tuesday" for int(x) == 1 and x in date]
    wed_date = ["Wednesday" for int(x) == 2 and x in date]
    thu_date = ["Thursday" for int(x) == 3 and x in date]
    fri_date = ["Friday" for int(x) == 4 and x in date]
    sat_date = ["Saturday" for int(x) == 5 and x in date]
    sun_date = ["Sunday" for int(x) == 6 and x in date]

    print(f"You were born on {mon_date} and {mon_date}'s child is fair of face")
    print(f"You were born on {tue_date} and {tue_date}'s child is full of grace")
    print(f"You were born on {wed_date} and {wed_date}'s child is full of woe")
    print(f"You were born on {thu_date} and {thu_date}'s child has far to go")
    print(f"You were born on {fri_date} and {fri_date}'s child is loving and giving")
    print(f"You were born on {sat_date} and {sat_date}'s child works hard for a living")
    print(f"You were born on {sun_date} and {sun_date}'s child fair and wise and good in every way")


for line in sys.stdin:
  line = line.strip()
  for date in line:
    birthdays(date)

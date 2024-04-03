#!/usr/bin/env python3

class Triathlete(object):

  def __init__(self, name, tid):
    self.name = name
    self.tid = tid
    self.times = {}
    #for k, v in self.times:
    #  self.times[k] = v

  def add_time(self, race, time):
    self.times[race] = time

  def get_time(self, race):
    return self.times[race]

  def total_time(self):
    return sum(self.times.values())

  def __eq__(self, other):
    return self.total_time() == other.total_time()

  def __gt__(self, other):
    return self.total_time() > other.total_time()

  def __str__(self):
    return f'Name: {self.name}\nID: {self.tid}\nRace time: {self.total_time()}'

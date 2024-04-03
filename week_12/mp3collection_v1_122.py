#!/usr/bin/env python3

class MP3Track(object):

  def __init__(self, title, duration):
    self.title = title
    self.duration = duration

  def __str__(self):
    return f'Title: {self.title}\nDuration: {self.duration}'


class MP3Collection(object):

  def __init__(self):
    self.collection = {}

  def lookup(self, track_title):
    if track_title in self.collection:
      return self.collection[track_title]
    return None

  def add(self, track):
    if track.title in self.collection:
      pass
    else:
      self.collection[track.title] = track

  def remove(self, track_title):
    if track_title in self.collection.keys():
      self.collection.pop(track_title)

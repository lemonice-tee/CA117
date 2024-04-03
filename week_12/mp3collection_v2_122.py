#!/usr/bin/env python3

class MP3Track(object):

  def __init__(self, title, duration, artists=None):
    self.title = title
    self.duration = duration
    if artists == None:
      self.artists = []
    else:
      self.artists = artists

  def __str__(self):
    return f'Title: {self.title}\nBy: {", ".join(self.artists)}\nDuration: {self.duration}'


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
    c = MP3Collection()
    if track_title in self.collection.keys():
      self.collection.pop(track_title)
    for track_title in self.collection:
      other.collection.pop(track_title)


  def __add__(self, other):
    c = MP3Collection()
    for track_title in self.collection:
      self.collection[track_title][:]
    for track_title in self.collection:
      other.collection[track_title][:]


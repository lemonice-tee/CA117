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

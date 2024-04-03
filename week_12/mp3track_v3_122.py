#!/usr/bin/env python3

class MP3Track(object):

  def __init__(self, title, duration, artists=None):
    self.title = title
    self.duration = duration
    if artists == None:
      self.artists = []
    else:
      self.artists = artists

  def to_mins_sec(self, duration):
    m, s = divmod(duration, 60)
    return m, s

  def __str__(self):
    m, s = self.to_mins_sec(self.duration)
    return f'Title: {self.title}\nBy: {", ".join(self.artists)}\nDuration: {m:01d}:{s:02d}'

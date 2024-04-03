#!/usr/bin/env python3

class Point(object):

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def midpoint(self, other):
    midpoint_x = ((self.x + other.x)/2)
    midpoint_y = ((self.y + other.y)/2)
    return Point(midpoint_x, midpoint_y)

  def __str__(self):
    return f'({self.x:.01f}, {self.y:.01f})'

class Circle(object):

  def __init__(self, centre=None, radius=1):
     if centre is None:
       self.point = Point()
     else:
       self.point = centre
     self.centre = self.point
     self.radius = radius

  def __str__(self):
    return f'Centre: {self.centre}\nRadius: {self.radius}'

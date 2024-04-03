#!/usr/bin/env python3

class Point(object):

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def midpoint(self, other):
    newcircle_midpoint_x = ((self.x + other.x)/2)
    newcircle_midpoint_y = ((self.y + other.y)/2)
    return Point(newcircle_midpoint_x, newcircle_midpoint_y)

  def __str__(self):
    return f'({self.x:.01f}, {self.y:.01f})'

class Circle(object):

  def __init__(self, centre=None, radius=1):
     if centre is None:
       self.centre = Point()
     else:
       self.centre = centre
     self.radius = radius

#  def midpoint(self, other):
#     x = (self.centre.x + other.x)/2
#     y = (self.centre.y + other.y)/2
#     return Point(x, y)

  def __add__(self, other):
    radius = self.radius + other.radius
    centre = self.centre.midpoint(other.centre)
    return Circle(centre, radius)


  def __str__(self):
    return f'Centre: {self.centre}\nRadius: {self.radius}'

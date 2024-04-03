#!/usr/bin/env python3

class Score(object):

  def __init__(self, goals=0, points=0):
    self.goals = goals
    self.points = points

  def __eq__(self, other):
    return self.score_to_points() == other.score_to_points()

  def __gt__(self, other):
    return self.score_to_points() > other.score_to_points()

  def __ge__(self, other):
    return self.score_to_points() >= other.score_to_points()

  def score_to_points(self):
    return self.goals * 3 + self.points

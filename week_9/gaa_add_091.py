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

  def __add__(self, other):
    total_goals = self.goals + other.goals
    total_points = self.points + other.points
    return Score(total_goals, total_points)

  def __iadd__(self, other):
    self.goals += other.goals
    self.points += other.points
    return self

  def score_to_points(self):
    return self.goals * 3 + self.points

  def __str__(self):
    return f'{self.goals} goal(s) and {self.points} point(s)'

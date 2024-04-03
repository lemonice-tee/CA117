#1/usr/bin/env python3

class Queue(object):

  def __init__(self):
    self.q = []

  def first(self):
    return self.q[0]

  def dequeue(self):
    return self.q.pop(0)

  def enqueue(self, e):
    return self.q.append(e)

  def is_empty(self):
    return len(self.q) == 0

  def __len__(self):
    return len(self.q)

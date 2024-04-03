#!/usr/bin/env python3

class Meeting(object):

  def __init__(self, hour, minute, duration):
    self.hour = hour
    self.minute = minute
    self.duration = duration

  def __str__(self):
    return f'{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)'


class Schedule(object):

  def __init__(self, s=None):
    if s is None:
      self.s = {}
    else:
      self.s = s

  def add(self, meeting):
    if meeting.hour in self.s:
      self.s[meeting.hour] = meeting
    else:
      self.s[meeting.hour] = meeting

  def __str__(self):
    lines =[]
    lines.append(f'Schedule\n--------')
    c = 0
    for k, v in sorted(self.s.items()):
      c += 1
      lines.append(f'{v}')
#    lines.append(f'Meetings today: (len{})')
    lines.append(f'Meetings today: {c}')
    return '\n'.join(lines)

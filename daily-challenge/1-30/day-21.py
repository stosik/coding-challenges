# This problem was asked by Snapchat.

# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
# find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

class IntervalLog:
  def __init__(self, value, start_end):
    self.value = value
    self.start_end = start_end

def solution(intervals):
  interval_logs = []

  for interval in intervals:
    interval_logs.append(IntervalLog(interval[0], 1))
    interval_logs.append(IntervalLog(interval[1], -1))

  interval_logs.sort(key=lambda d: (d.value, -d.start_end)) # O(nlogn)

  intersections = 0
  active_intersections = 0

  for log in interval_logs: # O(n * 2)
    active_intersections += log.start_end
    if log.start_end > 0:
      intersections += active_intersections - 1 # -1 as we count intersections and not the number of disks
  return intersections


print(solution([(30, 75), (0, 50), (60, 150)])) # 2
# Given an array A of non-negative integers, A[i] corresponds to the radius of a disc located at (0,i) on the Cartesian plane.
# Two discs are said to intersect iff they have at least one common point.
# Compute the total number of intersecting pairs of discs.

# https://app.codility.com/programmers/task/number_of_disc_intersections/

class DiscLog():
  def __init__(self, x, start_end):
    self.x = x
    self.start_end = start_end
 
def solution(A):
  discHistory = []
  for i in range(len(A)):
    discHistory.append(DiscLog(i - A[i], 1))
    discHistory.append(DiscLog(i + A[i], -1))
  
  discHistory.sort(key=lambda d: (d.x, -d.start_end))
  intersections = 0
  activate_intersections = 0

  for log in discHistory:
    activate_intersections += log.start_end
    if log.start_end > 0:
      intersections += activate_intersections - 1
  return intersections

print(solution([1, 5, 2, 1, 4, 0]))


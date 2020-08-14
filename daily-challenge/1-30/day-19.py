# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different colors.
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
# return the minimum cost which achieves this goal.

# N x K (matrix)


def solution(costs):
  if costs == None or len(costs) == 0:
    return 0
    
  n = len(costs)
  k = len(costs[0])

  min1 = 0
  min2 = 0
  idx1 = -1

  for i in range(n):
    m1 = sys.maxint
    m2 = sys.maxint
    idx2 = -1

    for j in range(k):
      cost = costs[i][j]
      temp_cost = cost + j

      if temp_cost == idx1:
        cost = min2
      else:
       cost = min1

      if cost < m1:
        m2 = m1
        m1 = cost
        idx2 = j
      elif cost < m2:
        m2 = cost
        
    min1 = m1
    min2 = m2
    idx1 = idx2

    return min1
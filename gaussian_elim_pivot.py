from matrix import height
 
from matrix import height

def gaussian_elimination_with_pivot(m):
  """
  Parameters
  ----------
  m  : list of list of floats (matrix)

  Returns
  -------  
  list of floats
      solution to the system of linear equation
  
  Raises
  ------
  ValueError
      no unique solution
  """
  # forward elimination
  n = height(m)
  for i in range(n):
    pivot(m, n, i)
    for j in range(i+1, n):
      m[j] = [m[j][k] - m[i][k]*m[j][i]/m[i][i] for k in range(n+1)]

  if m[n-1][n-1] == 0: raise ValueError('No unique solution')

  # backward substitution
  x = [0] * n
  for i in range(n-1, -1, -1):
    s = sum(m[i][j] * x[j] for j in range(i, n))
    x[i] = (m[i][n] - s) / m[i][i]
  return x

'''
# shorter way to pivot but cannot run in trinket
def pivot(m, n, i):
  max_row = max(range(i, n), key=lambda r: abs(m[r][i]))
  m[i], m[max_row] = m[max_row], m[i]
'''

def pivot(m, n, i):
  max = -1e100
  for r in range(i, n):
    if max < abs(m[r][i]):
      max_row = r
      max = abs(m[r][i])
  m[i], m[max_row] = m[max_row], m[i]

if __name__ == '__main__':
  #m = [[0,-2,6,-10], [-1,3,-6,5], [4,-12,8,12]]
  #m = [[1,-1,3,2], [3,-3,1,-1], [1,1,0,3]]
  m = [[1,-1,3,2], [6,-6,2,-2], [1,1,0,3]]
  print(gaussian_elimination_with_pivot(m))
  
  """  
  m = [[4,4,0,400], [-1,4,2,400], [0,-2,4,400]]   # aj Montri p80  [50, 50, 125]
  print(gaussian_elimination_with_pivot(m))
  """

# gaussian elimination with pivot
# author: Worasait Suwannik
# date: May 2015


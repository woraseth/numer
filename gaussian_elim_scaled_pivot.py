# gaussian elimination with scaled pivot

from matrix import height
 
def gaussian_elimination_with_scaled_pivot(m):
  # forward elimination
  n = height(m)
  scale = [max([abs(m[i][j]) for j in range(n)]) for i in range(n)] 
  for i in range(n):
    pivot(m, n, i, scale)
    for j in range(i+1, n):
      m[j] = [m[j][k] - (m[i][k]*m[j][i]/m[i][i]) for k in range(n+1)]

  if m[n-1][n-1] == 0: raise ValueError('No unique solution')

  # backward substitution
  x = [0] * n
  for i in range(n-1, -1, -1):
    s = sum(m[i][j] * x[j] for j in range(i, n))
    x[i] = (m[i][n] - s) / m[i][i]
  return x

'''
# shorter version but cannot run in trinket
def pivot(m, n, i, scale):
  max_row = max(range(i, n), key=lambda r: abs(m[r][i]/scale[r]))
  scale[i], scale[max_row] = scale[max_row], scale[i]
  m[i], m[max_row] = m[max_row], m[i]
'''

def pivot(m, n, i, scale):
  max = -1e100
  for r in range(i, n):
    if max < abs(m[r][i]/scale[r]):
      max_row = r
      max = abs(m[r][i]/scale[r]) 
  scale[i], scale[max_row] = scale[max_row], scale[i]
  m[i], m[max_row] = m[max_row], m[i]

if __name__ == '__main__':
  m = [[4,4,0,400], [-1,4,2,400], [0,-2,4,400]]   # aj Montri p80  [50, 50, 125]
  print(gaussian_elimination_with_scaled_pivot(m))
  #m = [[2.11,-4.21,0.92,2.01],[4.01,10.20,-1.12,-3.09],[1.09,0.99,0.83,4.21]]  # aj Montri p91 [-0.43, 0.43, 5.12]
  #print(gaussian_elimination(m, SCALED_PIVOT))

# author: Worasait Suwannik
# date: May 2015
 

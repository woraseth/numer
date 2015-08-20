from matrix import height
from matrix import column
 
def jacobi(m, x0=None, eps=1e-5, round=100):
  n  = height(m)
  b  = column(m, n)
  x0 = [0] * n if x0 == None else x0
  x1 = [None] * n
  
  for __ in range(round):
    for i in range(n):
      s = sum(-m[i][j] * x0[j] for j in range(n) if i != j)
      x1[i] = (s + b[i]) / m[i][i]
    if all(abs(x1[i]-x0[i]) < eps for i in range(n)):
      return x1 
    x0, x1 = x1, x0
  raise ValueError('Solution does not converge')
  
if __name__ == '__main__':
  m = [[4,3.2,0.5,9.2],[2.2,3,-0.3,0.9],[-3.1,-0.2,4,7]]
  print(jacobi(m))

# author: Worasait Suwannik
# date: Apr 2015

  # m = [[5,3,41],[2,7,57]]

 

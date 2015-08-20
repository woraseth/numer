from matrix import height

def gauss_seidel(m, x0=None, eps=1e-5, round=100):
  n  = height(m)
  x0 = [0] * n if x0 == None else x0
  x1 = x0[:]      
 
  for __ in range(round):
    for i in range(n):
      s = sum(-m[i][j] * x1[j] for j in range(n) if i != j) 
      x1[i] = (m[i][n] + s) / m[i][i]
    if all(abs(x1[i]-x0[i]) < eps for i in range(n)):
      return x1 
    x0 = x1[:]    
  raise ValueError('Solution does not converge')

if __name__ == '__main__':
  m = [[4,3.2,0.5,9.2], [2.2,3,-0.3,0.9], [-3.1,-0.2,4,7]]
  print(gauss_seidel(m))

# author: Worasait Suwannik http://bit.ly/wannik
# date: May 2015




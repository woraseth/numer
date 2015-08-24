from gauss import *

def least_square(x, y, order, sys_lin_method=gaussian_elimination):
  """
  Parameters
  ----------
  x : list of floats
  y : list of floats
  order : int
  
  Returns
  -------  
  list of floats
      coefficients of a polynomial
  """  
  sx  = [sum(x[j]**i        for j in range(len(x))) for i in range(order*2+1)]
  sxy = [sum(x[j]**i * y[j] for j in range(len(x))) for i in range(order+1)]
  m = []
  for i in range(order+1):
    a = sx[i:(i+order+1)]
    a.append(sxy[i])
    m.append(a)
  return sys_lin_method(m)

if __name__ == '__main__':
  x = [0, 0.5, 1, 1.5, 2, 2.5]
  y = [0.0674, -0.9156, 1.6253, 3.0377, 3.3535, 7.9409]
  print(least_square(x, y, 2))
  
  #x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
  #y = [2.8, 4.1, 5.2, 5.9, 6.8, 8, 9.3, 10, 10.6, 12, 13.4, 14, 15.5]
  #print(least_square(x, y, 1))

# least square interpolation
# author : Worasait Suwannik
# date   : Aug 2015

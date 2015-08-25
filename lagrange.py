def lagrange_interpolation(x, y, u):
  '''
  Parameters
  ----------
  x : list of floats
  y : list of floats
  u : float
  
  Returns
  -------  
  float : an estimate at the point u
  '''
  r = range(len(y))
  a =       [y[i]/product(x[i]-x[j] for j in r if j != i) for i in r]
  return sum(a[i]*product(u   -x[j] for j in r if j != i) for i in r)


def product(a): 
  p = 1
  for i in a: p *= i
  return p
  
if __name__ == '__main__':
  from math import *
  x = [1, 2.5, 4, 5.5, 7]
  y = [log(i) for i in x]
  u = 6
  estim = lagrange_interpolation(x, y, u)
  exact = log(u)
  print(estim, exact)

# author : Worasait Suwannik
# date   : Aug 2015

'''
#shorter way to write a product function
import operator, functools
def product(a): return functools.reduce(operator.mul, a, 1)

# original version
a =       [y[i]/product(x[i]-x[j] for j in range(len(y)) if j != i) for i in range(len(y))]
return sum(a[i]*product(u   -x[j] for j in range(len(y)) if j != i) for i in range(len(y)))
'''

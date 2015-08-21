def newton_interpolation(x, y, u):
  '''
  Parameters
  ----------
  x : list of floats
  y : list of floats
  u : float
  
  Returns
  -------  
  float
      an estimate at the point u
  '''
  g = y[:]
  s = g[0]
  for i in range(len(y)-1):
    g = [(g[j+1]-g[j])/(x[j+i+1]-x[j]) for j in range(len(g)-1)]
    s += g[0] * product(u-x[j] for j in range(i+1))
  return s  

def product(a): 
  p = 1
  for i in a: p *= i
  return p
  
if __name__ == '__main__':
  from math import *
  x = [1, 2.5, 4, 5.5, 7]
  y = [log(i) for i in x]
  u = 6
  estim = newton_interpolation(x, y, u)
  exact = log(u)
  print(estim, exact)

# author : Worasait Suwannik
# date   : Aug 2015

'''
shorter way to write a product function

import operator, functools
def product(a): return functools.reduce(operator.mul, a, 1)
'''

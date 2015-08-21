def secant(f, x0, x1, eps=0.001, max_iteration=100):
  """
  Parameters
  ----------
  f  : function
  x0 : float : initial guess
  x1 : float : initial guess

  Returns
  -------  
  float : a root of function f
  
  Raises
  ------
  ValueError : if cannot find root???
  """
  for __ in range(max_iteration):
    dx = (x1 - x0) * f(x1) / (f(x1) - f(x0)) 
    x0 = x1
    x1 -= dx
    # terminate?
    if abs(f(x1)) < eps and abs(dx) < eps:
      return x1 
  raise ValueError('Cannot find root')

if __name__ == '__main__':
  f = lambda x : x**5 + x**3 +x**2 - 1  
  x = secant(f, 1, 2) 
  #x = secant(f, -3, -2)     # gave incorrect result
  
  #f = lambda x : 5*x**3 - 4*x +1
  #x = secant(f, -3, -2) 
  
  #from math import *
  #f = lambda x : 3*x + sin(x) - e**x  # http://bit.ly/1K5dhQ7
  #x = secant(f, 0, 1) 
  
  print("f(%f) = %f" % (x, f(x)))

# author: Worasait Suwannik
# date: Aug 2015


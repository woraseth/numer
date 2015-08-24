def euler(f, x0, y0, h, x):
  """
  Parameters
  ----------
  f  : function
  x0 : float :  initial value
  y0 : float :  initial value
  h  : float :  step size
  x  : float 
      
  Returns
  -------  
  float : f at x
  """
  while x0 < x:
    y0 += f(x0, y0) * h
    x0 += h
  return y0

if __name__ == '__main__':
  f = lambda x, y : -2*x**3 + 12*x**2 - 20*x + 10
  print(euler(f, 0, 1, 0.5, 4))
  
# author : worasait suwannik
# date   : jul 2015

  #f = lambda x, y : -2*x**3 + 12*x**2 - 20*x + 8.5  # montri p156

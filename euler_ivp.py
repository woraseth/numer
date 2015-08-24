def euler_ivp(f, x0, y0, h, x):
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
  float : solution at x
  """
  for i in range(int((x-x0)/h)):
    y0 += f(x0, y0) * h
    x0 += h
  return y0

if __name__ == '__main__':
  f = lambda x, y : y - x  # from https://www.math.purdue.edu/academic/files/courses/2010spring/MA26200/1_10.pdf
  print(euler_ivp(f, 0, 0.5, 0.1, 1.0))
  
  #f = lambda x, y : -2*x**3 + 12*x**2 - 20*x + 10
  #print(euler(f, 0, 1, 0.5, 4))
  
# author : worasait suwannik
# date   : jul 2015

  #f = lambda x, y : -2*x**3 + 12*x**2 - 20*x + 8.5  # montri p156

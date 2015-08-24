# runge-kutta order 2

def huen(f, x0, y0, h, x):
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
  for i in range(int((x-x0)/h)):
    k1 = f(x0, y0)
    k2 = f(x0 + h, y0 + k1*h)
    
    y0 += (0.5*k1 + 0.5*k2)*h
    x0 += h
  return y0
  
def midpoint(f, x0, y0, h, x):
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
  for i in range(int((x-x0)/h)):
    k1 = f(x0, y0)
    k2 = f(x0 + 0.5*h, y0 + 0.5*k1*h)
    
    y0 += k2*h
    x0 += h
  return y0
  
if __name__ == '__main__':
  f = lambda x, y : -2*x**3 + 12*x**2 - 20*x + 10
  #print(huen(f, 0, 1, 0.5, 4))
  print(midpoint(f, 0, 1, 0.5, 4))
  
# author : worasait suwannik
# date   : jul 2015

  #f = lambda x, y : -2*x**3 + 12*x**2 - 20*x + 8.5  # aj Montri p156

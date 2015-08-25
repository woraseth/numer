def central_difference(f, x, h):
  '''
  Parameters
  ----------
  f : function
  x : number
  h : number
  
  Returns
  -------  
  number 
  '''
  return (f(x+h) - 2*f(x) + f(x-h)) / h**2

if __name__ == '__main__':
  from math import e
  f = lambda x : x**2 * e**(2*x)
  print(central_difference(f, 0, 0.2))
  
# derive using central difference method
# author : worasait suwannik
# date   : aug 2015

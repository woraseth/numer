def forward_difference(f, x, h):
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
  return (f(x+h) - f(x)) / h

def backward_difference(f, x, h):
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
  return (f(x) - f(x-h)) / h

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
  return (f(x+h) - f(x-h)) / (2*h)


if __name__ == '__main__':
  from math import sin
  f = lambda x : x * sin(x)
  print(forward_difference (f, 6, 0.2))
  print(backward_difference(f, 6, 0.2))
  print(central_difference (f, 6, 0.2))
# author: Worasait Suwannik
# date: aug 2015


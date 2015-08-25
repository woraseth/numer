from math import sqrt

gq = [[],[],
      [(-sqrt(1/3), 1), 
       ( sqrt(1/3), 1)],
      [(-sqrt(3/5), 5/9), 
       ( sqrt(3/5), 5/9), 
       ( 0,         8/9)],
      [(-sqrt(3/7-sqrt(6/5)*2/7), (18+sqrt(30))/36), 
       ( sqrt(3/7-sqrt(6/5)*2/7), (18+sqrt(30))/36), 
       (-sqrt(3/7+sqrt(6/5)*2/7), (18-sqrt(30))/36),
       ( sqrt(3/7+sqrt(6/5)*2/7), (18-sqrt(30))/36)],
      [(-sqrt(5-2*sqrt(10/7))/3, (322+13*sqrt(70))/900),
       ( sqrt(5-2*sqrt(10/7))/3, (322+13*sqrt(70))/900),
       (-sqrt(5+2*sqrt(10/7))/3, (322-13*sqrt(70))/900),
       ( sqrt(5+2*sqrt(10/7))/3, (322-13*sqrt(70))/900), 
       ( 0,                      128/225)]
          ]
for i in range(len(gq)):
  gq[i].sort(key=lambda x : x[0])

def gaussian_quadrature(f, a, b, n=5):
  '''
  Parameters
  ----------
  f : function
  a : number : start
  b : number : stop
  n : int   

  Returns
  -------  
  float
  '''
  g = lambda t : ((b-a)*t+b+a)/2
  return sum(w*f(g(p)) for (p,w) in gq[n]) * (b-a)/2

if __name__ == '__main__':
  from math import sin
  f = lambda x : x*sin(x)
  print(gaussian_quadrature(f, 0, 2, 5))

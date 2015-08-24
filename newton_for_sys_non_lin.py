def newton(f, j, x0, eps=1e-5, max_iteration=100):
  """
  Parameters
  ----------
  f  : list of functions
  j  : list of list of functions : Jacobian matrix
  x0 : list of floats            : initial guess
  
  Returns
  -------  
  list of floats
  
  Raises
  ------
  ValueError : if solution doesn't converge
  """
  for __ in range(max_iteration):
    m = [[fn(x0) for fn in j[i]] for i in range(len(j))]
    for i in range(len(f)):
      m[i].append(-f[i](x0))
      
    import gauss
    dx = gauss.gaussian_elimination(m)
    #import gauss_seidel 
    #y = gauss_seidel.gauss_seidel(m, [1,1,1,1])
    
    if all(i < eps for i in dx): 
      return x0
      
    x0 = [x0[i] + dx[i] for i in range(len(dx))]
  raise ValueError('Solution does not converge')

if __name__ == '__main__':
  
  from math import (sin, cos, e)
  
  # problem from aj Montri
  f = [
    lambda x : x[1]**2 - sin(x[0]*x[2]) - 4,
    lambda x : x[0]**3 - 4*(x[1]+x[2])**2 + cos(x[2]) + 2,
    lambda x : e**(x[0]+x[1]) - 5*x[1] + x[2]**2 - 4
  ]
  
  j = [
    [
      lambda x : -x[2]*cos(x[0]*x[2]),
      lambda x : 2*x[1],
      lambda x : -x[0]*cos(x[0]*x[2])
    ],
    [
      lambda x : 3*x[0]**2,
      lambda x : -8*(x[1]+x[2]),
      lambda x : -8*(x[1]+x[2])-sin(x[2])
    ],
    [
      lambda x : e**(x[0]+x[1]),
      lambda x : e**(x[0]+x[1])-5,
      lambda x : 2*x[2]
    ]
  ]
  
  print(newton(f, j, [0, 2, -3]))
  
  
  """
  from math import *
  
  # problem from Burden 7ed
  f = [
    lambda x : 3*x[0] - cos(x[1]*x[2]) - 0.5,
    lambda x : x[0]**2 - 81*(x[1]+0.1)**2 + sin(x[2]) + 1.06,
    lambda x : e**(-x[0]*x[1]) + 20*x[2] + (10*pi-3)/3
  ]
  
  j = [
    [
      lambda x : 3,
      lambda x : x[2]*sin(x[1]*x[2]),
      lambda x : x[1]*sin(x[1]*x[2])
    ],
    [
      lambda x : 2*x[0],
      lambda x : -162*(x[1]+0.1),
      lambda x : cos(x[2])
    ],
    [
      lambda x : -x[1]*e**(-x[0]*x[1]),
      lambda x : -x[0]*e**(-x[0]*x[1]),
      lambda x : 20
    ]
  ]
  
  print(newton(f, j, [0.1, 0.1, -0.1]))
  """

# newton's method for solving system of nonlinear equation
# author : worasait suwannik
# date   : jul 2015

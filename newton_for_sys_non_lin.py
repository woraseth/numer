from gauss import *

def newton_nonlinear(f, j, x0, sys_lin_meth=gaussian_elimination, eps=1e-5, max_iteration=100):
  """
  Parameters
  ----------
  f  : list of functions
  j  : list of list of functions : Jacobian matrix
  x0 : list of floats            : initial guess
  sys_lin_meth : function : solve system of linear equations
  
  Returns
  -------  
  list of floats
  
  Raises
  ------
  ValueError : if solution doesn't converge
  """
  for __ in range(max_iteration):
    # solve for dx
    m = [[fn(x0) for fn in j[i]] for i in range(len(j))]
    for i in range(len(f)):
      m[i].append(-f[i](x0))
    dx = sys_lin_meth(m)
    # update x0
    x0 = [x0[i] + dx[i] for i in range(len(dx))]
    # terminate?
    if all(i < eps for i in dx): 
      return x0
  raise ValueError('Solution does not converge')

if __name__ == '__main__':
  
  f = [lambda x : x[0]**2 + x[1]**2 - 17, 
       lambda x : 2*x[0]**(1/3) + x[1]*0.5 - 4]
  j = [[lambda x : 2*x[0], lambda x : 2*x[1]],
       [lambda x : (2/3)*x[0]**(-2/3), lambda x : 0.5*x[1]**-0.5]]
  x0 = [2, 3]
  x = newton_nonlinear(f, j, x0)
  print('solution is ', x)
  for i in range(len(f)):
    print('f[%d]=%f' % (i, f[i](x)))
  
  
  '''
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
  x0 = [0.1, 0.1, -0.1]
  from gauss_seidel import *
  def my_gs(m, ig=[1, 1, 1]): return gauss_seidel(m, ig)
  x = newton_nonlinear(f, j, x0, my_gs)
  print('solution is ', x)
  for i in range(len(f)):
    print('f[%d]=%f' % (i, f[i](x)))
  '''
  

# newton's method for solving system of nonlinear equation
# author : worasait suwannik
# date   : jul 2015

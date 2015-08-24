def euler_single(fs, x0, y0s, h):
  return [y0s[i] + fs[i](x0, y0s)*h for i in range(len(y0s))]

def runge_kutta_single(f, x0, y0s, h):
  n = len(y0s)
  k1s = [fs[i](x0, y0s)         for i in range(n)]
  yts = [y0s[i] + 0.5*h*k1s[i]  for i in range(n)]
  k2s = [fs[i](x0 + 0.5*h, yts) for i in range(n)]
  yts = [y0s[i] + 0.5*h*k2s[i]  for i in range(n)]
  k3s = [fs[i](x0 + 0.5*h, yts) for i in range(n)]
  yts = [y0s[i] + h*k3s[i]      for i in range(n)]
  k4s = [fs[i](x0 + h, yts)     for i in range(n)]

  return [y0s[i] + (k1s[i] + 2*k2s[i] + 2*k3s[i] + k4s[i])*h/6 for i in range(n)]
    
def sys_ode(fs, x0, y0s, h, x, method=runge_kutta_single):
  """
  Parameters
  ----------
  fs  : list of functions
  x0  : number            :  initial value
  y0s : list of numbers   :  initial value
  h   : number            :  step size
  x   : number
      
  Returns
  -------  
  list of numbers : solutions at x
  """  
  for i in range(int((x-x0)/h)):
    y0s = method(fs, x0, y0s, h) 
    x0 += h
  return y0s

if __name__ == '__main__':
  fs = [
    lambda x, ys : ys[1],
    lambda x, ys : 2*ys[1] - 3*ys[0]
  ]
  ys = sys_ode(fs, 0, [4, 6], 0.5, 2, euler_single)
  print(ys)
  
  #print(sys_ode(fs, 0, [4, 6], 0.5, 2, runge_kutta_single))

# system of ordinary differential equations
# author : worasait suwannik
# date   : jul 2015

"""
  fs = [
    lambda x, ys : -0.5*ys[0],
    lambda x, ys : 4 - 0.3*ys[1] - 0.1*ys[0]
  ]  # aj Montri Maleewong p168
"""

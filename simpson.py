def simpson(fn, a, b, n):
  '''
  f : function
  a : number : start
  b : number : stop
  n : integer : must be even
  '''
  h = (b - a) / n
  sum1 = sum(fn(a + (2*i + 1)*h) for i in range(0, int(n/2)))
  sum2 = sum(fn(a + (2*i + 2)*h) for i in range(0, int(n/2) - 1))
  return (fn(a) + fn(b) + 4*sum1 + 2*sum2) * h / 3;

if __name__ == '__main__':
  from math import cos, pi
  f = lambda x : cos(x)
  a = 0
  b = pi / 2
  n = 20
  print(simpson(f, a, b, n))
  # aj Pramote p283
  #print(simpson(lambda x : 2*x**3 - 5*x**2 + 3*x + 1, 0, 2, 10))  # 2.67
  # aj Pramote p284
  #for n in [2,4,6,8,10,20]:
  #  print(simpson(lambda x : x**4 + 2*x**3 - 5*x**2 + 3*x + 1, 0, 2, n)) # 9.3333, 9.0833, 9.06996, 9.0677, 9.0671, 9.0667

# author: Worasait Suwannik
# date: May 2015


class LagrangeInterpolation:
  def __init__(self,A,x):
    self.A = A
    self.x = x
    #coordinates 
    self.n = len(A[0])
    self.X = self.A[0]
    self.Y = self.A[1]

  def build_matrix(self):
    P = [[0 for i in range(self.n)] for j in range(self.n)]

    # (x-xi) * (x-xj) = (x**2 -x*xj - x*xi + xi*xj)
    # [xi*xj, -x*xj - x*xi, x**2]
    # [[0, -1, 1],[-2,1,1],[0,2,1]]
    #make the equation matrix
    for i in range(self.n):
      P[i][0] = 1 # for the multiply below doesn't zeroed
      divisor = 1 
      for k in range(self.n): #Dividend Product 
        if i != k:
          P[i][0]  *= self.X[k] 
          P[i][1]  += -(self.X[k])
          P[i][2]  = 1
          divisor  *= (self.X[i]- self.X[k]) 
      for k in range(self.n): #Divisor Product
        P[i][k]  = P[i][k]/divisor * self.Y[i]

    #sum variables to get the polinomial equation
    B = [0 for i in range(self.n)]
    for i in range(self.n):
      for j in range(self.n):
        B[i] += P[j][i]
    return B


  def estimate_value(self):
      B = self.build_matrix()
      estimate_value = B[0]
      for i in range(1,len(B)):
        estimate_value += B[i]* self.x**i
      
      return estimate_value
import math

class CholeskyDecomposition:
  def __init__(self,A,B):
  # the sum part could be a function
    self.A = A
    self.B = B
  
  def symetric_matrix(self):
    for i in range(len(self.A)):
      for j in range(len(self.A)):
        if self.A[i][j]!=self.A[j][i]:
          return False
    
    return True
  
  def validates_decomposition(self):
    return self.symetric_matrix()

  def inverse(self,X):
    inverseX = [[0 for i in range(len(X[1]))] for j in range(len(X[0]))]
    for i in range(len(X[0])):
      for j in range(len(X[1])):
        inverseX[j][i] = X[i][j]
    return inverseX

  def decompose(self):
    if not self.validates_decomposition():
      return "Não é possivel fazer a decomposição"
    else:
      for i in range(len(self.A)):
        generic_sum = 0 
        for k in range(0,i):
          generic_sum += (self.A[i][k])**2
        
        self.A[i][i] = math.sqrt(self.A[i][i] - generic_sum)
        for j in range(i+1,len(self.A)):
          generic_sum = 0
          for k in range(0,i):
            generic_sum+= (self.A[i][k] * self.A[j][k])
          self.A[j][i] = (1/self.A[i][i]) * (self.A[i][j] - generic_sum)
      # Turn into a lower triangular matrix
      for i in range(0, len(self.A)):
        for j in range(i+1,len(self.A)):
          self.A[i][j] = 0
      
      return self.A, self.inverse(self.A)
  
  def forward_substitution(self, L):
    n = len(self.B)
    self.Y = [0]*n
    self.Y[0] = self.B[0]/L[0][0]
    
    for i in range(1,n):
      sum = 0
      for j in range(i):
        sum+= L[i][j] * self.Y[j]
      self.Y[i] = (self.B[i]-sum)/L[i][i]
    return self.Y

  def backward_substitution(self,U):
    n = len(self.Y)
    X = [0] * n
    X[n - 1] = self.Y[n - 1]/U[n - 1][n - 1]

    for i in range(n-2,-1,-1):
      sum = 0
      for j in range(i+1,n):
        sum+= U[i][j] * X[j]
      X[i] = (self.Y[i] - sum)/U[i][i]
    
    return X
  
  def solution(self):
    if self.validates_decomposition():
      L,U = self.decompose()
      Y   = self.forward_substitution(L)
      X   = self.backward_substitution(U)
      return X
    else:
      return "Não é possivel fazer a decomposição"
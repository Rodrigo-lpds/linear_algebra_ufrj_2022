import math

class CholeskyDecomposition:
  def __init__(self,A):
  # the sum part could be a function
    self.A = A
  
  def symetric_matrix(self):
    for i in range(len(self.A)):
      for j in range(len(self.A)):
        if self.A[i][j]!=self.A[j][i]:
          return False
    
    return True
  
  def validates_decomposition(self):
    return self.symetric_matrix()

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
      
      return self.A
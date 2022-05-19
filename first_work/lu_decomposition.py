class LU:
  def __init__(self,A,B):
    self.A = A
    self.B = B
  
  def check_matrix_width(self):
    return len(self.A[0]) == len(self.A[1])
  
  def calculate_determinant(self, matrix, mul=1):
    n = len(matrix)
    if n == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        determinant = 0
        for i in range(n):
            m = []
            for j in range(1, n):
                buff = []
                for k in range(n):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            determinant += mul * self.calculate_determinant(m, sign * matrix[0][i])
    return determinant

  def validates_decomposition(self):
    is_square = self.check_matrix_width()
    determinant_ans = self.calculate_determinant(self.A)
    nil_determinant = 0
    
    return is_square and determinant_ans != nil_determinant

  def decompose(self):
    n = len(self.A)
    for k in range(n):
      for i in range(k+1,n):
        self.A[i][k] = self.A[i][k]/self.A[k][k]

      for j in range(k+1,n):
        for i in range(k+1,n):
          self.A[i][j] = self.A[i][j] - self.A[i][k]*self.A[k][j]
    
    #compose L
    L = [[1,0,0],[0,1,0],[0,0,1]]
    for i in range(1,n):
      for j in range(i):
        L[i][j] = self.A[i][j]

    # compose U
    U = [self.A[0],[0,0,0],[0,0,0]]
    for i in range(1,n):
      for j in range(i,n):
        U[i][j] = self.A[i][j]
    return L,U

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
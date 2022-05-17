#to do
# check if lu decomposition can be used
class LU:
  def __init__(self,A,B):
    self.A = A
    self.B = B

  def decompose(self):
    ''' 
      DO K = 1, N-1
        DO I = K+1,N
          A(I,K) = A(I,K)/A(K,K)
        ENDDO
        DO J = K+1,N
          DO I = K+1,N
            A(I,J) = A(I,J)-A(I,K)*A(K,J)
          ENDDO
        ENDDO
      ENDDO
      A(N,N)
    '''
    n = len(self.A)
    for k in range(n):
      for i in range(k+1,n):
        self.A[i][k] = self.A[i][k]/self.A[k][k]

      for j in range(k+1,n):
        for i in range(k+1,n):
          self.A[i][j] = self.A[i][j] - self.A[i][k]*self.A[k][j]

    #print(A)
    
    #compose L
    L = [[1,0,0],[0,1,0],[0,0,1]]
    for i in range(1,n):
      for j in range(i):
        L[i][j] = self.A[i][j]

    #print(L)
    
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
  #    print(Y)
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
    L,U = self.decompose()
    Y   = self.forward_substitution(L)
    X   = self.backward_substitution(U)
    return X
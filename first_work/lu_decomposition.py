def decompose(A):
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
  n = len(A)
  for k in range(n):
    for i in range(k+1,n):
      A[i][k] = A[i][k]/A[k][k]

    for j in range(k+1,n):
      for i in range(k+1,n):
        A[i][j] = A[i][j] - A[i][k]*A[k][j]

  #print(A)
  
  #compose L
  L = [[1,0,0],[0,1,0],[0,0,1]]
  for i in range(1,n):
    for j in range(i):
      L[i][j] = A[i][j]

  #print(L)
  
  # compose U
  U = [A[0],[0,0,0],[0,0,0]]
  for i in range(1,n):
    for j in range(i,n):
      U[i][j] = A[i][j]
  return L,U

def forward_substitution(L,B):
  n = len(B)
  Y = [0]*n
  Y[0] = B[0]/L[0][0]
  
  for i in range(1,n):
    sum = 0
#    print(Y)
    for j in range(i):
      sum+= L[i][j] * Y[j]
    Y[i] = (B[i]-sum)/L[i][i]
  return Y

def backward_substitution(Y,U):
  n = len(Y)
  X = [0] * n
  X[n - 1] = Y[n - 1]/U[n - 1][n - 1]

  for i in range(n-2,-1,-1):
    sum = 0
    for j in range(i+1,n):
      sum+= U[i][j] * X[j]
    X[i] = (Y[i] - sum)/U[i][i]
  
  return X

A = [[1,2,2],[4,4,2],[4,6,4]]
B = [3,6,10]
L,U = decompose(A)
Y = forward_substitution(L,B)

X = backward_substitution(Y,U)
print(X)
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

  print(A)
  
  #compose L
  L = [[1,0,0],[0,1,0],[0,0,1]]
  for i in range(1,n):
    for j in range(i):
      L[i][j] = A[i][j]

  print(L)
  
  # compose U
  U = [A[0],[0,0,0],[0,0,0]]
  for i in range(1,n):
    for j in range(i,n):
      U[i][j] = A[i][j]

  print(U)

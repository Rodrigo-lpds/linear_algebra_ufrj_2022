import math

# the sum part could be a function
A = [[1,0.2,0.4],[0.2,1,0.5],[0.4,0.5,1]]

for i in range(len(A)):
  generic_sum = 0 
  for k in range(0,i):
    generic_sum += (A[i][k])**2
  
  A[i][i] = math.sqrt(A[i][i] - generic_sum)
  for j in range(i+1,len(A)):
    generic_sum = 0
    for k in range(0,i):
      generic_sum+= (A[i][k] * A[j][k])
    A[j][i] = (1/A[i][i]) * (A[i][j] - generic_sum)
# Turn into a lower triangular matrix
for i in range(0, len(A)):
  for j in range(i+1,len(A)):
    A[i][j] = 0

print(A)
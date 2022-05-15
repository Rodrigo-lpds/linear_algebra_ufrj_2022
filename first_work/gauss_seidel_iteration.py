# read Slide 4 for references
#to do 
# check if converges
# calculate normal 
# split sum loops into separate functions
# check if iteration can be done
import math

A = [[3,-1,-1],[-1,3,-1],[-1,-1, 3]]
B = [1,2,1]
X_0 = [1,1,1]
X_1 = [0,0,0]
R = 0

for solutions in range(1):
  for i in range(len(X_0)):
    sum_with_new_X = 0
    sum_with_old_X = 0
    for j in range(i):
      sum_with_new_X += A[i][j] * X_1[j]
    for j in range(i+1,len(A)):
      sum_with_old_X += A[i][j] * X_0[j]

    X_1[i] = (B[i]-sum_with_new_X - sum_with_old_X) / A[i][i]
  #print(solutions)
  #if solutions+1 != 2:
  #  X_0 = X_1

def calculate_normal(X_0,X_1):
  sum_0 = 0
  sum_1 = 0
  for i in range(0,len(X_0)):
    sum_0 += (X_1[i] - X_0[i])**2
    sum_1 += X_1[i] ** 2
  
  return math.sqrt(sum_0)/math.sqrt(sum_1)

print(X_1)
print(calculate_normal(X_0,X_1))


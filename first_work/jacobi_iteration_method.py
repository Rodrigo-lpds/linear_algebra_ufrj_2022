# read Slide 4 for references
#to do 
# check if converges
# calculate normal 
# split sum loops into separate functions
# check if iteration can be done
import math 

class JacobiIterationMethod:
  def __init__(self,n,A,B,TOLm):
    self.n = n
    self.A = A
    self.B = B
    self.TOLm = TOLm
    self.X_0 = [1,1,1]
    self.X_1 = [0,0,0]
    self.R = 0

  def calculate_solutions(self):
    for i in range(len(self.X_0)):
      generic_sum = 0
      for j in range(0,len(self.X_0)):
          if j != i:
            generic_sum += self.A[i][j] * self.X_0[j]
      self.X_1[i] = (self.B[i] - generic_sum) / self.A[i][i]

    return self.X_1


  def calculate_normal(X_0,X_1):
    sum_0 = 0
    sum_1 = 0
    for i in range(0,len(X_0)):
      sum_0 += (X_1[i] - X_0[i])**2
      sum_1 += X_1[i] ** 2
    
    return math.sqrt(sum_0)/math.sqrt(sum_1)
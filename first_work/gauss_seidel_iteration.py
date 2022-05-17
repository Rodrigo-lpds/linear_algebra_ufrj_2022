# read Slide 4 for references
#to do 
# calculate normal based on TOLm
import math

class GaussSeidelIteration:
  def __init__(self,n,A,B,TOLm):
    self.n = n
    self.A = A
    self.B = B
    self.TOLm = TOLm
    self.X_0 = [1,1,1]
    self.X_1 = [0,0,0]
    self.R = 0

  def check_convergence(self):
    #Diagonally dominant matrix
    for i in range(0,len(self.A)):
      for j in range(0,len(self.A)):
        if i!=j and (abs(self.A[i][i]) < abs(self.A[i][j]) or abs(self.A[i][i]) < abs(self.A[j][i])):
          return False
    return True

  def calculate_solutions(self):
    for i in range(len(self.X_0)):
      sum_with_new_X = 0
      sum_with_old_X = 0
      for j in range(i):
        sum_with_new_X += self.A[i][j] * self.X_1[j]
      for j in range(i+1,len(self.A)):
        sum_with_old_X += self.A[i][j] * self.X_0[j]

      self.X_1[i] = (self.B[i]-sum_with_new_X - sum_with_old_X) / self.A[i][i]
    
    return self.X_1
  #print(solutions)
  #if solutions+1 != 2:
  #  X_0 = X_1
  def calculate_normal(self):
    sum_0 = 0
    sum_1 = 0
    for i in range(0,len(self.X_0)):
      sum_0 += (self.X_1[i] - self.X_0[i])**2
      sum_1 += self.X_1[i] ** 2
    
    return math.sqrt(sum_0)/math.sqrt(sum_1)
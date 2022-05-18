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

  def calculate_solution(self,X_0,X_1):
    for i in range(len(X_0)):
      sum_with_new_X = 0
      sum_with_old_X = 0
      for j in range(i):
        sum_with_new_X += self.A[i][j] * X_1[j]
      for j in range(i+1,len(self.A)):
        sum_with_old_X += self.A[i][j] * X_0[j]

      X_1[i] = (self.B[i]-sum_with_new_X - sum_with_old_X) / self.A[i][i]
    
    return X_0,X_1

  def calculate_normal(self,X_0,X_1):
    sum_0 = 0
    sum_1 = 0
    for i in range(0,len(X_0)):
      sum_0 += (X_1[i] - X_0[i])**2
      sum_1 += X_1[i] ** 2
    
    self.R = math.sqrt(sum_0)/math.sqrt(sum_1)
    return self.R
  
  def calculate_solutions(self):
    X_0, X_1 = self.calculate_solution(self.X_0,self.X_1)
    self.calculate_normal(X_0, X_1)
    while self.R > self.TOLm:
      X_0 = X_1
      X_1 = [0,0,0]
      X_0, X_1 = self.calculate_solution(X_0,X_1)
   
      self.calculate_normal(X_0, X_1)
    
    return X_0, X_1, self.R
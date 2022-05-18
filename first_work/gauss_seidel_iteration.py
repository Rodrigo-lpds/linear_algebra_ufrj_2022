import iterations
class GaussSeidelIteration(iterations.Iterations):
  def __init__(self,n,A,B,TOLm):
    super().__init__(n,A,B,TOLm)

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
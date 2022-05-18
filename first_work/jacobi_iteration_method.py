import iterations
class JacobiIterationMethod(iterations.Iterations):
  def __init__(self,n,A,B,TOLm):
    super().__init__(n,A,B,TOLm)

  def calculate_solution(self,X_0,X_1):
    for i in range(len(X_0)):
      generic_sum = 0
      for j in range(0,len(X_0)):
          if j != i:
            generic_sum += self.A[i][j] * X_0[j]
      X_1[i] = (self.B[i] - generic_sum) / self.A[i][i]

    return X_0,X_1
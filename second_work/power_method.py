from re import X
import sys
from unicodedata import decomposition
sys.path.insert(0,"..")

from first_work.lu_decomposition import LU

class PowerMethod:
  def __init__(self,A,TOLm):
    self.A = A
    self.TOLm = TOLm
    self.X_0 = [1.0 for i in range(len(A[0]))]
    self.X_1 = [0 for i in range(len(A[0]))]

#X_1 = [0.0,0,0]
#calculate AX
  def calculateAx(self,X_0,X_1):
    for i in range(len(self.A[0])):
      for j in range(len(self.A[1])):
        X_1[i]+= self.A[i][j] * X_0[i]

    return X_1
  
  def find_lambda(self,X_0,X_1):
    # find factor
    lamb = X_1[0]/X_0[0]
    X_1 = [element/lamb for element in X_1] 
    
    return lamb,X_1

  # calculate R
  def calculate_R(self,lamb,old_lamb):
    R = (lamb - old_lamb)/lamb
    
    return R

  def calculate_solutions(self):
    X_1     = self.calculateAx(self.X_0,self.X_1)
    old_lamb    = 1
    lamb,X_1    = self.find_lambda(self.X_0,X_1)
    R           = self.calculate_R(lamb,old_lamb)

    while R > self.TOLm:
      X_0 = X_1
      X_1 = [0 for i in range(len(self.A[0]))]
      old_lamb    = lamb
      X_1         = self.calculateAx(X_0,X_1)
      lamb,X_1    = self.find_lambda(X_0,X_1)
      R = self.calculate_R(lamb,old_lamb)
    return X_1,lamb

  def calculate_auto_vector (self):
    B = [0 for i in range(len(self.A[0]))]
    lambdas = [0 for i in range(len(self.A[0]))]
    X_1,lamb = self.calculate_solutions()
    print(X_1)
    for i in range(len(self.A[0])):
      for j in range(len(self.A[1])):
        B[i]+= self.A[i][j] * X_1[i]
    print(B)

    for i in range(len(X_1)):
      lambdas[i] = B[i]/X_1[i]
    
    return lambdas

#X_1  é o autovetor
#Ax = lambdaX
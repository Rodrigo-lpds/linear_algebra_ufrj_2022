#PTPB=PTY
import sys
from unicodedata import decomposition
sys.path.insert(0,"..")

from first_work.lu_decomposition import LU

class MultilinearRegression:
  def __init__(self,A,n,x):
    self.A = A
    self.x = x
    #coordinates 
    self.n = n
    self.X = self.A[0]
    self.Y = self.A[1]

  def build_matrix(self):
    P = [[0 for i in range(self.n)] for j in range(self.n)]

    for i in range(self.n):
      for j in range(self.n):
        P[i][j] = self.X[i]**j

    decomposition = LU(P, self.Y)
    return decomposition.solution()
  
  def estimate_value(self):
    B = self.build_matrix()
    estimate_value = B[0]
    for i in range(1,len(B)):
      estimate_value += B[i]* self.x**i
    
    return estimate_value
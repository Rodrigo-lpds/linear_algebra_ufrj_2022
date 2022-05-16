#PTPB=PTY
import sys
from unicodedata import decomposition
sys.path.insert(0,"..")

from first_work.lu_decomposition import LU
#coordinates 
X = [-2,0,1]
Y = [-27,-1,0]
n = 3
P = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
  for j in range(n):
    P[i][j] = X[i]**j

decomposition = LU(P, Y)
B = decomposition.solution()
print(B)
#PTPB=PTY
import sys
from unicodedata import decomposition
sys.path.insert(0,"..")

from first_work.lu_decomposition import LU
#coordinates 
X = [1,2.5,4]
Y = [2,3.5,8]
n = 3
P = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
  for j in range(n):
    P[i][j] = X[i]**j

decomposition = LU(P, Y)
B = decomposition.solution()
print(B)

x = 3.25
estimate_value = B[0]
for i in range(1,len(B)):
  estimate_value += B[i]* x**i
print(estimate_value)
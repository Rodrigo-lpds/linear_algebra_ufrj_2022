from lu_decomposition import LU
from cholesky_decomposition import CholeskyDecomposition

A = [[1,0.2,0.4],[0.2,1,0.5],[0.4,0.5,1]]
cd = CholeskyDecomposition(A)
print(cd.decompose())
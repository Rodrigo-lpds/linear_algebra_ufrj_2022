from lu_decomposition import LU
from cholesky_decomposition import CholeskyDecomposition
from gauss_seidel_iteration import GaussSeidelIteration
from jacobi_iteration_method import JacobiIterationMethod

A = [[1,2,2],[4,4,2],[4,6,4]]
B = [3,6,10]
obj = LU(A,B)
print(obj.solution())

A = [[1,0.2,0.4],[0.2,1,0.5],[0.4,0.5,1]]
cd = CholeskyDecomposition(A)
print(cd.decompose())

A = [[3,-1,-1],[-1,3,-1],[-1,-1, 3]]
B = [1,2,1]
gc = GaussSeidelIteration(3,A,B,0)
print(gc.calculate_solutions())

A = [[3,-1,-1],[-1,3,-1],[-1,-1, 3]]
B = [1,2,1]

ji = JacobiIterationMethod(3,A,B,0)
print(ji.calculate_solutions())

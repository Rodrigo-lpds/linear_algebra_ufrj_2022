#import OS
import os
from lu_decomposition import LU
from cholesky_decomposition import CholeskyDecomposition
from jacobi_iteration_method import JacobiIterationMethod
from gauss_seidel_iteration import GaussSeidelIteration
from read_dat_file import ReadDatFile

dat_files = []
for x in os.listdir():
  if x.endswith(".dat") and x.startswith("EXEMPLO"):
    dat_files.append(x)

for file in dat_files:
  dat_file  = ReadDatFile(file)
  data      = dat_file.read_file()

  ICOD  = dat_file.get_ICOD(data)
  N     = dat_file.get_N(data)
  A     = dat_file.get_matrix_A(data)
  B     = dat_file.get_matrix_B(data)
  TOLm  = dat_file.get_TOLm(data)

  if ICOD == "1":
    obj = LU(A,B)
    f = open("saida_lu.dat", "a")
    f.write("Matriz A = ")
    f.write(str(A)+"\n")
    f.write("Matriz B = ")
    f.write(str(B)+"\n")
    f.write("solucao = ")
    f.write(str(obj.solution())+"\n")
    f.close()
  elif ICOD == "2":
    obj = CholeskyDecomposition(A,B)
    f = open("saida_cholesky.dat", "a")
    f.write("Matriz A = ")
    f.write(str(A)+"\n")
    f.write("Matriz B = ")
    f.write(str(B)+"\n")
    f.write("solucao = ")
    f.write(str(obj.solution())+"\n")
    f.close()

  elif ICOD == "3":
    obj = GaussSeidelIteration(N,A,B,TOLm)
    f = open("saida_gaus.dat", "a")
    f.write("Matriz A = ")
    f.write(str(A)+"\n")
    f.write("Matriz B = ")
    f.write(str(B)+"\n")
    f.write("solucao = ")
    f.write(str(obj.calculate_solutions())+"\n")
    f.close()
  elif ICOD == "4":
    obj = JacobiIterationMethod(N,A,B,TOLm)
    f = open("saida_jacobi.dat", "a")
    f.write("Matriz A = ")
    f.write(str(A)+"\n")
    f.write("Matriz B = ")
    f.write(str(B)+"\n")
    f.write("solucao = ")
    f.write(str(obj.calculate_solutions())+"\n")
    f.close()
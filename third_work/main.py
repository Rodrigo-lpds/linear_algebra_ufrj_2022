from re import X
from multilinear_regression import MultilinearRegression
from lagrange_interpolation import LagrangeInterpolation
from read_dat_file import ReadDatFile

file  = ReadDatFile("EXEMPLO_01.dat")
data  = file.read_file()
ICOD  = file.get_ICOD(data)
N     = file.get_N(data)
A     = file.get_points(data)
X     = file.get_X(data)

if ICOD == "1":
 lagrange = LagrangeInterpolation(A, N, X)
 print(lagrange.estimate_value())
elif ICOD == "2":
  multi = MultilinearRegression(A, N, X)
  print(multi.estimate_value())




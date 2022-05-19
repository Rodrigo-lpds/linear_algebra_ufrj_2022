import os
from multilinear_regression import MultilinearRegression
from lagrange_interpolation import LagrangeInterpolation
from read_dat_file import ReadDatFile

dat_files = []
for x in os.listdir():
  if x.endswith(".dat") and x.startswith("EXEMPLO"):
    dat_files.append(x)

for file in dat_files:
  dat_file  = ReadDatFile(file)
  data  = dat_file.read_file()

  ICOD  = dat_file.get_ICOD(data)
  N     = dat_file.get_N(data)
  A     = dat_file.get_points(data)
  X     = dat_file.get_X(data)

  if ICOD == "1":
    obj = LagrangeInterpolation(A, N, X)
    f = open("saida_lagrange.dat", "a")
    f.write("Pontos = ")
    f.write(str(A)+"\n")
    f.write("X a ser estimado = ")
    f.write(str(X)+"\n")
    f.write("y estimado = ")
    f.write(str(obj.estimate_value())+"\n")
    f.close()
  elif ICOD == "2":
    obj = MultilinearRegression(A, N, X)
    f = open("saida_multilinear_regression.dat", "a")
    f.write("Pontos = ")
    f.write(str(A)+"\n")
    f.write("X a ser estimado = ")
    f.write(str(X)+"\n")
    f.write("Y estimado = ")
    f.write(str(obj.estimate_value())+"\n")
    f.close()

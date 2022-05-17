from multilinear_regression import MultilinearRegression
from lagrange_interpolation import LagrangeInterpolation

ICOD = input("Digite 1 para escolher interpolacao de lagrange ou 2 para regressao multilinear  ")
print(ICOD)

#coordinates = input("Coordinates")

A = [[1,2.5,4],[2,3.5,8]]

x = input("Digite a coordenada x para ser estimada  ")

if ICOD == "1":
  lagrange = LagrangeInterpolation(A, float(x))
  print(lagrange.estimate_value())
elif ICOD == "2":
  multi = MultilinearRegression(A, float(x))
  print(multi.estimate_value())




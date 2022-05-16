#coordinates 
X = [1,2.5,4]
Y = [2,3.5,8]
n = 3
P = [[0 for i in range(n)] for j in range(n)]

# (x-xi) * (x-xj) = (x**2 -x*xj - x*xi + xi*xj)
# [xi*xj, -x*xj - x*xi, x**2]
# [[0, -1, 1],[-2,1,1],[0,2,1]]
#make the equation matrix
for i in range(n):
  P[i][0] = 1 # for the multiply below doesn't zeroed
  divisor = 1 
  for k in range(n): #Dividend Product 
    if i != k:
      P[i][0]  *= X[k] 
      P[i][1]  += -(X[k])
      P[i][2]  = 1
      divisor  *= (X[i]- X[k]) 
  for k in range(n): #Divisor Product
    P[i][k]  = P[i][k]/divisor * Y[i]

#sum variables to get the polinomial equation
B = [0 for i in range(n)]
for i in range(n):
  for j in range(n):
    B[i] += P[j][i]

print (B)
x = 3.25
estimate_value = B[0]
for i in range(1,len(B)):
  estimate_value += B[i]* x**i
#print(B[0] + B[1]*3.25 + B[2] * 3.25**2)
print (estimate_value)
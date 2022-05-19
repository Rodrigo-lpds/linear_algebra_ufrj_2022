from power_method import PowerMethod

A    = [[1.0,0.2,0],[0.2,1.0,0.5],[0.0,0.5,1.0]]
TOLm = 0.0066
pw = PowerMethod(A,TOLm)
print(pw.calculate_auto_vector())

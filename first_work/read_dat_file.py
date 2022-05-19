class ReadDatFile:
  def __init__(self,dat_file):
    self.dat_file = dat_file
    self.commands = []

  def read_file(self):
    with open(self.dat_file, 'r') as datFile:
        data = [data.strip('\n') for data in datFile if not(data.startswith("#"))]
    return data

  def get_ICOD(self,data):
    return data[0]
  
  def get_N(self,data):
    return int(data[1])

  def get_matrix_A(self,data):
    N = self.get_N(data)
    rows = data[2:2+N:]
    A = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
      for j in range(N):
        A[i][j] = float(rows[i].split(' ')[j])
    
    return A
  
  def get_matrix_B(self,data):
    N = self.get_N(data)
    rows = data[2+N:2+2*N:]
    B = [0 for i in range(N)]
    for i in range(N):
      B[i] = float(rows[i])
    
    return B  

  
  def get_TOLm(self,data):
    return float(data[-1])
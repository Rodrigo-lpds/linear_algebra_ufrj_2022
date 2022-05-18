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
  
  def get_points(self,data):
    points = data[2:-1:]
    X = [float(point.split(' ')[0]) for point in points]
    Y = [float(point.split(' ')[1]) for point in points]
    A = [X,Y]
    return A

  def get_X(self,data):
    return float(data[-1])
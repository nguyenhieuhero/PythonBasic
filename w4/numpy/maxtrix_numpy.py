import numpy as np

def getMatrixFromInput(row, col, maxtrix_name):
  _mat = []
  print(f"_____Nhap du lieu cho ma tran {maxtrix_name}_________")
  for i in range(row):
    temp = []
    for j in range(col):
      temp.append(int(input(f"Nhap phan tu hang {i} cot {j}: ")))
    _mat.append(temp)
  return np.array(_mat)

row = int(input("Nhap so hang cua ma tran: "))
col = int(input("Nhap so cot cua ma tran: "))
matA = getMatrixFromInput(row,col,"A")
matB = getMatrixFromInput(row,col,"B")

mul = np.dot(matA,matB)
print(f"Tich 2 ma tran la {mul}")

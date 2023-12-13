inp = int(input("Nhap so N: "))
pascalTriangle = []
for height in range(inp):
  temp = []
  for index in range(height+1):
    try:
      if index > 0:
        temp.append(pascalTriangle[height-1][index-1]+pascalTriangle[height-1][index])
      else:
        temp.append(1)
    except:
      temp.append(1)
  pascalTriangle.append(temp)

print(pascalTriangle)
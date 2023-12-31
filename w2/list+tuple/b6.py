n = int(input("Nhap so n: "))
fiboList=[0,1]
while True:
  temp = fiboList[-1] + fiboList[-2]
  if temp > n:
    break
  fiboList.append(temp)

print(fiboList)
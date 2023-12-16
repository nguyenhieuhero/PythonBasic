a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
while (b==0):
  print("B phai khac 0!")
  b = int(input("Nhap so b: "))

print(f"Can bac {b} cua a la {pow(a,1/b)}")
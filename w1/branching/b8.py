a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))
c = float(input("Nhap so c: "))

list = [a,b,c]
list.sort(reverse=True)
if list[0] == list[1]:
  print(list[2])
else:
  print(list[0])
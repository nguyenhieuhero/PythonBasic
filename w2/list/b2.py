inputString = input("Nhap chuoi nhi phan cach nhau boi dau ',': ").split(",")
for binString in inputString:
  print(int(binString,base=2))
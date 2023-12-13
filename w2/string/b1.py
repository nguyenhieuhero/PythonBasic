inputString = input("Nhap chuoi can xu ly: ")
while inputString[:-4:-1] != "!!!":
  inputString = inputString + "!"

print("Chuoi sau khi xu ly la: %s" %(inputString))
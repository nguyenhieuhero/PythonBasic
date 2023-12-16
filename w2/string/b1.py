inputString = input("Nhap chuoi can xu ly: ")
while inputString.endswith("!"):
  inputString = inputString[:len(inputString)-1]
inputString = inputString + "!!!"
print("Chuoi sau khi xu ly la: %s" %(inputString))
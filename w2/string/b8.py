inputString = input("Nhap chuoi: ")
for number in range(10):
  inputString = inputString.replace(str(number),"?")

print(inputString)
inputString = input("Nhap chuoi: ")
newString = ""
for char in inputString:
  if char.isdigit():
    continue
  newString = newString + char
    

print(newString)

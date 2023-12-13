inputStringArr = input("Nhap chuoi: ").split(" ")
maxStringLen = 0
for string in inputStringArr:
  if maxStringLen < len(string):
    maxStringLen = len(string)

for string in inputStringArr:
  if maxStringLen == len(string):
    print(string)
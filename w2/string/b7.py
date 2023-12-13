inputString = input("Nhap chu so va so luong so can loai bo: ").split(" ")
target = [int(chr) for chr in inputString[0]]
numberToRemove = int(inputString[1])
#Loai bo cac so be nhat tu trai sang phai
for i in range(10):
  for index in range(0,len(target)):
    if target[index] == i:
      target[index] = ''
      numberToRemove -= 1
    if numberToRemove == 0:
      break
fixed = "".join([str(x) for x in target])
print(fixed)
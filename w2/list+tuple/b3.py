inp = int(input("Nhap so: "))
for number in range(1,inp):
  temp = 0
  for num in range(1,number):
    if number%num == 0:
      temp += num
  if temp > number:
    print(number)
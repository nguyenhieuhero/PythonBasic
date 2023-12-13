inputString = input("Nhap chuoi: ")
flag = True
for index in range(0,int(len(inputString)/2)):
  if inputString[index] != inputString[-index-1]:
    flag=False

if flag:
  print("Day la chuoi doi xung")
else:
  print("Day khong phai la chuoi doi xung")
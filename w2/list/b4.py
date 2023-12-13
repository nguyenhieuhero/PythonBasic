import re
inputString = input("Nhap chuoi: ")
emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
if re.fullmatch(emailRegex,inputString):
  print("Email hop le")
else:
  print("Email khong hop le")
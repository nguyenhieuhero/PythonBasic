inputString = input("Nhap chuoi: ").replace(' ','')
dict = {}
for char in inputString:
  if char in dict:
    dict[char] += 1
  else:
    dict[char] = 1
for key in dict:
  print(f"Chu cai {key} xuat hien {dict[key]} lan")
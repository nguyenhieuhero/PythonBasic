def main():
  numberList: list[int] = []
  while(1):
    number = int(input("Nhap so: "))
    if number <= 0:
      break
    else:
      numberList.append(number)
  print(numberList)

main()
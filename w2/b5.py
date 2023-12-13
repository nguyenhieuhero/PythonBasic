def main():
  numberArr = []
  while True:
    inp = int(input("Nhap so: "))
    if inp == 0:
      break
    numberArr.append(inp)
  print(f"So luong so da nhap la {len(numberArr)}")
  if len(numberArr) == 0:
    print("Khong co so de xet")
    return
  smallestNumber = numberArr[0]
  largestNumber = numberArr[0]
  for num in numberArr:
    if smallestNumber > num:
      smallestNumber = num
    if largestNumber < num:
      largestNumber = num
  print(f"So lon nhat {largestNumber}, so nho nhat {smallestNumber}")

if __name__ == '__main__':
  main()
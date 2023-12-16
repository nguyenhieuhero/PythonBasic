def GCD(a: int, b: int) -> int:
  if(b==0): return a
  else:
    return GCD(b,a%b)


def LCM(a: int, b: int) -> int:
  return a*b/GCD(a,b)

def main():
  numberArr = []
  while True:
    inp = int(input("Nhap so: "))
    if inp <= 0:
      break
    numberArr.append(inp)
  if len(numberArr) < 2:
    print("Invalid")
  else:
    GCDHolder = numberArr[0]
    LCMHolder = numberArr[0]
    for index in range(1,len(numberArr)):
      GCDHolder = GCD(GCDHolder,numberArr[index])
      LCMHolder = LCM(LCMHolder,numberArr[index])
    print(GCDHolder,LCMHolder)
if __name__ == '__main__':
  main()
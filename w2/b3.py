def GCD(a: int, b: int) -> int:
  if(b==0): return a
  else:
    return GCD(b,a%b)


def LCM(a: int, b: int) -> int:
  return a*b/GCD(a,b)

print(GCD(10,16))
print(LCM(10,16))
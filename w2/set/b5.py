N = int(input("Nhap so nguyen N: "))
_set = set()
for x in range (1,N+1):
  if N%x == 0:
    _set.add(x)
print(f"Uoc cua N la :{_set}")
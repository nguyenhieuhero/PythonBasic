A = int(input("Nhap so nguyen A: "))
B = int(input("Nhap so nguyen B: "))
_set = set()
for x in range (1,A+1 if A<B else B+1):
  if A % x == 0 and B % x == 0:
    _set.add(x)
print(f"Uoc chung cua A va B la :{_set}")
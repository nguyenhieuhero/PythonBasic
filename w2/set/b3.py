_set = {int(x) for x in input("Nhap day so: ").split(" ")}
max_value = list(_set)[0]
min_value = max_value
for x in _set:
  if max_value < x:
    max_value = x
  if min_value > x:
    min_value = x

print(f"So phan tu cua tap la {len(_set)}")
print(f"max = {max_value}, min = {min_value}")
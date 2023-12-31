def is_prime(number: int) -> bool:
  if(number <= 1):
    return False
  for num in range(2, number):
    if number % num == 0:
      return False
  return True
maxNumber = 1000000
_list = []
for number in range(maxNumber):
  if is_prime(number):
    _list.append(number)
_tuple=tuple(_list)
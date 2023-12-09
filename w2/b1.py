def is_prime(number: int) -> bool:
  if(number <= 1):
    return False
  for num in range(2, number):
    if number % num == 0:
      return False
  return True

print(is_prime(6))
print(is_prime(17))
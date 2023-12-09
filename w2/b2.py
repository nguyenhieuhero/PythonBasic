def is_prime(number: int) -> bool:
  if(number <= 1):
    return False
  for num in range(2, number):
    if number % num == 0:
      return False
  return True

def printPrimesBetweenTwoNumber(a: int, b: int) -> list[int]:
  listPrimes = []
  for num in range(a,b+1):
    if is_prime(num):
      listPrimes.append(num)
  return listPrimes

print(printPrimesBetweenTwoNumber(0,7))
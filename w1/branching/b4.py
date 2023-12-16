def total(num: int)->int:
  sumOfDigitFromNumber = 0
  for digit in str(num):
    sumOfDigitFromNumber += int(digit)
  return sumOfDigitFromNumber

print(total(124))
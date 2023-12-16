def isFibo(number: int) -> bool:
  if number == 0  or number == 1:
    return True
  fiboList = [0,1]
  while fiboList[-1] < number:
    fiboList.append(fiboList[-1] + fiboList[-2])
    if fiboList[-1] == number:
      return True
  return False

print(isFibo(46368)) # True
print(isFibo(4))  #False
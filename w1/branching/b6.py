def calculateFunction(N: int) -> int:
  sum = 0
  temp = 1
  for index in range(1,N+1):
    temp = temp * index
    sum += temp
  return sum

print(calculateFunction(5))
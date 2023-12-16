def average(*nums: int) -> float:
  avg: float = 0
  size: int = 0
  for num in nums:
    size += 1
    avg += num
  return avg/size

print(average(1,2,3,4,5))
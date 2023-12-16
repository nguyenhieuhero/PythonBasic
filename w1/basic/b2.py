import math
def moneyCalculator(money = 10000000, profit_per_year = 0.051, year = 10):
  return money * pow((1 + profit_per_year),10)

print(moneyCalculator())

def yearCalculate(money = 10000000, target = 50000000, profit_per_year = 0.051):
  return math.ceil(math.log(target/money,(1+profit_per_year)))

print(yearCalculate())



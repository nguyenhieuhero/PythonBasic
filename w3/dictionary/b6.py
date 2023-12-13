import random
_rain = { month: [random.randint(100,400) for _i in range(20)] for month in range(1,13)}
print(_rain)
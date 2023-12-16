def area(side1: float, side2: float, side3: float) -> float:
  if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
    raise "Invalide triangle"
  else:
    #using Heron formula
    p = (side1 + side2 + side3)/2
    return pow(p*(p-side1)*(p-side2)*(p-side3),1/2)

print(area(3,4,5))
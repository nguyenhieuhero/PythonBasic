class Point2D:
  def __init__(self,x,y) -> None:
    self.x = x
    self.y = y

def distanceBetween2Point(point1: Point2D, point2: Point2D) -> float:
  return pow((point1.x - point2.x)**2 + (point1.y - point2.y)**2, 1/2)

def area2(point1: Point2D, point2: Point2D, point3: Point2D) -> float:
  side1 = distanceBetween2Point(point1,point2)
  side2 = distanceBetween2Point(point1,point3)
  side3 = distanceBetween2Point(point2,point3)
  if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
    raise "Invalide triangle"
  else:
    #using Heron formula
    p = (side1 + side2 + side3)/2
    return pow(p*(p-side1)*(p-side2)*(p-side3),1/2)


point1 = Point2D(0,3)
point2 = Point2D(4,0)
point3 = Point2D(0,0)


print(area2(point1,point2,point3))
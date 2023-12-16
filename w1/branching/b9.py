dd = int(input("Nhap ngay: "))
mm = int(input("Nhap thang: "))
yy = int(input("Nhap nam: "))

isLeapYear = (yy%4 == 0 and yy%100 != 0) or yy%400 == 0
daysInFeb = 29 if isLeapYear else 28
daysInMonth = {
  1:31,
  2: daysInFeb,
  3: 31,
  4: 30,
  5: 31,
  6: 30,
  7: 31,
  8: 31,
  9: 30,
  10: 31,
  11: 30,
  12: 31,
}

if mm > 12 or dd > daysInMonth[mm]:
  print("Ngay khong ton tai!")
else:
  if dd == daysInMonth[mm]:
    dd = 0
    mm += 1
  if mm > 12:
    mm = 1
    yy += 1
  print(f"Ngay tiep theo la ngay {dd+1}/{mm}/{yy}")
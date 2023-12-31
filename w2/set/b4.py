_set = set()
while(True):
  studentName = input("Nhap ten sinh vien: ")
  if studentName == "":
    break
  _set.add(studentName)

print(_set)

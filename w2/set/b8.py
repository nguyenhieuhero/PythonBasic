_size = int(input("Nhao so luong nguoi tham gia: "))
_arr = []
for x in range(_size):
  _attendee_set = {int(x) for x in input(f"Nhap bo 6 so cua nguoi choi thu {x}: ").split(" ")}
  _arr.append(_attendee_set)

winner_set = {int(x) for x in input("Nhap bo 6 so chien thang: ").split(" ")}
for _attendee_set in _arr:
  if len(_attendee_set & winner_set) >= 5:
    print(f"Bo so cua nguoi thang cuoc la {_attendee_set}")
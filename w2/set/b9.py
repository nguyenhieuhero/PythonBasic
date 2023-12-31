nhan_su=set()
hanh_chinh=set()
truyen_thong=set()

def handle_input():
  employee_ids = {int(x) for x in input("Nhap ma nhan vien: ").split(" ")}
  return employee_ids

while(True):
  print("________Chuong trinh quan ly nhan vien_______")
  print("0. Xem ma nhan vien moi phong")
  print("1. Nhap danh sach ma nhan vien phong nhan su")
  print("2. Nhap danh sach ma nhan vien phong hanh chinh")
  print("3. Nhap danh sach ma nhan vien phong truyen thong")
  print("4. Danh sach nhan vien thuoc ca 3 phong")
  print("5. Danh sach nhan vien chi thuoc 1 phong")
  print("6. Cap phong dung chung nhieu nhan vien nhat")
  print("7. Ma nhan vien nho nhat cua tung phong")
  print("Khac. Thoat chuong trinh!")
  _case = int(input("Nhap lua chon cua ban: "))
  match _case:
    case 0:
      print(f"Ma nhan vien phong nhan su {nhan_su}")
      print(f"Ma nhan vien phong nhan su {hanh_chinh}")
      print(f"Ma nhan vien phong nhan su {truyen_thong}")
      continue
    case 1:
      nhan_su = handle_input()
      continue
    case 2:
      hanh_chinh = handle_input()
      continue
    case 3:
      truyen_thong = handle_input()
      continue
    case 10:
      break
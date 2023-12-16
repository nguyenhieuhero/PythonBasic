def validateStudentByScore(score: float) -> str:
  if score >= 9:
    return "Xuat sac"
  if score >= 8:
    return "Gioi"
  if score >= 6.5:
    return "Kha"
  if score >= 5:
    return "Trung binh"
  if score >= 3.5:
    return "Yeu"
  return "Kem"

print(validateStudentByScore(6.5))
print(validateStudentByScore(8))
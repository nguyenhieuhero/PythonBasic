A = {"one":1,"three":3,"four":4,"five":5}
B = {"two":2,"three":3,"five":5}
C = {}
for keyA in A:
  C[keyA] = A[keyA]
  for keyB in B:
    C[keyB] = B[keyB]
    if keyB in A:
      C[keyA] = A[keyA] + B[keyB]

print(C)

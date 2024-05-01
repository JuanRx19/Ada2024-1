
def conflict(r, c, x):
  cTemp = 0
  rTemp = 0
  flag = True
  while(flag and cTemp < 9):
    #print(cTemp)
    if(A[r][cTemp]  == x):
      flag = False
    cTemp += 1

  while(flag and rTemp < 9):
    if(A[rTemp][c] == x):
      flag = False
    rTemp += 1

  cTemp = (c // 3) * 3
  rTemp = (r // 3) * 3
  r = rTemp
  c = cTemp #Esta malo
  while(flag and rTemp < r + 3):
    while(flag and cTemp < c + 3):
      #print(A[rTemp][cTemp])
      if(A[rTemp][cTemp] == x):
        flag = False
      cTemp += 1
    rTemp += 1
  
  return flag

def next(r, c):
  if(c < 8):
    sudoku(r, c + 1)
  elif(c == 8):
    sudoku(r+1, 0)

A = [[0, 0, 0, 2, 7, 0, 0, 5, 0], [3, 9, 0, 0, 0, 8, 0, 0, 7], [5, 0, 4, 0, 6, 0, 0, 0, 1], 
     [0, 6, 7, 0, 2, 0, 0, 0, 5], [0, 0, 5, 7, 9, 0, 0, 6, 0], [0, 0, 1, 5, 0, 0, 0, 2, 0],
     [0, 0, 8, 0, 0, 0, 0, 0, 2], [0, 0, 9, 0, 0, 0, 3, 0, 0], [0, 5, 3, 4, 0, 0, 8, 0, 0]]

def sudoku(r, c):
  ans = None
  if(r == 9):
    ans = True
    for i in A:
      print(i)
  elif(c == 9):
    next(r, c)
  else:
    ans = False
    if(A[r][c] != 0):
      next(r, c)
    else:
      for x in range(1, 10):
        if(conflict(r, c, x)):
          #print(A[r][c], r, c, x)
          A[r][c] = x
          next(r, c)
          A[r][c] = 0

  return ans
      

sudoku(0, 0)

#print(A)
#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

def conflict(A, n, x):
  flag = False
  i = 0
  while i != n and not(flag):
    if(n-i == abs(x - A[i]) or x == A[i]):
      flag = True
    i+=1
  return flag


def solve(A, n, ans):
  if(n == 8):
    ans += 1
    print(A)
  else:
    for x in range(8):
      if(not(conflict(A, n, x))):
        A.append(x)
        ans = solve(A, n + 1, ans)
        A.pop()
  
  return ans

print(solve([], 0, 0))

#n - i = abs(x - y)
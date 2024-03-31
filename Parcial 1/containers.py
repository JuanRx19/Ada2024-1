from sys import stdin

def f(A, n, x, mem):
  ans,key = None,(n, x)
  if key in mem:
    ans = mem[key]
  else:
    if n==0: ans = x==0
    else:
      ans = f(A, n-1, x, mem)
      if (A[n-1]/10)<=x: ans = ans or f(A, n-1, x-(A[n-1]/10), mem)
    mem[key] = ans
  return ans

def solve(A, n, x):
  mem = {}
  while(not(f(A, n, x, mem))):
     x += 1
  return x

def main():
    C = int(stdin.readline())
    while(C != 0):
        calories = int(stdin.readline())
        tam = int(stdin.readline())
        A = list(map(int, input().split()))
        if(sum(A) > calories):
            print(f"{int(solve(A, tam, calories/10) * 10)}")
        else:
            print("NO SOLUTION")
        C-=1

main()
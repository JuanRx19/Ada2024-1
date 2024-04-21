#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

def solve(n, x, stockholders, coalitions, mem):
  ans = None
  if((n, coalitions) in mem):
    ans  = mem[(n, coalitions)]
  else:
    if(n == 0 and coalitions <= 5000):
      ans = float('inf')
    elif(coalitions > 5000):
      ans = coalitions
    elif(n == x):
      ans = solve(n-1, x, stockholders, coalitions, mem)
    else:
      ans = min(solve(n-1, x, stockholders, coalitions + stockholders[n-1], mem), solve(n-1, x, stockholders, coalitions, mem))
    mem[(n, coalitions)] = ans
  
  return ans
  
def main():
  n, x = map(int, stdin.readline().split())
  while(n != 0 and x != 0):
    stockholders = []
    mem = dict()
    for _ in range(n):
      num = stdin.readline().strip()
      if(len(num) == 6):
        stockholders.append(int(num[0:3])* 100 + int(num[4:6]))
      elif(len(num) == 5):
        stockholders.append(int(num[0:2])* 100 + int(num[3:5]))
      else:
        stockholders.append(int(num[0:1])* 100 + int(num[2:4]))

    if(stockholders[x-1] > 5000):
      print("100.00")
    else:
      ans = solve(n, x, stockholders, stockholders[x-1], mem)
      #print(stockholders)
      ans = (stockholders[x-1] / ans) * 100
      print(f"{ans:.2f}")
    n, x = map(int, stdin.readline().split())

main()
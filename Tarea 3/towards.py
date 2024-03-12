from sys import stdin

def solve_tower(tower, row, col, x, n, mem):
  if((0, 0, n) in mem):
    ans = mem[(0, 0, n)]
  else:
    if((row, col, x) in mem):
      ans = mem[(row, col, x)]
    else:
      if(row == 0):
        ans = abs(x)
      else:
        if(row-1 > len(tower)//2):
          ans = min(solve_tower(tower, row-1, col, x + tower[row-1][col], n, mem),
                    solve_tower(tower, row-1, col, x - tower[row-1][col], n, mem),
                    solve_tower(tower, row-1, col+1, x + tower[row-1][col], n, mem),
                    solve_tower(tower, row-1, col+1, x - tower[row-1][col], n, mem))
        else:
          if(col == 0):
            ans = min(solve_tower(tower, row-1, col, x + tower[row-1][col], n, mem),
                      solve_tower(tower, row-1, col, x - tower[row-1][col], n, mem))
          elif(row-1 == col):
            ans = min(solve_tower(tower, row-1, col-1, x + tower[row-1][col], n, mem),
                      solve_tower(tower, row-1, col-1, x - tower[row-1][col], n, mem))
          else:
            ans = min(solve_tower(tower, row-1, col, x + tower[row-1][col], n, mem),
                      solve_tower(tower, row-1, col, x - tower[row-1][col], n, mem),
                      solve_tower(tower, row-1, col-1, x + tower[row-1][col], n, mem),
                      solve_tower(tower, row-1, col-1, x - tower[row-1][col], n, mem))
      mem[(row, col, x)] = ans
  return ans

def solve(tower, C):
  mem = {}
  n = 0
  flag = 0
  while(not(solve_tower(tower, 2*C - 1, 0, 0, n, mem) == n)):
    if(flag == 0):
      flag = 1
      print(mem)
    n+=1
  return n

def main():
  C = int(stdin.readline())
  while(C != 0):
    tower = []
    for _ in range(2*C - 1):
      row = list(map(int, stdin.readline().split()))
      tower.append(row)
    print(solve(tower, C))
    C = int(stdin.readline())

main()
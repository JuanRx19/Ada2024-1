from sys import stdin

def solve(tower, row, col, x, mem):
  if((row, col, x) in mem):
    ans = mem[(row, col, x)]
  else:
    if(row == 0):
      ans = abs(x)
    else:
      if(row-1 > len(tower)//2):
        ans = min(solve(tower, row-1, col, x + tower[row-1][col], mem),
                  solve(tower, row-1, col, x - tower[row-1][col], mem),
                  solve(tower, row-1, col+1, x + tower[row-1][col], mem),
                  solve(tower, row-1, col+1, x - tower[row-1][col], mem))
      else:
        if(col == 0):
          ans = min(solve(tower, row-1, col, x + tower[row-1][col], mem),
                    solve(tower, row-1, col, x - tower[row-1][col], mem))
        elif(row-1 == col):
          ans = min(solve(tower, row-1, col-1, x + tower[row-1][col], mem),
                    solve(tower, row-1, col-1, x - tower[row-1][col], mem))
        else:
          ans = min(solve(tower, row-1, col, x + tower[row-1][col], mem),
                    solve(tower, row-1, col, x - tower[row-1][col], mem),
                    solve(tower, row-1, col-1, x + tower[row-1][col], mem),
                    solve(tower, row-1, col-1, x - tower[row-1][col], mem))
      mem[(row, col, x)] = ans
  return ans

def main():
  C = int(stdin.readline())
  while(C != 0):
    tower = []
    mem = {}
    for _ in range(2*C - 1):
      row = list(map(int, stdin.readline().split()))
      tower.append(row)
    print(solve(tower, 2*C - 1, 0, 0, mem))
    C = int(stdin.readline())

main()
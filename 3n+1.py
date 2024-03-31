from sys import stdin

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
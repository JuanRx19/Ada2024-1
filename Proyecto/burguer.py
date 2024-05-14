#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

def solve(n, l0, l1, mov, intervalo, i, N, lado, mem):
  ans = None
  if((n, l0, l1, mov) in mem):
    ans = mem[(n, l0, l1, mov)]
  else:
    if(n == N << 1 and l0 == N and l1 == N):
      #print(l0, l1, mov, giro)
      ans = mov
    elif(n == N << 1 or l0 > N or l1 > N):
      ans = float('inf')
    else:
      if(n == N and n >= intervalo[i][0] and n <= intervalo[i][1]):
        ans = solve(N << 1, N, N, 1, intervalo, i, N, lado, mem)
      elif(i < len(intervalo) and mov != len(intervalo) and n >= intervalo[i][0] and n <= intervalo[i][1]):
        if(n >= intervalo[i][0] and n < intervalo[i][1] and lado == 0):
          ans = min(solve(n + 1, l0 + 1, l1, mov + 1, intervalo, i, N, 1 - lado, mem), solve(n + 1, l0 + 1, l1, mov, intervalo, i, N, lado, mem))
        elif(n >= intervalo[i][0] and n < intervalo[i][1] and lado == 1):
          ans = min(solve(n + 1, l0, l1 + 1, mov + 1, intervalo, i, N, 1 - lado, mem), solve(n + 1, l0, l1 + 1, mov, intervalo, i, N, lado, mem))
        elif(n == intervalo[i][1] and lado == 0):
          ans = min(solve(n + 1, l0, l1 + 1, mov + 1, intervalo, i + 1, N, 1 - lado, mem), solve(n + 1, l0 + 1, l1, mov, intervalo, i + 1, N, lado, mem))
        elif(n == intervalo[i][1] and lado == 1):
          ans = min(solve(n + 1, l0 + 1, l1, mov + 1, intervalo, i + 1, N, 1 - lado, mem), solve(n + 1, l0, l1 + 1, mov, intervalo, i + 1, N, lado, mem))
      else:
        if(lado == 0):
          ans = solve(n + 1, l0 + 1, l1, mov, intervalo, i, N, lado, mem)
        else:
          ans = solve(n + 1, l0, l1 + 1, mov, intervalo, i, N, lado, mem)
      mem[(n, l0, l1, mov)] = ans
  
  return ans

def main():
  C = int(stdin.readline())
  while(C > 0):
    intervalo = []
    N, K = map(int, stdin.readline().split())
    for _ in range(K):
      l0, l1 = map(int, stdin.readline().split())
      intervalo.append((l0, l1))
    ans = solve(0, 0, 0, 0, intervalo, 0, N, 0, {})
    if(ans != float('inf')):
      print("Perfect burger!")
      print(ans)
    else:
      print("Another bland and poorly cooked burger!")
    C-=1

main()
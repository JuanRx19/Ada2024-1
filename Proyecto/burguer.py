#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

INF = 100005

def convertir(interval, i, j):
  value = (interval[0] + j)
  if((interval[0] + j) != interval[1]):
    j += 1
  else:
    j = 0
    i += 1
  return value, i, j

def solve(l0, l1, mov, intervalo, i, j, N, lado, mem):
  if((l0, l1, mov) in mem):
    ans = mem[(l0, l1, mov)]
  else:
    if(l0 == N):
      if(l1 != N):
        ans = mov + 1
      else:
      #print(l0, l1, mov, i, j, intervalo[i-1])
        ans = mov
    elif(l0 > N or l1 > N):
      #print(data, mov)
      ans = INF
    else:
      if(i != len(intervalo) and mov != len(intervalo)):
        value, i, j = convertir(intervalo[i], i, j)
        if(lado == 0):
          ans = min(solve(l0 + abs(value - l1 - l0), l1, mov + 1, intervalo, i, j, N, 1 - lado, mem), solve(l0 + abs(value - l1 - l0), l1, mov, intervalo, i, j, N, lado, mem))
        else:
          ans = min(solve(l0, l1 + abs(value - l1 - l0), mov + 1, intervalo, i, j, N, 1 - lado, mem), solve(l0, l1 + abs(value - l1 - l0), mov, intervalo, i, j, N, lado, mem))
      else:
        if(lado == 0):
          ans = solve(l0 + abs(2 * N - l0 - l1), l1, mov, intervalo, len(intervalo), j, N, lado, mem)
        else:
          ans = solve(l0, l1 + abs(2 * N - l1 - l0), mov, intervalo, len(intervalo), j, N, lado, mem)
    mem[(l0, l1, mov)] = ans
  
  return ans

def main():
  C = int(stdin.readline())
  while(C > 0):
    intervalo = []
    N, K = map(int, stdin.readline().split())
    for _ in range(K):
      l0, l1 = map(int, stdin.readline().split())
      intervalo.append((l0, l1))
    ans = solve(0, 0, 0, intervalo, 0, 0, N, 0, {})
    if(ans != INF):
      print("Perfect burger!")
      print(ans)
    else:
      print("Another bland and poorly cooked burger!")
    C-=1

main()
"""def solve(n, l0, l1, mov, intervalo, i, N, lado):
  ans = None
  if(n == N << 1 and l0 == N and l1 == N):
    #print(l0, l1, mov, giro)
    ans = mov
  elif(n == N << 1 or l0 > N or l1 > N):
    ans = float('inf')
  else:
    if(i < len(intervalo) and mov != len(intervalo) and n >= intervalo[i][0] and n <= intervalo[i][1]):
      if(n >= intervalo[i][0] and n < intervalo[i][1] and lado == 0):
        ans = min(solve(n + 1, l0 + 1, l1, mov + 1, intervalo, i, N, 1 - lado), solve(n + 1, l0 + 1, l1, mov, intervalo, i, N, lado))
      elif(n >= intervalo[i][0] and n < intervalo[i][1] and lado == 1):
        ans = min(solve(n + 1, l0, l1 + 1, mov + 1, intervalo, i, N, 1 - lado), solve(n + 1, l0, l1 + 1, mov, intervalo, i, N, lado))
      elif(n == intervalo[i][1] and lado == 0):
        ans = min(solve(n + 1, l0, l1 + 1, mov + 1, intervalo, i + 1, N, 1 - lado), solve(n + 1, l0 + 1, l1, mov, intervalo, i + 1, N, lado))
      elif(n == intervalo[i][1] and lado == 1):
        ans = min(solve(n + 1, l0 + 1, l1, mov + 1, intervalo, i + 1, N, 1 - lado), solve(n + 1, l0, l1 + 1, mov, intervalo, i + 1, N, lado))
    else:
      if(lado == 0):
        ans = solve(n + 1, l0 + 1, l1, mov, intervalo, i, N, lado)
      else:
        ans = solve(n + 1, l0, l1 + 1, mov, intervalo, i, N, lado)
  
  return ans"""

"""def solve(n, l0, l1, mov, intervalo, i, N, lado, mem):
  ans = None
  if((n, l0, l1, mov) in mem):
    print((n, l0, l1, mov))
    ans = mem[(n, l0, l1, mov)]
  else:
    if(n == N << 1 and l0 == N and l1 == N):
      #print(l0, l1, mov, giro)
      ans = mov
    elif(n == N << 1 or l0 > N or l1 > N):
      ans = float('inf')
    else:
      if(i < len(intervalo)):
        if(mov != len(intervalo) and n >= intervalo[i][0] and n < intervalo[i][1] and lado == 0):
          ans = min(solve(n + 1, l0 + 1, l1, mov + 1, intervalo, i, N, 1 - lado, mem), solve(n + 1, l0 + 1, l1, mov, intervalo, i, N, lado, mem))
        elif(mov != len(intervalo) and n >= intervalo[i][0] and n < intervalo[i][1] and lado == 1):
          ans = min(solve(n + 1, l0, l1 + 1, mov + 1, intervalo, i, N, 1 - lado, mem), solve(n + 1, l0, l1 + 1, mov, intervalo, i, N, lado, mem))
        elif(mov != len(intervalo) and n == intervalo[i][1] and lado == 0):
          ans = min(solve(n + 1, l0, l1 + 1, mov + 1, intervalo, i + 1, N, 1 - lado, mem), solve(n + 1, l0 + 1, l1, mov, intervalo, i + 1, N, lado, mem))
        elif(mov != len(intervalo) and n == intervalo[i][1] and lado == 1):
          ans = min(solve(n + 1, l0 + 1, l1, mov + 1, intervalo, i + 1, N, 1 - lado, mem), solve(n + 1, l0, l1 + 1, mov, intervalo, i + 1, N, lado, mem))
        elif(mov != len(intervalo) and not(n >= intervalo[i][0] and n < intervalo[i][1]) and lado == 0):
          ans = solve(n + 1, l0 + 1, l1, mov, intervalo, i, N, lado, mem)
        elif(mov != len(intervalo) and not(n >= intervalo[i][0] and n < intervalo[i][1]) and lado == 1):
          ans = solve(n + 1, l0, l1 + 1, mov, intervalo, i, N, lado, mem)
        elif(mov == len(intervalo) and lado == 0):
          ans = solve(n + 1, l0 + 1, l1, mov, intervalo, i, N, lado, mem)
        elif(mov == len(intervalo) and lado == 1):
          ans = solve(n + 1, l0, l1 + 1, mov, intervalo, i, N, lado, mem)
      else:
        if(lado == 0):
          ans = solve(n + 1, l0 + 1, l1, mov, intervalo, i, N, lado, mem)
        else:
          ans = solve(n + 1, l0, l1 + 1, mov, intervalo, i, N, lado, mem)
      mem[(n, l0, l1, mov)] = ans

  return ans"""

def solve(l0, l1, mov, intervalo, i, N, lado):
  if(l0 == N):
    print(l0, l1, intervalo, mov)
    ans = mov
  elif(l0 > N or l1 > N):
    ans = float('inf')
  else:
    if(mov != len(intervalo)):
      if(intervalo[i][0] != intervalo[i][1] and lado == 0):
        intervalo[i] = (intervalo[i][0] + 1, intervalo[i][1])
        ans = min(solve(l0 + (intervalo[i][0] - l1), l1, mov + 1, intervalo, i, N, 1 - lado), solve(l0 + (intervalo[i][0] - l1), l1, mov, intervalo, i, N, lado))
      elif(intervalo[i][0] != intervalo[i][1] and lado == 1):
        intervalo[i] = (intervalo[i][0] + 1, intervalo[i][1])
        ans = min(solve(l0, l1 + (intervalo[i][0] - l0), mov + 1, intervalo, i, N, 1 - lado), solve(l0, l1 + (intervalo[i][0] - l0), mov, intervalo, i, N, lado))
      elif(intervalo[i][0] == intervalo[i][1] and lado == 0):
        ans = min(solve(l0 + (intervalo[i][0] - l1), l1, mov + 1, intervalo, i + 1, N, 1 - lado), solve(l0 + (intervalo[i][0] - l1), l1, mov, intervalo, i + 1, N, lado))
      elif(intervalo[i][0] == intervalo[i][1] and lado == 1):
        ans = min(solve(l0, l1 + (intervalo[i][0] - l0), mov + 1, intervalo, i + 1, N, 1 - lado), solve(l0, l1 + (intervalo[i][0] - l0), mov, intervalo, i + 1, N, lado))
    else:
      if(lado == 0):
        ans = solve(l0 + (2 * N - l0 - l1), l1, mov, intervalo, len(intervalo), N, lado)
      else:
        #print(l0, l1)
        ans = solve(l0, l1 + (2 * N - l1 - l0), mov, intervalo, len(intervalo), N, lado)
  
  return ans
def main():
  #print(solve(0, 0, 0, [(2, 4), (6, 9), (11, 15)], 0, 10, 0))
  #print(solve(0, 0, 0, [(2, 5), (35, 38)], 0, 20, 0))
  print(solve(0, 0, 0, [(1, 2), (23, 23), (38, 43)], 0, 25, 0))
  #print(solve(0, 0, 0, [(4, 5), (13, 15), (22, 24)], 0, 15, 0))
  #print(solve(0, 0, 0, 0, [(2, 4), (6, 9), (11, 15)], 0, 10, 0))
  #print(solve(0, 0, 0, 0, [(2, 5), (35, 38)], 0, 20, 0))
  #print(solve(0, 0, 0, 0, [(1, 2), (23, 23), (38, 43)], 0, 25, 0))
  #print(solve(0, 0, 0, 0, [(4, 5), (13, 15), (22, 24)], 0, 15, 0))
  #print(solve(0, 0, 0, 0, [(1, 2), (3, 4), (5, 6)], 0, 6, 0))

main()
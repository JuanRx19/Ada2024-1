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

"""def solve(l0, l1, mov, intervalo, i, N, lado, data):
  if(l0 == N):  
    #print(data)
    ans = mov
  elif(l0 > N or l1 > N):
    #print(data, mov)
    ans = float('inf')
  else:
    if(i != len(intervalo) and mov != len(intervalo)):
      if(intervalo[i][0] != intervalo[i][1] and lado == 0):
        temp = intervalo[i][0]
        temp2 = (intervalo[i][0], intervalo[i][1])
        intervalo[i] = (intervalo[i][0] + 1, intervalo[i][1])
        data.append((l0, l1, mov, lado, temp, 1.1))
        girar = solve(l0 + abs(temp - l1 - l0), l1, mov + 1, intervalo, i, N, 1 - lado, data)
        data.pop()

        intervalo[i] = temp2
        data.append((l0, l1, mov, lado, temp, intervalo, 1.2))
        nogirar = solve(l0 + abs(temp - l1 - l0), l1, mov, intervalo, i, N, lado, data)
        data.pop()

        ans = min(girar, nogirar)
      elif(intervalo[i][0] != intervalo[i][1] and lado == 1):
        temp = intervalo[i][0]
        temp2 = (intervalo[i][0], intervalo[i][1])
        intervalo[i] = (intervalo[i][0] + 1, intervalo[i][1])
        data.append((l0, l1, mov, lado, temp, 2.1))
        girar = solve(l0, l1 + abs(temp - l1 - l0), mov + 1, intervalo, i, N, 1 - lado, data)
        data.pop()

        intervalo[i] = temp2
        data.append((l0, l1, mov, lado, temp, 2.2))
        nogirar = solve(l0, l1 + abs(temp - l1 - l0), mov, intervalo, i, N, lado, data)
        data.pop()
        ans = min(girar, nogirar)
      elif(intervalo[i][0] == intervalo[i][1] and lado == 0):
        data.append((l0, l1, mov, lado, intervalo[i][0], 3.1))
        girar = solve(l0 + abs(intervalo[i][0] - l1 - l0), l1, mov + 1, intervalo, i + 1, N, 1 - lado, data)
        data.pop()

        data.append((l0, l1, mov, lado, intervalo[i][0], 3.2))
        nogirar = solve(l0 + abs(intervalo[i][0] - l1 - l0), l1, mov, intervalo, i + 1, N, lado, data)
        data.pop()
        ans = min(girar, nogirar)
      elif(intervalo[i][0] == intervalo[i][1] and lado == 1):
        data.append((l0, l1, mov, lado, intervalo[i][0], 4.1))
        girar = solve(l0, l1 + abs(intervalo[i][0] - l1 - l0), mov + 1, intervalo, i + 1, N, 1 - lado, data)
        data.pop()

        data.append((l0, l1, mov, lado, intervalo[i][0], 4.2))
        nogirar = solve(l0, l1 + abs(intervalo[i][0] - l1 - l0), mov, intervalo, i + 1, N, lado, data)
        data.pop()
        ans = min(girar, nogirar)
    else:
      if(lado == 0):
        data.append((l0, l1, mov, lado, 5.1))
        ans = solve(l0 + abs(2 * N - l0 - l1), l1, mov, intervalo, len(intervalo), N, lado, data)
        data.pop()
      else:
        #print(l0, l1)
        data.append((l0, l1, mov, lado, 5.2))
        ans = solve(l0, l1 + abs(2 * N - l1 - l0), mov, intervalo, len(intervalo), N, lado, data)
        data.pop()
  
  return ans"""

"""def solve(l0, l1, mov, intervalo, i, j, N, lado, mem):
  if((l0, l1, mov) in mem):
    ans = mem[(l0, l1, mov)]
  else:
    if(l0 == N and l1 == N):  
      #print(l0, l1, mov, i, j, intervalo[i-1])
      ans = mov
    elif(l0 > N or l1 > N):
      #print(data, mov)
      ans = float('inf')
    else:
      if(i != len(intervalo) and mov != len(intervalo)):
        if((intervalo[i][0] + j) != intervalo[i][1] and lado == 0):
          ans = min(solve(l0 + abs((intervalo[i][0] + j) - l1 - l0), l1, mov + 1, intervalo, i, j + 1, N, 1 - lado, mem), solve(l0 + abs((intervalo[i][0] + j) - l1 - l0), l1, mov, intervalo, i, j + 1, N, lado, mem))
        elif((intervalo[i][0] + j) != intervalo[i][1] and lado == 1):
          ans = min(solve(l0, l1 + abs((intervalo[i][0] + j) - l1 - l0), mov + 1, intervalo, i, j + 1, N, 1 - lado, mem), solve(l0, l1 + abs((intervalo[i][0] + j) - l1 - l0), mov, intervalo, i, j + 1, N, lado, mem))
        elif((intervalo[i][0] + j) == intervalo[i][1] and lado == 0):
          ans = min(solve(l0 + abs((intervalo[i][0] + j) - l1 - l0), l1, mov + 1, intervalo, i + 1, 0, N, 1 - lado, mem), solve(l0 + abs((intervalo[i][0] + j) - l1 - l0), l1, mov, intervalo, i + 1, 0, N, lado, mem))
        elif((intervalo[i][0] + j) == intervalo[i][1] and lado == 1):
          ans = min(solve(l0, l1 + abs((intervalo[i][0] + j) - l1 - l0), mov + 1, intervalo, i + 1, 0, N, 1 - lado, mem), solve(l0, l1 + abs((intervalo[i][0] + j) - l1 - l0), mov, intervalo, i + 1, 0, N, lado, mem))
      else:
        if(lado == 0):
          ans = solve(l0 + abs(2 * N - l0 - l1), l1, mov, intervalo, len(intervalo), j, N, lado, mem)
        else:
          ans = solve(l0, l1 + abs(2 * N - l1 - l0), mov, intervalo, len(intervalo), j, N, lado, mem)
    mem[(l0, l1, mov)] = ans
  
  return ans"""

"""
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
"""

#No funca
"""
def convertir(interval, i, j, l0, l1, mov, N):
  value = abs((interval[i][0] + j) - l1 - l0)
  if(i == len(interval) and mov != len(interval)):
    if((interval[i][0] + j) != interval[i][1]):
      j += 1
    else:
      j = 0
      i += 1
  else:
    value = abs(2 * N - l1 - l0)
    i = len(interval)
    
  return value, i, j

def solve(l0, l1, mov, intervalo, i, j, N, lado, mem):
  if((l0, l1, mov) in mem):
    ans = mem[(l0, l1, mov)]
  else:
    if(l0 == N):
      if(l1 != N):
        ans = mov + 1
      else:
        ans = mov
    elif(l0 > N or l1 > N):
      ans = INF
    else:
      value, i, j = convertir(intervalo, i, j, l0, l1, mov, N)
      if(lado == 0):
        ans = min(solve(l0 + value, l1, mov + 1, intervalo, i, j, N, 1 - lado, mem), solve(l0 + value, l1, mov, intervalo, i, j, N, lado, mem))
      else:
        ans = min(solve(l0, l1 + value, mov + 1, intervalo, i, j, N, 1 - lado, mem), solve(l0, l1 + value, mov, intervalo, i, j, N, lado, mem))
      
    mem[(l0, l1, mov)] = ans
  
  return ans"""

#Funca versión vieja
"""
if((l0, l1, mov) in mem):
    ans = mem[(l0, l1, mov)]
  else:
    if(l0 == N):
      if(l1 != N):
        ans = mov + 1
      else:
        ans = mov
    elif(l0 > N or l1 > N):
      ans = float('inf')
    else:
      if(i != len(intervalo) and mov != len(intervalo)):
        value, i, j = convertir(intervalo[i], i, j)
        if(lado == 0):
          ans = min(solve(l0 + abs(value - l1 - l0), l1, mov + 1, intervalo, i, j, N, 1 - lado, mem),
                    solve(l0 + abs(value - l1 - l0), l1, mov, intervalo, i, j, N, lado, mem))
        else:
          ans = min(solve(l0, l1 + abs(value - l1 - l0), mov + 1, intervalo, i, j, N, 1 - lado, mem),
                    solve(l0, l1 + abs(value - l1 - l0), mov, intervalo, i, j, N, lado, mem))
      else:
        if(lado == 0):
          ans = solve(l0 + abs(2 * N - l0 - l1), l1, mov, intervalo, len(intervalo), j, N, lado, mem)
        else:
          ans = solve(l0, l1 + abs(2 * N - l1 - l0), mov, intervalo, len(intervalo), j, N, lado, mem)
    mem[(l0, l1, mov)] = ans
  
  return ans
  """

"""
def convertir(interval, i, j):
  
  Esta función define el paso siguiente a dar entre los intervalos, si el limite inferior es igual al
  superior, entonces debo pasar al siguiente intervalo. Por ejemplo, si tengo (4, 4) significa que no tengo mas valores
  para buscar dentro del intervalo (4, 4), por lo que avanzo al siguiente intervalo.
  
  Parametros: interval --> tupla con el limite inferior y superior.
              i --> el intervalo en el que se encuentra.
              j --> el valor a sumar al limite inferior.
  
  Retorna: La suma del limite inferior + j, el intervalo y el valor a sumar en la siguiente recurrencia.
  
  value = (interval[0] + j)
  if((interval[0] + j) != interval[1]):
    j += 1
  else:
    j = 0
    i += 1
  return value, i, j

def solve(l0, l1, intervalo, i, j, N, mem):
  if((l0, l1, i) in mem):
    ans = mem[(l0, l1, i)]
  else:
    if(l0 == N):
      if(l1 != N):
        ans = 1
      else:
        ans = 0
    elif(i == len(intervalo) or l0 > N or l1 > N):
      ans = INF
    else:
      value, i, j = convertir(intervalo[i], i, j)
      ans = min(solve(l1, l0 + (value - (l1 + l0)), intervalo, i, j, N, mem) + 1,
                solve(l0 + (value - (l1 + l0)), l1, intervalo, i, j, N, mem))
    mem[(l0, l1, i)] = ans

  return ans
"""
def main():
  pass
  #print(solve(0, 0, 0, [(2, 4), (6, 9), (11, 15)], 0, 0, 10, 0))
  #print(solve(0, 0, 0, [(2, 5), (35, 38)], 0, 0, 20, 0))
  #print(solve(0, 0, 0, [(1, 2), (23, 23), (38, 43)], 0, 0, 25, 0))
  #print(solve(0, 0, 0, [(4, 5), (13, 15), (22, 24)], 0, 0, 15, 0))
  #print(solve(0, 0, 0, 0, [(2, 4), (6, 9), (11, 15)], 0, 10))
  #print(solve(0, 0, 0, 0, [(2, 5), (35, 38)], 0, 20))
  #print(solve(0, 0, 0, 0, [(1, 2), (23, 23), (38, 43)], 0, 25))
  #print(solve(0, 0, 0, 0, [(4, 5), (13, 15), (22, 24)], 0, 15))
  #print(solve(0, 0, 0, 0, [(1, 2), (3, 4), (5, 6)], 0, 6, 0))
main()
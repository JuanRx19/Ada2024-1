def phi(A, m, n):
  ans = None
  if(m >= n):
    ans = 0
  elif(m + 1 == n):
    ans = 1
  elif(m + 1 < n and A[m] != A[n - 1]):
    ans = max(phi(A, m + 1, n), phi(A, m, n - 1))
  else:
    ans = 2 + phi(A, m + 1, n - 1)

  return ans

def phiTab(A, M, N):
  tab = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
  
  for m in range(N + 1):
    for n in range(N + 1):
      if(m + 1 == n):
        tab[m][n] = 1
  print(tab)
  for m in range(2, N + 1):
    for n in range(N + 1):
      print(m, n)
      if(m + 1 < n and A[m] != A[n - 1]):
        tab[m][n] = max(tab[m+1][n], tab[m][n-1])
      else:
        #print(m + 1)
        tab[m][n] = 2 + tab[m+1][n-1]
  
  return tab[N][0]
print(phi("A", 0, 1))
print(phi("ADA", 0, 3))
print(phi("RADAR", 0, 5))
print(phi("TAREA", 0, 5))
print(phi("ALGORITMO", 0, 9))
#print(phiTab("A", 0, 1))
print(phiTab("ADA", 0, 3))
#print(phiTab("RADAR", 0, 5))
#print(phiTab("TAREA", 0, 5))
#print(phiTab("ALGORITMO", 0, 9))
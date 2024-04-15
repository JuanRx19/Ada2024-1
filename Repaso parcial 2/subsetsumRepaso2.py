def subsetsum(A, n, x):
  ans = None
  if n==0:
    ans = x == 0
  else:
    if A[n-1]<=x:
      ans = subsetsum(A, n-1, x) or subsetsum(A, n-1, x-A[n-1])
    else:
      ans = subsetsum(A, n-1, x)
  return ans

def subsetsumTab(A, N, X):
  tab = [[False for _ in range(X + 1)] for _ in range(N + 1)]
  for n in range(N + 1):
    tab[n][0] = True

  for n in range(1, N + 1):
    for x in range(X + 1):
      if(A[n-1] <= x):
        tab[n][x] = tab[n-1][x] or tab[n-1][x - A[n-1]]
      else:
        tab[n][x] = tab[n-1][x]
  
  return tab[N][X]

print(subsetsum([1, 2, 3, 4, 5], 5, 16))
print(subsetsumTab([1, 2, 3, 4, 5], 5, 16))
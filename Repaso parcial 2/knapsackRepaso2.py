W = [6, 2, 11, 6, 4] #[6, 3, 4, 7]
B = [4, 2, 1, 2, 10] #[3, 1, 5, 2]
N = len(W)
M = 15 #20

def knapsack(m, n):
    ans = None
    if n == 0 or m == 0:
      ans = 0
    elif W[n - 1] > m:
      ans = knapsack(m, n - 1)
    else:
      ans = max(knapsack(m, n - 1), knapsack(m - W[n - 1], n - 1) + B[n - 1])
    return ans

def knapsackTab(M, N):
    tab = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for n in range(1, N + 1):
       for m in range(1, M + 1):
          if(W[n - 1] > m):
             tab[n][m] = tab[n-1][m]
          else:
             tab[n][m] = max(tab[n-1][m], tab[n-1][m - W[n - 1]] + B[n - 1])
    
    return tab[N][M]

def knapsackOpt(M, N):
    tab = [[0 for _ in range(M + 1)] for _ in range(2)]
    prev = 0
    curr = 1
    for n in range(1, N + 1):
        for m in range(1, M + 1):
          if(W[n - 1] > m):
            tab[curr][m] = tab[prev][m]
          else:
            tab[curr][m] = max(tab[prev][m], tab[prev][m - W[n - 1]] + B[n - 1])
        prev = 1 - prev
        curr = 1 - curr
    return tab[1][M]

def knapsackOptTab(M, N):
    tab = [0 for _ in range(M + 1)]
    for n in range(1, N + 1):
      for m in range(M, -1, -1):
          if(W[n - 1] > m):
            tab[m] = tab[m]
          else:
            tab[m] = max(tab[m], tab[m - W[n - 1]] + B[n - 1])
    return tab[M]

print(knapsack(M, N))
print(knapsackTab(M, N))
print(knapsackOpt(M, N))
print(knapsackOptTab(M, N))
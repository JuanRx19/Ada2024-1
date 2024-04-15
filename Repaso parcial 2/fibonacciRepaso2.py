
def fib(n):
  ans = None
  if(n <= 1):
    ans = n
  else:
    ans = fib(n-2) + fib(n-1)

  return ans

def fibTab(N):
  tab = [0 for _ in range(N + 1)]
  if(N >= 1):
    tab[1] = 1

  for n in range(2, N + 1):
    tab[n] = tab[n-2] + tab[n-1]

  return tab[N]

val = 2

print(fibTab(val))
print(fib(val))
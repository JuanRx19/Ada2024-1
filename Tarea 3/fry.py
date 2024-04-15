from sys import stdin

def reverse(A):
    temp = []
    for i in range(len(A) - 1, -1, -1):
        temp.append(A[i])
    
    return temp

def solve(T, E, n, feces, mem):
    if((n, feces) in mem):
        ans = mem[(n, feces)]
    else:
        if(n == 0):
            ans = 0
        else:
            if feces >= n:
                ans = solve(T, E, n-1, (feces - 1) + E[n-1], mem) + (T[n-1] >> 1)
            else:
                if(n != 0 and feces != 0):
                    ans = min(solve(T, E, n-1, (feces - 1) + E[n-1], mem) + (T[n-1] >> 1), solve(T, E, n-1, feces + E[n-1], mem) + T[n-1])
                else:
                    ans = solve(T, E, n-1, feces + E[n-1], mem) + T[n-1]
        mem[(n, feces)] = ans

    return ans

def solveTab(T, E, t, feces): #  t es igual a n, pero no al iterador
    tab = [[0 for _ in range(len(E) + 1)] for _ in range(len(T) + 1)]
    for n in range(1, len(T) + 1):
        for f in range(feces):
            if(f != 0):
                tab[n][f] = min(tab[n-1][feces - 1 + E[n-1]] + (T[n-1] >> 1), tab[n-1][feces + E[n - 1]] + T[n-1])
            else:
                tab[n][f] = tab[n-1][feces + E[n-1]]
        feces = E[n-1]
    return tab

def solveTab2(T, E, t, feces): #  t es igual a n, pero no al iterador
    tab = [[0 for _ in range(len(E) + 1)] for _ in range(len(T) + 1)]
    for n in range(1, len(T) + 1):
        for f in range(len(E) + 1):
            if(n != 0 and E[f-1] != 0):
                #print("If")
                #print(tab[n-1][(feces -  1) + E[n-1]] + (T[n-1] >> 1), tab[n-1][feces + E[n-1]] + T[n-1])
                tab[n][f] = min(tab[n-1][(feces -  1) + E[n-1]] + (T[n-1] >> 1), tab[n-1][feces + E[n-1]] + T[n-1])
            else:
                #print("Else")
                #print(tab[n-1][feces + E[n-1]] + T[n-1])
                tab[n][f] = tab[n-1][feces + E[feces-1]] + T[n-1]

    return tab

def phi(T, E):
  N,SE = len(T),sum(E)
  tab = [ [ 0 for _ in range((SE<<1)+1) ] for _ in range(2) ]
  n, e, curr, prev = N-1, 0, 0, 1
  while n!=-1:
    print(e)
    if e==SE+1:
      n,e,curr,prev = n-1,0,1-curr,1-prev
    else:
      if e==0:
        tab[curr][e] = T[n]+tab[prev][e+E[n]]
      else:
        tab[curr][e] = min(T[n]+tab[prev][e+E[n]], (T[n]>>1)+tab[prev][e+E[n]-1])
      e += 1
  return tab

def main():
    C = int(stdin.readline())
    while(C != 0):
        mem = {}
        T = []
        E = []
        for _ in range(C):
            TE = list(map(int, stdin.readline().split()))
            T.append(TE[0])
            E.append(TE[1])
        print(solveTab2(reverse(T), reverse(E), len(T), 0))
        #print(solveTab2(reverse(T), reverse(E), len(T), 0))
        #print(phi(T, E))
        print(solve(reverse(T), reverse(E), len(T), 0, mem))
        C = int(stdin.readline())

main()
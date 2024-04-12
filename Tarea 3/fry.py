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

def solveTab(T, E): #  t es igual a n, pero no al iterador
    print(T)
    print(E)
    feces = 0
    tab = [[0] * (len(E) + 1)] * (len(T) + 1)
    for n in range(1, len(T) + 1):
        for f in range(len(E) + 1):
            if(n != 0 and E[f-1] != 0):
                #print("If")
                #print(tab[n-1][(feces -  1) + E[n-1]] + (T[n-1] >> 1), tab[n-1][feces + E[n-1]] + T[n-1])
                tab[n][f] = min(tab[n-1][(f -  1) + E[f-1]] + (T[n-1] >> 1), tab[n-1][feces + E[f-1]] + T[n-1])
            else:
                #print("Else")
                #print(tab[n-1][feces + E[n-1]] + T[n-1])
                #print(E)
                tab[n][f] = tab[n-1][feces + E[f-1]] + T[n-1]

    return tab[len(E)][len(T)]
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
        print(solveTab(reverse(T), reverse(E)))
        print(solve(reverse(T), reverse(E), len(T), 0, mem))
        C = int(stdin.readline())

main()
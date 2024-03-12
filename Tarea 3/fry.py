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
        print(solve(reverse(T), reverse(E), len(T), 0, mem))
        C = int(stdin.readline())

main()
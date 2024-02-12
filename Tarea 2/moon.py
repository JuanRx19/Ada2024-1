from sys import stdin

def biseccion(f, a, b, v):
    low, hi, ans = a, b, None
    eps = 1e-6
    iter = 0
    while iter < 50:
        mid = (hi + low) / 2
        if v <= f(mid): 
            hi = mid
        else: 
            low = mid
        iter += 1
        ans = low
    return ans

def f(D, T):
    return D/T

def solve(T, S, D):
    print(D > T)
    return biseccion(f, 0, 100000000, S) # T S D, D T S, D S T

def main():
    C = int(stdin.readline())
    for _ in range(C):
        T, S, D = map(int, stdin.readline().split())
        print(solve(T, S, D))

main()
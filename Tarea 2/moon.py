from sys import stdin
import math

def f(v, T):
    return v * T

def biseccion(f, a, b, v, T):
    low, hi, ans = a, b, None
    iter = 0
    while iter < 50:
        mid = (hi + low) / 2
        if v <= f(mid, T): 
            hi = mid
        else: 
            low = mid
        iter += 1
        ans = low
    return math.floor(ans)

def solve(T, S, D):
    ans = biseccion(f, 0, 5000000, abs(D * 1000000), T * 86400)
    if(D > 0 and ans != 0):
        print(f"Remove {ans} tons")
    else:
        print(f"Add {ans} tons")

def main():
    C = int(stdin.readline())
    for _ in range(C):
        T, S, D = map(int, stdin.readline().split())
        solve(T, S, D)

main()
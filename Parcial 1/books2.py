#Juan Miguel Rojas Mejía
#8963761
from sys import stdin

def f(x, A):
    ans = 1
    ac = 0
    for i in range(len(A)): 
        if(A[i] + ac > x):
            ans+=1
            ac = A[i]
        else:
            ac += A[i]

    return ans

def solve(A, k):
    l = max(A) #15 - 5 > 5
    r = sum(A)
    while l < r:
        mid = l + ((r - l) >> 1)
        if f(mid, A) <= k:
            r = mid
        else:
            l = mid + 1
    return l

def main():
    line = stdin.readline().strip()
    while(line != ""):
        n, m = map(int, line.split())
        A = list(map(int, stdin.readline().split()))
        print(solve(A, m))
        line = stdin.readline().strip()

main()
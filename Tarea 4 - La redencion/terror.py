#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

def solve(N, K, X, Y):
    ans = 0

    for i in range(N):
        Y[i] = Y[i] - X[i]
    
    Y.sort()

    for i in range(N):
        if(Y[i] < 0 and K != 0):
            K -= 1
        else:
            ans += Y[i]
    
    return ans

def main():
    C = int(stdin.readline())
    iter = 0
    while(C != iter):
        N, K = map(int, stdin.readline().split())
        X = list(map(int, stdin.readline().split()))
        Y = list(map(int, stdin.readline().split()))
        ans = solve(N, K, X, Y)
        if(ans <= 0):
            print(f"Case {iter+1}: No Profit")
        else:
            print(f"Case {iter+1}: {ans}")
        iter+=1

main()
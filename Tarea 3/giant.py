from sys import stdin

def solve(n, k):
    dp = [[0] * 505 for _ in range(505)]
    for L in range(2, n + 1):
        for i in range(1, n-L+2):
            j = i+L-1
            dp[i][j] = float('inf')
            for p in range(i, j + 1):
                dp[i][j] = min(dp[i][j], dp[i][p-1] + dp[p+1][j] + (p+k) * L)

    return dp[1][n]

def main():
    C = int(stdin.readline())
    i = 0
    while(C != i):
        n, k = map(int, stdin.readline().split())
        print(f"Case {i+1}: {solve(n, k)}")
        i+=1

main()
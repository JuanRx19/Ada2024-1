def dfs(n, k, dp):
    if dp[n][k] != -1:
        return dp[n][k]
    if n <= 1:
        return 0
    v = float('inf')
    for i in range(1, n + 1):
        tmp = n * (k + i) + dfs(i - 1, k, dp) + dfs(n - i, k + i, dp)
        v = min(v, tmp)
    dp[n][k] = v
    return v

def main():
    t = int(input())
    for case in range(1, t + 1):
        n, k = map(int, input().split())
        dp = [[-1] * 505 for _ in range(505)]
        result = dfs(n, k, dp)
        print("Case {}: {}".format(case, result))

if __name__ == "__main__":
    main()


"""from sys import stdin

def solve():
    pass

def main():
    C = int(stdin.readline())
    while(C != 0):
        n, m = map(int, stdin.readline().split())
        print(solve(n, m))
        C-=1

main()"""
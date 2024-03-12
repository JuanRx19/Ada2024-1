from sys import stdin

def solve(A, n, x, dp):
    ans = 0
    if(dp[n][x] != -1):
        ans = dp[n][x]
    else:
        if(n == 0):
            ans = -float('inf')
        elif(x <= 0):
            ans = x
        else:
            ans = max(solve(A, n-1, x - (A[n-1]), dp), solve(A, n-1, x, dp))
        dp[n][x] = ans
    return ans

def main():
    C = int(stdin.readline())
    while(C != 0):
        calories = int(stdin.readline())
        tam = int(stdin.readline())
        A = list(map(int, input().split()))
        dp = [[-1] * (105) for _ in range(2505)]
        if(sum(A) > calories):
            print(f"{calories + (solve(A, tam, calories, dp) * -1)}")
        else:
            print("NO SOLUTION")
        C-=1

main()
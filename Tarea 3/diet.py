from sys import stdin

def solve(A, n, x):
    ans = 0
    if(n == 0 or x <= 0):
        ans = 0
    elif(n != 0 and x > 0):
        ans = min(solve(A, n-1, x - A[n-1]) + A[n-1], solve(A, n-1, x) + A[n-1])

    return ans

def main():
    C = int(stdin.readline())
    while(C != 0):
        calories = int(stdin.readline())
        tam = int(stdin.readline())
        A = list(map(int, input().split()))
        ans = solve(A, tam, calories)
        if(ans >= calories):
            print(f"{solve(A, tam, calories)}")
        else:
            print("NO SOLUTION")
        C-=1

main()
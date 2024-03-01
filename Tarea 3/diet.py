from sys import stdin

def solve(A, n, x, mem):
    ans = 0
    if((n, x) in mem):
        ans = mem[(n, x)]
    else:   
        if(n == 0 and x > 0):
            ans = -float('inf')
        elif(n == 0 or x <= 0):
            ans = x
        elif(n != 0 and x > 0):
            ans= max(solve(A, n-1, x - A[n-1], mem), solve(A, n-1, x, mem))
            mem[(n, x)] = ans
    return ans

def main():
    C = int(stdin.readline())
    while(C != 0):
        mem = {}
        calories = int(stdin.readline())
        tam = int(stdin.readline())
        A = list(map(int, input().split()))
        ans = solve(A, tam, calories, mem)
        if(abs(ans) != float('inf')):
            print(f"{calories + abs(ans)}")
        else:
            print("NO SOLUTION")
        C-=1

main()
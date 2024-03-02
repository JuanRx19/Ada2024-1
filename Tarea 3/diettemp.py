from sys import stdin

def solve(A, ite, n, x, mem):
    ans = 0
    if((ite, x) in mem):
        ans = mem[(ite, x)]
    else:
        if(ite == n and x > 0):
            ans = -float('inf')
        elif(ite == n or x <= 0):
            ans = x
        elif(ite != n and x > 0):
            ans = max(solve(A, ite+1, n, x - (A[ite]), mem), solve(A, ite+1, n, x, mem))
            mem[(ite, x)] = ans
    return ans

def main():
    C = int(stdin.readline())
    while(C != 0):
        mem = {}
        calories = int(stdin.readline())
        tam = int(stdin.readline())
        A = list(map(int, input().split()))
        ans = solve(A, 0, tam, calories, mem)
        if(abs(ans) != float('inf')):
            print(f"{calories + abs(ans)}")
        else:
            print("NO SOLUTION")
        C-=1

main()
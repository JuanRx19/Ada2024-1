#from sys import stdin

def solve(A, n, x):
    ans = 0
    if(n == 0 or x == 0):
        ans = 0
    elif(n != 0 and x != 0 and x < 0):
        ans = 0 #solve(A, n-1, x)
    elif(n != 0 and x != 0 and x > 0):
        ans = min(solve(A, n-1, x - A[n-1]) + A[n-1], solve(A, n-1, x) + A[n-1])

    return ans

"""def main():
    C = int(stdin.readline())
    while(C != 0):
        calories = int(stdin.readline())
        tam = int(stdin.readline())
        A = list(map(int, input().split()))
        print(f"{solve(A, tam, calories)}")
        C-=1"""

print(f"{solve([1230, 1050, 820, 890, 1150], 5, 2480)}")
#main()
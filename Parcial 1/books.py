#Juan Miguel Rojas Mejía
#8963761
from sys import stdin

def f(A, mid):
    lib = 0
    contLib = 1
    for i in range(len(A)):
        if(lib + A[i] > mid):
            lib = A[i]
            contLib+=1
        else:
            lib += A[i]
    return contLib

def build(A, x):
    lib = 0
    contLib = 1
    config = ""
    for i in range(len(A)):
        if(lib + A[i] > x):
            lib = A[i]
            config += "/ " + str(A[i]) + " "
            contLib+=1
        else:
            lib += A[i]
            config += str(A[i]) + " "
    
    return config[0:len(config)-1]

def solve(A, m):
    mid = 0
    left = max(A)
    right = sum(A)
    while(left < right):
        mid = left + ((right - left) >> 1)
        ans = f(A, mid)
        if(ans <= m):
            right = mid
        elif(ans > m):  
            left = mid + 1
    return build(A, left)

def main():
    C = int(stdin.readline())
    while(C != 0):
        n, m = map(int, stdin.readline().split())
        A = list(map(int, stdin.readline().split()))
        print(solve(A, m))
        C-=1

main()
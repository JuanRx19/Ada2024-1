#Juan Miguel Rojas Mejía
#8963761
from sys import stdin

def reverse(A):
    temp = []
    for i in range(len(A) - 1, -1, -1):
        temp.append(A[i])
    
    return temp

def f(A, mid):
    lib = 0
    contLib = 1
    for i in range(len(A)):
        if(lib + A[i] <= mid):
            lib += A[i]
        else:
            lib = A[i]
            contLib+=1
    return contLib

def build(A, x, m):
    A = reverse(A)
    temp = []
    lib = 0
    iter = 0
    for i in range(len(A)):
        lib += A[i]
        if(lib > x):
            lib = A[i]
            temp.append("/")
            temp.append(A[i])
        else:
            temp.append(A[i])
    
    temp = reverse(temp)
    while(len(A)-1 + m > len(temp)):
        if(temp[iter] != "/" and temp[iter + 1] != "/"):
            temp.insert(iter+1, "/")
        iter += 1
    return temp

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
    
    return ' '.join(map(str, build(A, left, m)))

def main():
    C = int(stdin.readline())
    while(C != 0):
        n, m = map(int, stdin.readline().split())
        A = list(map(int, stdin.readline().split()))
        print(solve(A, m))
        C-=1

main()
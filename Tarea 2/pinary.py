from sys import stdin

"""def binarysearch(A, low, high,  x):
    ans = 0
    if(low+1 == high):
        ans = A[low]    
    else:
        mid = low + ((high-low)>>1)
        if(A[mid][0] == x):
            ans = A[mid]
        elif(A[mid][0] < x):
            ans = binarysearch(A,  mid, high, x)
        else:
            ans = binarysearch(A, low, mid, x)

    return ans"""

def binarysearch(A, low, high, x):
    ans = 0
    flag = 0
    while(flag == 0):
        if(low+1 == high):
            ans = A[low]
            flag = 1
        else:
            mid = low + ((high-low)>>1)
            if(A[mid][0] == x):
                ans = A[mid]
                flag = 1
            elif(A[mid][0] < x):
                low = mid
            else:
                high = mid
    return ans

def init(A, tam):
    ant = 1
    act = 2
    pinary = 10
    for _ in range(tam):
        val = ant + act
        ant = act 
        act = val
        pinary*=10
        A.append([val, pinary])
    return A

"""def solve(A, n):
    ans = 0
    nivel = binarysearch(A, 0, len(A) - 1, n)
    if(nivel[0] == n):
        ans = nivel[1]
    else:
        ans += nivel[1] + solve(A, n - nivel[0])
    
    return ans"""

def solve(A, n):
    ans = 0
    flag = 0
    while(flag == 0):
        nivel = binarysearch(A, 0, len(A) - 1, n)
        if(nivel[0] == n):
            ans += nivel[1]
            flag = 1
        else:
            ans += nivel[1]
            n = n - nivel[0]
            
    return ans

def main():
    A = [[1, 1], [2, 10]]
    A = init(A, 37)
    T = int(stdin.readline())
    for _ in range(T):
        val = int(stdin.readline())
        print(solve(A, val))

main()
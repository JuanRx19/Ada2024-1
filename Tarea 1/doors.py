from sys import stdin
import math

"""def binarysearch(low, high, x):
    ans = 0
    if(low+1 == high):
        ans = low
    else:
        mid = low + ((high-low)>>1)
        if(mid**2 <= x):
            ans = binarysearch(mid, high, x)
        else:
            ans = binarysearch(low, mid, x)
    
    return ans"""

def binarysearch(low, high, x):
    ans = 0
    flag = 0
    while(flag == 0):
        if(low+1 == high):
            ans = low
            flag = 1
        else:
            mid = low + ((high-low)>>1)
            if(mid*mid <= x):
                low = mid
            else:
                high = mid
    return ans

def solve(T):
    if(T == 1):
        ans = 1
    else:
        ans = binarysearch(1, T, T)
    
    return ans * ans

def main():
    T = int(stdin.readline())
    while(T != 0):
        print(solve(T))
        T = int(stdin.readline())

main()
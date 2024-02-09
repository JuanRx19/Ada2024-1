from sys import stdin
import math

def binarysearch(low, high, x):
    ans = 0
    if(low+1 == high):
        ans = low
    else:
        mid = low + ((high-low)>>1)
        if(mid**2 <= x):
            ans = binarysearch(mid, high, x)
        else:
            ans = binarysearch(low, mid, x)
    
    return ans

def solve(T):
    raiz = math.sqrt(T)
    if(T == 1):
        ans = 1
    elif(type(raiz) == int):
        ans = T
    else:
        ans = (binarysearch(1, T, T))**2
    
    return ans

def main():
    T = int(stdin.readline())
    while(T != 0):
        print(solve(T))
        T = int(stdin.readline())

main()
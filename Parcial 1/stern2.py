#Juan Miguel Rojas Mejía
#8963761
from sys import stdin
import sys

"""sys.setrecursionlimit(2000)

def solve(n, d):
    ans = ""
    if(n == d):
        ans = ""
    else:
        if(n > d):
            n = n - d
            ans = "R" + solve(n, d)
        else:
            d = d - n
            ans = "L" + solve(n, d)
    
    return ans"""

def solve(n, d):
    ans = ""
    while(n != d):
        if(n > d):
            n = n - d
            ans += "R"
        else:
            d = d - n
            ans += "L"
    
    return ans

def main():
    n, d = map(int, stdin.readline().split())
    while(n != 1 or d != 1):
        print(solve(n, d))
        n, d = map(int, stdin.readline().split())

#main()
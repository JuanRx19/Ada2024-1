#Juan Miguel Rojas Mejía
#8963761
from sys import stdin

"""import sys

sys.setrecursionlimit(2000)

def solve(left, right, act, n, d):
    ans = ""
    if(act[0] == n and act[1] == d):
        ans = ""
    else:
        if(act[0] / act[1] > n / d): #1/1 > 5/7
            next = [act[0] + left[0], act[1] + left[1]]
            ans = "L" + solve(left, act, next, n, d)
        else:
            next = [act[0] + right[0], act[1] + right[1]]
            ans = "R" + solve(act, right, next, n, d)
    return ans"""

def solve(left, right, act, n, d):
    ans = ""
    while(act[0] != n or act[1] != d):
        if(act[0] * d  > n * act[1]): #1/1 > 5/7
            next = [act[0] + left[0], act[1] + left[1]]
            ans += "L"
            right = act
            act = next
        else:
            next = [act[0] + right[0], act[1] + right[1]]
            ans += "R"
            left = act
            act = next
    return ans

def main():
    left = [0, 1]
    right = [1, 0]
    act = [1, 1]
    n, d = map(int, stdin.readline().split())
    while(n != 1 or d != 1):
        print(solve(left, right, act, n, d))
        n, d = map(int, stdin.readline().split())

main()
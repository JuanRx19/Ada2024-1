from sys import stdin

def f(n):
    ans = None
    if(n==0):
        ans = 0
    else:
        ans = (n%10) + f(n//10)
    return ans

def g(n):
    ans = None
    if(n < 10):
        ans = n
    else:
        ans = g(f(n))
    return ans

def main():
    n = int(stdin.readline())
    while(n!=0):
        print(g(n))
        n = int(stdin.readline())

main()
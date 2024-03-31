#Juan Miguel Rojas Mejía
#8963761

from sys import stdin
from collections import deque

def solve(tianJiL, kingL, N):
    tianJi = deque()
    king = deque ()
    tianJi.extend(tianJiL)
    king.extend(kingL)
    ans = 0
    while(N != 0):
        if(tianJi[len(tianJi)-1] > king[len(king)-1]):
            ans+=200
            tianJi.pop()
            king.pop()
        elif(tianJi[len(tianJi)-1] < king[len(king)-1]):
            ans-=200
            king.pop()
            tianJi.popleft()
        else:
            if(tianJi[0] > king[0]):
                ans+=200
                tianJi.popleft()
                king.popleft()
            elif(king[len(tianJi)-1] != tianJi[0]):
                ans-=200
                king.pop()
                tianJi.popleft()
        N-=1

    return ans

def main():
    N = int(stdin.readline())
    val = 0
    while(N != 0):
        tianJi = list(map(int, stdin.readline().split()))
        king = list(map(int, stdin.readline().split()))
        tianJi.sort()
        king.sort()
        print(solve(tianJi, king, N))
        N = int(stdin.readline())

main()
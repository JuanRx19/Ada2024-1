#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

def solve(N, val):
    sortVal = val.copy()
    sortVal.sort()
    ans = 0
    iterSort = 0
    for i in range(N):
        if(val[i] != sortVal[iterSort]):
            ans+=1
        else:
            iterSort+=1
    
    return ans

def main():
    C = int(stdin.readline())
    i = 0
    while(C > i):
        N = int(stdin.readline())
        val = list(map(int, stdin.readline().split()))
        print(f"Case {i+1}: {solve(N, val)}")
        i += 1

main()
from sys import stdin
import heapq

def solve(n, k):
    med = []
    for i in range(n):
        m, t = stdin.readline().split()
        med.append((m, int(t)))
    tobby = med

    iterator = 0
    for cases in range(k):
        if(iterator < len(med) - 1):
            ant = heapq.heappop(tobby)
            heapq.heappush((med[iterator][0], med[iterator][1]))
            iterator+=1
        else:
            iterator=0
        print(iterator)
    print(med)

def main():
    T = int(stdin.readline())
    while(T>=1):
        n, k = map(int, stdin.readline().split())
        solve(n, k)
        T = T - 1

main()
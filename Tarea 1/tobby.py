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
        pass
    print(med)

def main():
    T = int(stdin.readline())
    while(T>=1):
        n, k = map(int, stdin.readline().split())
        solve(n, k)
        T = T - 1

main()
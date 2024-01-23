from sys import stdin
import heapq

def solve(n, k):
    med = []
    suma = []
    tobby = []
    for i in range(n):
        m, t = stdin.readline().split()
        suma.append(int(t))
        med.append((int(t), i, m))

    for i in range(len(med)):
        heapq.heappush(tobby, med[i])

    for _ in range(k):
        ans = heapq.heappop(tobby)
        #print(ans)
        print(str(ans[0]) + " " + ans[2])
        heapq.heappush(tobby, (ans[0] + suma[ans[1]], ans[1], ans[2]))

def main():
    T = int(stdin.readline())
    while(T>=1):            
        n, k = map(int, stdin.readline().split())
        solve(n, k)
        T = T - 1

main()
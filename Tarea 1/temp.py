import heapq

h = []
"""heapq.heappush(h, (40, 0, "Bceta"))
heapq.heappush(h, (20, 1, "Aor"))
heapq.heappush(h, (80, 0, "Bceta"))
heapq.heappush(h, (40, 1, "Aor"))
heapq.heappush(h, (60, 1, "Aor"))"""

heapq.heappush(h, (30, 0, "Aceta"))
heapq.heappush(h, (1, 1, "Lor"))


print(heapq.heappop(h))
print(heapq.heappop(h))
"""print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))"""

print()
"""
def solve(n, k):
    med = []
    tobby = []
    suma = []
    for i in range(n):
        m, t = stdin.readline().split()
        suma.append(int(t))
        med.append((int(t), i, m))

    iterator = 0
    for cases in range(k):
        if(iterator < n):
            heapq.heappush(tobby, (suma[iterator], med[iterator][1], med[iterator][2]))
            suma[iterator]+=med[iterator][0]
            iterator+=1
        else:
            iterator = 0
        
    print(tobby)

def main():
    T = int(stdin.readline())
    while(T>=1):
        n, k = map(int, stdin.readline().split())
        solve(n, k)
        T = T - 1

main()"""
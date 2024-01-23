import heapq

h = []
heapq.heappush(h, (40, "Aceta"))
heapq.heappush(h, (20, "Lor"))
heapq.heappush(h, (80, "Aceta"))
heapq.heappush(h, (40, "Lor"))
heapq.heappush(h, (60, "Lor"))


print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))
import heapq

h = []
heapq.heappush(h, (40, 0, "Bceta"))
heapq.heappush(h, (20, 1, "Aor"))
heapq.heappush(h, (80, 0, "Bceta"))
heapq.heappush(h, (40, 1, "Aor"))
heapq.heappush(h, (60, 1, "Aor"))


print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))
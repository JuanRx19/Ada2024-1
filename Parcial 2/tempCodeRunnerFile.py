#Juan Miguel Rojas Mejía
#8963761

from sys import stdin
import math

p, rango = [0 for _ in range(10001)], [0 for _ in range(10001)]

def makeSet(v):
  p[v], rango[v] = v, 0

def findSet(v):
    ans = None
    if v == p[v]:
        ans = v
    else:
        p[v] = findSet(p[v])
        ans = p[v]
    return ans

def unionSet(u, v):
    u, v = findSet(u), findSet(v)
    if u != v:
        if rango[u] < rango[v]:
            u, v = v, u
        p[v] = u
        if rango[u] == rango[v]:
            rango[u] += 1

def kruskal(n, grafo, receiver):
  for i in range(1, n + 1): makeSet(i)
  grafo.sort(key = lambda x: x[2])
  mst = []
  it = 0

  while(it != n and len(mst) != receiver):
    u, v, c = grafo[it]

    if findSet(u) != findSet(v):
      unionSet(u, v)
      mst.append(grafo[it])
    it+=1
  return mst[receiver-1][2]

def dist(A, B):
  return math.ceil(math.sqrt(((B[0] - A[0]) * (B[0] - A[0])) + ((B[1] - A[1]) * (B[1] - A[1]))))

def main():
  C = int(stdin.readline())
  for _ in range(C):
    sensors = []
    grafo = []
    receiver = int(stdin.readline())
    data = list(map(int, stdin.readline().split()))
    while(data[0] != -1):
      sensors.append((data[0], data[1]))
      data = list(map(int, stdin.readline().split()))
    
    for i in range(1, len(sensors) + 1):
       for j in range(i+1, len(sensors) + 1):
          if(i != j):
            grafo.append((i, j, dist(sensors[i-1], sensors[j-1])))
          
    print(kruskal(len(grafo), grafo, len(sensors) - receiver))

main()

#print(len([(16, 57, 62), (15, 69, 215), (12, 72, 232), (1, 82, 254), (20, 98, 301), (59, 100, 324), (86, 95, 365), (28, 52, 454), (10, 21, 515), (32, 92, 526), (5, 73, 549), (42, 45, 591), (34, 39, 661), (41, 60, 667), (12, 67, 677), (7, 83, 687), (4, 56, 698), (31, 65, 700), (16, 81, 701), (11, 61, 737), (8, 25, 787), (70, 79, 792), (53, 76, 812), (24, 88, 842), (2, 97, 888), (46, 78, 888), (17, 64, 933), (35, 88, 973), (33, 49, 1022), (27, 43, 1082), (19, 43, 1116), (53, 58, 1116), (81, 94, 1116), (6, 68, 1126), (23, 43, 1139), (67, 69, 1198), (48, 51, 1277), (16, 27, 1324), (9, 47, 1366), (31, 63, 1373), (18, 28, 1378), (23, 89, 1382), (13, 51, 1410), (47, 74, 1410), (38, 64, 1416), (18, 89, 1449), (13, 62, 1454), (32, 50, 1458), (44, 93, 1493), (10, 90, 1538), (27, 48, 1539), (61, 91, 1551), (44, 91, 1595), (25, 38, 1622), (24, 30, 1646), (35, 68, 1701), (14, 29, 1747)]))
#Juan Miguel Rojas Mejía
#8963761

from sys import stdin
import math

p, rango = [0 for _ in range(1000001)], [0 for _ in range(1000001)]

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
       for j in range(i, len(sensors) + 1):
          if(i != j):
            grafo.append((i, j, dist(sensors[i-1], sensors[j-1])))
    
    print(kruskal(len(grafo), grafo, len(sensors) - receiver))

main()
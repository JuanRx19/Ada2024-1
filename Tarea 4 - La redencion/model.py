#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

p, rango = [0 for _ in range(201)], [0 for _ in range(201)]

def dfs(G):
  vis = [False for _ in range(len(G))]
  color = [0 for _ in range(len(G))]
  colorSelect = -1
  for i in range(1, len(G)):
    if not vis[i]:
      ans = dfsAux(i, G, vis, color, colorSelect)
  
  return ans

def dfsAux(u, G, vis, color, colorSelect):
  ans = False
  vis[u] = True
  color[u] = -colorSelect
  #print(f"visting %d y vecinos {G[u]}" % u)
  for v in G[u]:
    if not vis[v]:
      ans = dfsAux(v, G, vis, color, -colorSelect)
    elif(color[v] == color[u]):
      ans = True

  return ans
      
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

def kruskal(n, grafo):
  for i in range(1, n + 1): makeSet(i)
  grafo.sort(key = lambda x: x[2])
  mst = []
  ans = 0

  for it in grafo:
    u, v, c = it

    if findSet(u) != findSet(v):
      unionSet(u, v)
      mst.append(it)
      ans+= it[2]
    elif(it[2] < 0):
      ans+= it[2]
  return ans

def main():
  N = int(stdin.readline())
  while(N != 0):
    M = int(stdin.readline())
    grafocheck = [ list() for _ in range(N + 1) ]
    grafo = []
    for _ in range(1, M+1):
      v1, v2, arista = map(int, stdin.readline().split())
      grafocheck[v1].append(v2)
      grafocheck[v2].append(v1)
      grafo.append([v1, v2, arista])
    
    if(dfs(grafocheck)):
      print("Invalid data, Idiot!")
    else:
      print(kruskal(N, grafo))
    #bfs([[3, 1, 2], [0, 2, 4, 5], [3, 4], [4, 1], [5, 0], [1, 2]])
    N = int(stdin.readline())

main()
#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

def sortgrafo(grafo):
  i = 1
  while(i < 24):
    grafo[i].sort()
    i+=1
  return grafo

def dfs(G):
  vis = [False for _ in range(len(G))]
  if not vis[1] and len(G[1]) != 0:
    vis = dfsAux(1, G, vis)
  
  return vis

def dfsAux(u, G, vis):
  vis[u] = True
  #print(f"visting %d y vecinos {G[u]}" % u)
  for v in G[u]:
    if not vis[v]:
      vis = dfsAux(v, G, vis)
  return vis

def solve(grafo, visdfs, end, nodo, data, vis, ans):
  #print(data)
  if(nodo == end):
    ans+=1
    for i in range(len(data) - 1):
      print(data[i], end=" ")
    print(data[len(data) - 1])
  else:
    i = 0
    while(i != len(grafo[nodo])):
      #print(not(vis[grafo[nodo][i]]) and visdfs[grafo[nodo][i]])
      if(not(vis[grafo[nodo][i]]) and visdfs[grafo[nodo][i]]):
        data.append(grafo[nodo][i])
        vis[grafo[nodo][i]] = True
        ans = solve(grafo, visdfs, end, grafo[nodo][i], data, vis, ans)
        vis[grafo[nodo][i]] = False
        data.pop()
      i+=1
  return ans

def main():
  count = 1
  C = stdin.readline().strip()
  while(C != ""):
    grafo = [ list() for _ in range(24) ]
    origen, destino = map(int, stdin.readline().split())
    while(origen != 0 and destino != 0):
      grafo[origen].append(destino)
      grafo[destino].append(origen)
      origen, destino = map(int, stdin.readline().split())
    #print(grafo)
    vis = [False for _ in range(len(grafo))]
    vis[1] = True
    visdfs = dfs(grafo)
    grafo = sortgrafo(grafo)
    print(f"CASE {count}:")
    ans = solve(grafo, visdfs, int(C), 1, [1], vis, 0)
    print(f"There are {ans} routes from the firestation to streetcorner {C}.")
    count+=1
    C = stdin.readline().strip()

main()
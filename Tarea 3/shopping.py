#Juan Miguel Rojas
#8963761

from sys import stdin
from heapq import heappush,heappop

INF = float('inf')
def dijkstra(G, s):
  ans = [ INF for _ in G ] ; ans[s] = 0
  prev = [ None for _ in G ]
  visited = [ False for _ in G ]
  heap = [ (0, s) ]
  while len(heap)!=0:
    d,u = heappop(heap)
    if visited[u]==False:
      for v,dv in G[u]:
        if d+dv<ans[v]:
          ans[v] = d+dv
          heappush(heap, (ans[v], v))
          prev[v] = u
      visited[u] = True
  return ans

def universe(N): return (1<<N)-1
def is_elt(n, X): return (X|(1<<n))==X
def remove_elt(n, X): return X-(1<<n) if is_elt(n, X) else X
def singleton(n, X): return X==(1<<n)
def phi_memo(N, w, u, X, mem):
    ans,key = None,(u,X)
    if key in mem: ans = mem[key]
    else:
        if not(is_elt(u, X)): ans = INF
        elif singleton(u, X): ans = w[0][u]
        else:
            ans,Y = INF,remove_elt(u, X)
            for v in range(1, N):
                if is_elt(v, Y):
                    ans = min(ans, phi_memo(N, w, v, Y, mem)+w[v][u])
    mem[key] = ans
    return ans

def tsp(N, w):
    ans = INF
    X = remove_elt(0, universe(N))
    mem = dict()
    for u in range(1, N):
        ans = min(ans, phi_memo(N, w, u, X, mem)+w[u][0])
    return ans

def solve(G, shops):
    dijksGrafo = []
    updateGrafo = []
    iter = 0
    for shop in shops:
        dijksGrafo.append(dijkstra(G, shop))
        updateGrafo.append([])
        for select in shops:
            updateGrafo[len(updateGrafo)-1].append(dijksGrafo[iter][select])
        iter+=1
    print(updateGrafo)
    return tsp(len(updateGrafo),updateGrafo)

def main():
    C = int(stdin.readline())
    while(C != 0):
        N, M = map(int, stdin.readline().split())
        G = [ list() for _ in range(N) ]
        shops = [0]
        for _ in range(M):
            o, d, p = map(int, stdin.readline().split())
            G[o].append((d, p))
            G[d].append((o, p))
        shopping = int(stdin.readline())
        for _ in range(shopping):
            shops.append(int(stdin.readline()))
        print(solve(G, shops))
        C-=1
    

main()
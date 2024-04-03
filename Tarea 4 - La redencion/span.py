#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

p, rango = [0 for _ in range(100)], [0 for _ in range(100)]

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

def kruskal(n, aristas, start):
    for i in range(1, n + 1): makeSet(i)
    mst = []
    flag = 0
    while(start != len(aristas)-1 and flag == 0):
        u, v, c = aristas[start]
        if findSet(u) != findSet(v):
            unionSet(u, v)
            mst.append(aristas[start])
        
        if(len(mst) == n-1):
            flag = 1
        start+=1
    """for it in range(start, len(aristas)-1):
        u, v, c = aristas[it]
        if findSet(u) != findSet(v):
            unionSet(u, v)
            mst.append(aristas[it])"""
    print(mst)
    return mst

def solve(n, k, grafo):
    ans = float('inf')
    grafo.sort(key = lambda x: x[2])
    start = 0
    flag = 0
    while(flag == 0):
        mst = kruskal(n, grafo, start)
        if(len(mst) < n-1):
            flag = 1
        else:
            ans = min(ans, mst[len(mst)-1][2] - mst[0][2])
            start+=1
    #print(mst)
    if(ans == float('inf')):
        ans = -1
    return ans

def main():
    n, k = map(int, stdin.readline().split())
    while(n != 0):
        grafo = []
        for _  in range(k):
            v1, v2, arista = map(int, stdin.readline().split())
            grafo.append([v1, v2, arista])
        if(k == 0):
            print("-1")
        else:
            print(solve(n, k, grafo))
        n, k = map(int, stdin.readline().split())

main()
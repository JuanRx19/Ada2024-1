#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

def makeSet(v, p, rango):
    p[v], rango[v] = v, 0

def findSet(v, p, rango):
    ans = None
    if v == p[v]:
        ans = v
    else:
        p[v] = findSet(p[v], p, rango)
        ans = p[v]
    return ans

def unionSet(u, v, p,  rango):
    u, v = findSet(u, p, rango), findSet(v, p, rango)
    if u != v:
        if rango[u] < rango[v]:
            u, v = v, u
        p[v] = u
        if rango[u] == rango[v]:
            rango[u] += 1

def kruskal(n, aristas, start, p, rango):
    for i in range(1, n + 1): makeSet(i, p, rango)
    mst = []
    for it in range(start, len(aristas)-1):
        u, v, c = aristas[it]
        if findSet(u, p, rango) != findSet(v, p, rango):
            unionSet(u, v, p, rango)
            mst.append(aristas[it])
    return mst

def solve(n, k, grafo, p, rango):
    ans = float('inf')
    grafo.sort(key = lambda x: x[2])
    start = 0
    flag = 0
    while(flag == 0):
        mst = kruskal(n, grafo, start, p, rango)
        if(len(mst) < n-1):
            flag = 1
        else:
            ans = min(ans, mst[len(mst)-1][2] - mst[0][2])
            start+=1
        k-=1
    #print(mst)
    if(ans == float('inf')):
        ans = -1
    return ans

def main():
    n, k = map(int, stdin.readline().split())
    p, rango = [0 for _ in range(100)], [0 for _ in range(100)]
    while(n != 0):
        grafo = []
        for _  in range(k):
            v1, v2, arista = map(int, stdin.readline().split())
            grafo.append([v1, v2, arista])
        if(k == 0):
            print("-1")
        else:
            print(solve(n, k, grafo, p, rango))
        n, k = map(int, stdin.readline().split())

main()
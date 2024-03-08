from sys import stdin

"""def main():
    pass

main()"""
def universe(N): return (1<<N)-1
def is_elt(n, X): return (X|(1<<n))==X
def remove_elt(n, X): return X-(1<<n) if is_elt(n, X) else X
def singleton(n, X): return X==(1<<n)

INF = float('inf')
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

w = [[ 0, 6, 7, 6 ],
    [ 6, 0, 8, 8 ],
    [ 7, 8, 0, 7 ],
    [ 6, 8, 7, 0 ]]

print(tsp(4, w))
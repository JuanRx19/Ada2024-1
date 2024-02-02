from sys import stdin

def build(A, tree, l, r, v):
    if l == r:
        tree[v] = int(A[l])
    else:
        mid = l + ((r - l) >> 1)
        build(A, tree, l, mid, v + 1)
        build(A, tree, mid + 1, r, v + 2 * (mid - l + 1))
        tree[v] = tree[v + 1] + tree[v + 2 * (mid - l + 1)]

def construir_str(M):
    str = ""
    cont = 0
    cont2 = 0
    C = int(stdin.readline())
    P  = stdin.readline().strip()
    while(cont != M):
        str += P
        cont2+=1
        if(cont2 == C):
            cont+=1
            cont2 = 0
            if(cont != M):
                C = int(stdin.readline())
                P  = stdin.readline().strip()
    
    return list(map(int, str))

def sum(tree, L, R, l, r, v):
    ans = None
    if l > r: ans = 0
    elif l == L and r == R: ans = tree[v]
    else:
        m = L + ((R - L) >> 1)
        ans = sum(2 * v + 1, L, m, l, min(r, m)) + sum(2 * (v + 1), m + 1, R, max(l, m + 1), r)
    return ans

def solve(A):
    #tree = [0] * 2*len(A)
    #build(A, tree, 0, len(A)-1, 0)
   #print(tree)
    opc = int(stdin.readline())
    for _ in range(opc):
        ele, i, j = stdin.readline().split()
    print(ele, i, j)


def main():
    T = int(stdin.readline())
    cont = 0
    while(cont != T):            
        M = int(stdin.readline())
        solve(construir_str(M))
        cont += 1

print(7//2)
#print(solve([1, 2]))
#main()
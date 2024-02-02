from sys import stdin

def solve(M):
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
    print(str)
#solve(2)

#A = [10, 8, 1, 4, 3, 6, 7, 9, 3, 4, 8, 2]
#A = [2, 3, 5, 6, 8, 1, 4, 10, 5, 3]
A = [1, 2, 3, 4, 5, 6]

def build(A, tree, l, r, v):
    if l == r:
        tree[v] = A[l]
    else:
        mid = l + ((r - l) >> 1)
        build(A, tree, l, mid, v + 1)
        build(A, tree, mid + 1, r, v + 2 * (mid - l + 1))
        tree[v] = tree[v + 1] + tree[v + 2 * (mid - l + 1)]

def mostrar(A, tree, l, r, v):
    if l == r:
        if(l > 2):
            print(tree[v])
    else:
        mid = l + ((r - l) >> 1)
        mostrar(A, tree, l, mid, v + 1)
        mostrar(A, tree, mid + 1, r, v + 2 * (mid - l + 1))

tree = [0] * 2*len(A)
build(A, tree, 0, len(A)-1, 0)
mostrar(A, tree, 0, len(A)-1, 0)
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

def sum(tree, v, L, R, l, r):
    ans = None
    if l > r:
        ans = 0
    elif l == L and r == R:
        ans = tree[v]
    else:
        mid = L + ((R - L) >> 1)
        ans = sum(tree, v + 1, L, mid, l, min(r, mid)) + sum(tree, v + 2 * (mid - L + 1), mid + 1, R, max(l, mid + 1), r)
    return ans

def update(v, L, R, l, r, h):
    if l <= r:
        if l == L and r == R: tree[v] += h
        else:
            m = L + ((R - L) >> 1)
            update(v + 1, L, m, l, min(r, m), h)
            update(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r, h)


tree = [0] * 2*len(A)
build(A, tree, 0, len(A)-1, 0)
update(0, 0, len(A)-1, 1, 4, 1)
#update_2(0, 0, len(A)-1, 0, len(A)-1)
#print(sum(tree, 0, 0, len(A)-1, 1, 4))
#update_2(A, tree, 2, 4, 0, len(A)-1, 0, 0)
print(tree[0])
from sys import stdin

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

def build(A, tree, l, r, v):
    if l == r:
        tree[v] = int(A[l])
    else:
        mid = l + ((r - l) >> 1)
        build(A, tree, l, mid, v + 1)
        build(A, tree, mid + 1, r, v + 2 * (mid - l + 1))
        tree[v] = tree[v + 1] + tree[v + 2 * (mid - l + 1)]
    return tree

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

def update(tree, v, L, R, left, right, h):
    if L == R:
        tree[v] = h
    else:
        mid = L + ((R - L) >> 1)
        if left <= mid:
            update(tree, v + 1, L, mid, left, right, h)
        if right > mid:
            update(tree, v + 2 * (mid - L + 1), mid + 1, R, left, right, h)
        tree[v] = tree[v + 1] + tree[v + 2 * (mid - L + 1)]
    return tree

def update_2(tree, v, L, R, left, right):
    if L == R:
        if(tree[v] == 1):
            tree[v] = 0
        else:
            tree[v] = 1
    else:
        mid = L + ((R - L) >> 1)
        if left <= mid:
            update_2(tree, v + 1, L, mid, left, right)
        if right > mid:
            update_2(tree, v + 2 * (mid - L + 1), mid + 1, R, left, right)
        tree[v] = tree[v + 1] + tree[v + 2 * (mid - L + 1)]
    return tree

def solve(A):
    Q = 0
    tree = [0] * 2*len(A)
    tree = build(A, tree, 0, len(A)-1, 0)
    opc = int(stdin.readline())
    for _ in range(opc):
        ele, i, j = stdin.readline().split()
        i = int(i)
        j = int(j)
        if(ele == "F"):
            tree = update(tree, 0, 0, len(A)-1, i, j, 1)
        elif(ele == "E"):
            tree = update(tree, 0, 0, len(A)-1, i, j, 0)
        elif(ele == "I"):
            tree = update_2(tree, 0, 0, len(A)-1, i, j)
        else:
            print(f"Q{Q+1}: {sum(tree, 0, 0, len(A)-1, i, j)}")
            Q+=1


def main():
    T = int(stdin.readline())
    cont = 0
    while(cont != T):            
        M = int(stdin.readline())
        print(f"Case {cont+1}:")
        solve(construir_str(M))
        cont += 1

main()
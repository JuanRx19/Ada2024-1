from sys import stdin

def build(A, tree, l, r, v):
    if l == r:
        tree[v] = int(A[l])
    else:
        mid = l + ((r - l) >> 1)
        build(A, tree, l, mid, v + 1)
        build(A, tree, mid + 1, r, v + 2 * (mid - l + 1))
        tree[v] = tree[v + 1] + tree[v + 2 * (mid - l + 1)]
    return tree

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

def update_1(A, tree, L, R, l, r, v):
    if l == r:
        if(l >= L and r <= R):
            if(tree[v] == 0):
                tree[v] = 1
            elif(tree[v] == 1):
                tree[v] = 0
    else:
        mid = l + ((r - l) >> 1)
        update_1(A, tree, L, R, l, mid, v + 1)
        update_1(A, tree, L, R, mid + 1, r, v + 2 * (mid - l + 1))
        tree[v] = tree[v + 1] + tree[v + 2 * (mid - l + 1)]
    return tree

def update_2(A, tree, L, R, l, r, v, h):
    if l == r:
        if(l >= L and r <= R):
            tree[v] = h
    else:
        mid = l + ((r - l) >> 1)
        update_2(A, tree, L, R, l, mid, v + 1, h)
        update_2(A, tree, L, R, mid + 1, r, v + 2 * (mid - l + 1), h)
        tree[v] = tree[v + 1] + tree[v + 2 * (mid - l + 1)]
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
            tree = update_2(A, tree, i, j, 0, len(A)-1, 0, 1)
        elif(ele == "E"):
            tree = update_2(A, tree, i, j, 0, len(A)-1, 0, 0)
        elif(ele == "I"):
            tree = update_1(A, tree, i, j, 0, len(A)-1, 0)
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
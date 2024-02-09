"""
Segment Tree Implementation
Carlos Ramírez
Noviembre 7 de 2020

"""

#Segment tree is represented as a list
n, MAXN = int(), 1000
tree = [0 for _ in range(MAXN * 2)]

#build the segment tree
def build(a, v, l, r):
    if l == r: tree[v] = a[l]
    else:
        mid = l + ((r - l) >> 1)
        build(a, v + 1, l, mid)
        build(a, v + 2 * (mid - l + 1), mid + 1, r)
        tree[v] = tree[v + 1] + tree[v + 2 * (mid - l + 1)]

#sum query
def sum(v, L, R, l, r):
    ans = None
    if l > r: ans = 0
    elif l == L and r == R: ans = tree[v]
    else:
        m = L + ((R - L) >> 1)
        ans = sum(v + 1, L, m, l, min(r, m)) + sum(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r)
    return ans

#update query
def update(v, L, R, pos, h):
    if L == R: tree[v] = h
    else:
        mid = L + ((R - L) >> 1)
        if pos <= mid:
            update(v + 1, L, mid, pos, h)
        else:
            update(v + 2 * (mid - L + 1), mid + 1, R, pos, h)
        tree[v] = tree[v + 1] + tree[v + 2 * (mid - L + 1)]

        
build([1, 2, 3, 4, 5, 6], 0, 0, 5)
"""for i in range(14):
    print(str(tree[i]) + " ", end = '')
print()"""

#build(list(map(int, "000000111111111111")), 0, 0, 17)
print(tree)
print(sum(0, 0, 17, 1, 10))
#print(sum(0, 0, 6, 0, 4))
update(0, 0, 5, 0, 7)
"""for i in range(14):
    print(str(tree[i]) + " ", end = '')"""
print()

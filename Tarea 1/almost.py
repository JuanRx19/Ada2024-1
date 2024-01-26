def find(d, p):
    ans = 0
    if(d[p][0] == p):
        ans = p
    else:
        ans = find(d, d[p][0])
        d[p][0] = ans
    return ans

def union(d, p, q):
    padre = find(d, d[p][0])
    hijo = find(d, d[q][0])
    d[hijo][0] = padre
    d[padre][1] += d[hijo][1]
    return d

def move(d, p, q):
    padre = find(d, d[p][0])
    hijo = find(d, d[q][0])
    if(padre == hijo):
        ans = d
    else:
        for num in d:
            find(d, num)
        d[p][0] = hijo
        d[padre][1] -= p
        d[hijo][1] += p
        ans = d

    return ans

def solve():
    pass

def main():
    d = {1:[1, 13], 5:[1, 12], 7:[5, 7], 2:[2, 29], 8:[2, 27], 9:[8, 19], 10:[9, 10]}
    d = move(d, 9, 7)
    d = move(d, 2, 9)
    print(d)

main()
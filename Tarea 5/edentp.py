def cell(id, left, middle, right):
    v = id & (1 << ((left << 2) | (middle << 1) | right))
    if v:
        #print("Entra", v, id, (1 << ((left << 2) | (middle << 1) | right)))
        return 1
    #print("Fuera", v, id, (1 << ((left << 2) | (middle << 1) | right)))
    return 0

def debug(p, a):
    print(''.join(map(str, p)))
    print(''.join(map(str, a)))

def searchR(k, id, n, a):
    global cnt
    if cnt:
        #print(p, cnt)
        return
    if k == n:
        #debug(p, a)
        if cell(id, p[n - 2], p[n - 1], p[0]) != a[n - 1]:
            return
        if cell(id, p[n - 1], p[0], p[1]) != a[0]:
            return
        print(p, a)
        cnt += 1
        return
    for i in range(2):
        p[k] = i
        #print(p, k, p[k])
        if k >= 2 and cell(id, p[k - 2], p[k - 1], p[k]) != a[k - 1]:
            #print(k, p, k - 2, k - 1, k)
            continue
        searchR(k + 1, id, n, a)

def reachable(id, n, a):
    global cnt
    cnt = 0
    searchR(0, id, n, a)
    if cnt:
        #print(cnt)
        return True
    else:
        return False

if __name__ == "__main__":
    while True:
        try:
            line = input().split()
            id = int(line[0])
            n = int(line[1])
            s = line[2]
            a = [int(x) for x in s]
            p = [0] * n
            if reachable(id, n, a):
                print("REACHABLE")
            else:
                print("GARDEN OF EDEN")
        except EOFError:
            break
a = [1, 0, 1, 0, 1]
p = [1, 1, 1, 0, 0]
k = 2
#print(cell(204, p[k - 2], p[k - 1], p[k]), a[k-1])
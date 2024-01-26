def union(d, x, y):
    if d[x][1] >= d[y][1]:
        d[y][0] = x
        d[x][1] = d[x][1] + 1
        d[x][2] = d[x][2] + y
    else:
        d[x][0] = y
        if d[x][1] == d[y][1]:
            d[y][1] = d[y][1] + 1
            d[y][2] = d[y][2] + y
    return d

d = {1:[1, 1], 2:[2, 2], 3:[3, 3], 4:[4, 9], 5:[4, 5]}

for i in d:
    print(i)
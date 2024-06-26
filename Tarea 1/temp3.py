from sys import stdin

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

#d = {1:[1, 1], 2:[2, 2], 3:[3, 3], 4:[4, 9], 5:[4, 5]}
#d = {1:[1, 8], 2:[2, 7], 3:[1, 7], 4:[1, 4], 5:[2, 5]}
#d = {1:[1, 13], 5:[1, 12], 7:[5, 7], 2:[2, 29], 8:[2, 27], 9:[8, 19], 10:[9, 10]}
#d = {1:[1, 13], 5:[1, 12], 7:[1, 7], 8:[15, 27], 9:[1, 19], 10:[15, 10], 11:[15, 10], 15:[15, 10]}
#d = move(d, 9, 7)
#d = move(d, 2, 9)
#d = move(d, 15, 9)
#d = move(d, 5, 3)
#print(d)
n = 5
d = {}
for num in range(1, n+1):
    d[num] = [n+num]

for num in range(n+1, (n*2)+1):
    d[num] = [num, num-n, 1]

print(len(d))
"""for i in d:
    print(i)"""
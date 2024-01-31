from sys import stdin

def find(d, p):
    ans = 0
    tam = len(d)
    if(d[p][0] == tam * p):
        ans = p
    else:
        ans = find(d, d[p][0])
        d[p][0] = ans
    return ans

def union(d, p, q):
    padre = find(d, d[p][0])
    hijo = find(d, d[q][0])
    if(padre != hijo):
        d[hijo][0] = padre
        d[padre][1] += d[hijo][1]
        d[padre][2] += d[hijo][2]
        d[hijo][1] = d[padre][1]
    return d

def move(d, p, q):
    padre = find(d, d[p][0])
    hijo = find(d, d[q][0])
    flag = 0
    if(padre == hijo):
        ans = d
    else:
        if(d[p][0] == p):
            nuevo_padre = 1
            for num in d:
                find(d, num)
                if(d[num][0] == p and num != d[num][0] and flag == 0):
                    nuevo_padre = num
                    d[num][1] = d[p][1] - p
                    d[num][2] = d[p][2] - 1
                    flag = 1
                if(d[num][0] == p and num != d[num][0]):
                    d[num][0] = nuevo_padre
        else:
            for num in d:
                find(d, num)
        d[p][0] = hijo
        d[padre][1] -= p
        d[padre][2] -= 1
        d[hijo][1] += p
        d[hijo][2] += 1
        ans = d

    return ans

def solve(n, m):
    d = {}
    for num in range(1, n+1):
        d[num] = [num, num, 1]
    for _ in range(m):
        opc = list(map(int, stdin.readline().split()))
        if(opc[0] == 1):
            d = union(d, opc[1], opc[2])
        elif(opc[0] == 2):
            d = move(d, opc[1], opc[2])
        elif(opc[0] == 3):
            print(f"{d[find(d, opc[1])][2]} {d[find(d, opc[1])][1]}")
            
def main():
    line = stdin.readline().strip()
    while(line != ""):
        n, m = map(int, line.split())
        solve(n, m)
        line = stdin.readline().strip()

main()
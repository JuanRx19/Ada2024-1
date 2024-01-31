from sys import stdin

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
    if(padre != hijo):
        d[q][0] = padre
        d[hijo][0] = padre
        d[padre][1] += d[hijo][1]
        d[padre][2] += d[hijo][2]
    return d

def move(d, p, q):
    padre = find(d, d[p][0])
    hijo = find(d, d[q][0])
    if(padre == hijo):
        ans = d
    else:
        d[p][0] = hijo
        d[hijo][1] += p
        d[padre][1] -= p
        d[hijo][2] += 1
        d[padre][2] -= 1
        ans = d

    return ans

def solve(n, m):
    d = {}
    for num in range(1, n+1):
        d[num] = [n+num]

    for num in range(n+1, (n*2)+1):
        d[num] = [num, num-n, 1, 1]

    for _ in range(m):
        opc = list(map(int, stdin.readline().split()))
        if(opc[0] == 1):
            d = union(d, opc[1], opc[2])
        elif(opc[0] == 2):
            d = move(d, opc[1], opc[2])
        elif(opc[0] == 3):
            ans = find(d, opc[1])
            print(f"{d[ans][2]} {d[ans][1]}")
            
def main():
    line = stdin.readline().strip()
    while(line != ""):
        n, m = map(int, line.split())
        solve(n, m)
        line = stdin.readline().strip()

main()
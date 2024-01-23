from sys import stdin
import heapq

def solve(n, k):
    med = []
    tobby = []
    suma = []
    for i in range(n):
        m, t = stdin.readline().split()
        suma.append(int(t))
        med.append((int(t), i, m))

    iterator = 0
    for cases in range(k):
        if(iterator < n):
            heapq.heappush(tobby, (suma[iterator], med[iterator][1], med[iterator][2]))
            suma[iterator]+=med[iterator][0]
            iterator+=1
        else:
            heapq.heappush(tobby, (suma[iterator-1], med[iterator-1][1], med[iterator-1][2]))
            suma[iterator-1]+=med[iterator-1][0]
            iterator = 0 #El problema sigue aquí
    
    for _ in range(k):
        desapel = heapq.heappop(tobby)
        print(str(desapel[0]) + " " + desapel[2])

def main():
    T = int(stdin.readline())
    while(T>=1):            
        n, k = map(int, stdin.readline().split())
        solve(n, k)
        T = T - 1

main()
#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

"""def binarysearch(dividendo, low, hi, x):
    ans = 0
    if(low == hi):
        ans = x << low, 1 << low
    elif(low+1 == hi):
        ans = x << low, 1 << low
    else:
        mid = low + ((hi-low)>>1)
        if(x << mid <= dividendo):
            ans = binarysearch(dividendo, mid, hi, x)
        else:
            ans = binarysearch(dividendo, low, mid, x)
    return ans"""

"""def division(dividendo, divisor):
    cociente = 0
    while(dividendo >= divisor):
        potencia = 0
        while(divisor << potencia <= dividendo):
            potencia+=1
        potencia -= 1
        cociente += 1 << potencia
        dividendo -= divisor << potencia
    return cociente"""

def solve(P, N, A):
    A.sort(key=lambda x: (x[0], -x[1]))
    cont = 0
    for i in range(len(A)):
        cont = P//N
        if cont < A[i][0]:
            A[i][0] = cont
        P -= A[i][0]
        N -= 1
    A.sort(key=lambda x: x[1])
    return A

def main():
    C = int(stdin.readline())
    A = []
    while C != 0:
        total = 0
        P, N = map(int, stdin.readline().split())
        A = list(map(int, stdin.readline().split()))

        for i in range(len(A)):
            total += A[i]
            A[i] = [A[i], i]
            
        if total >= P:
            A = solve(P, N, A)
            for i in range(len(A)):
                if len(A) - 1 != i:
                    print(A[i][0], end=" ")
                else:
                    print(A[i][0])
        else:
            print("IMPOSSIBLE")
        C -= 1

main()

#val = 150140 >> 6
#print(val)
#val += 150140 >> 4
#print(val)
#val += 150140 >> 3
#print(val)
#val += 150140 >> 1
#print(f"Division prueba: {val}")
#print(f"Division original: {150140 // 90}")
#resultado = (i >> 6)
#resultado += (i >> 200)
#print(resultado)
#print(division(150140, 90))
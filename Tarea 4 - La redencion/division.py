#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

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
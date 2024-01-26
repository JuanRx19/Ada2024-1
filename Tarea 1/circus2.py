from sys import stdin

def solve(N, H, Ta, Td):
    hippo = list(map(int, input().split()))
    hippo.sort()
    pasan = []
    time = 0
    cont = 0
    while(len(hippo) != 0 and time < N * Ta):
        cont = 0
        pasan = []
        for num in range(len(hippo)-1, -1, -1):
            if cont + hippo[num] < H and len(pasan) < 2:
                pasan.append(hippo[num])
                cont += hippo[num]  
                hippo.pop(num)
        if(len(pasan) == 1):
            time += Ta
        else:
            time += Td
    if(time > N * Ta):
        time = N * Ta
    return time

def main():
    T = int(stdin.readline())
    cont = 0
    while(cont != T):            
        N, H, Ta, Td = map(int, stdin.readline().split())
        print(f"Case {cont+1}: {solve(N, H, Ta, Td)}")
        cont += 1

main()
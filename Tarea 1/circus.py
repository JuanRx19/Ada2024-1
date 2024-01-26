from sys import stdin

def solve(N, H, Ta, Td):
    hippo = list(map(int, input().split()))
    hippo.sort()
    time = 0
    iter = 0
    while(len(hippo) > 1):
        ver = hippo.pop(len(hippo)-1)
        if(ver + hippo[0] < H):
            hippo.pop(0)
            time+=Td
        else:
            time+=Ta
        iter+=1
    if(len(hippo) == 1):
        time+=Ta
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
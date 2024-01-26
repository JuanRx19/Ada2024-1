from sys import stdin

def solve(N, H, Ta, Td):
    hippo = list(map(int, input().split()))
    hippo.sort()
    time = 0
    iter = 0
    while(iter < len(hippo)-1):
        ver = hippo.pop(len(hippo)-1)
        if(ver + hippo[iter] < H):
            time+=Td
            iter+=1
        else:
            time+=Ta
    if(len(hippo)-1 == iter):
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
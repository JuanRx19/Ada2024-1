from sys import stdin

def mergesort(A, low, hi):
    if low+1<hi:
        mid = low+((hi-low)>>1) # mid = (low+hi)//2
        mergesort(A, low, mid) # induction hypothesis on the first half
        mergesort(A, mid, hi) # induction hypothesis on the second half
        merge(A, low, mid, hi)

def merge(A, low, mid, hi):
    global tmp # a global array at least the size of A
    for i in range(low, hi): tmp[i] = A[i] # copy A[low..hi) to tmp[low..hi)
    l,r = low,mid
    for n in range(low, hi):
        if l==mid: A[n],r = tmp[r],r+1 # only process the right half
        elif r==hi: A[n],l = tmp[l],l+1 # only process the left half
        else:
            # the first pending element of each half needs to be compared
            if tmp[l]<=tmp[r]: A[n],l = tmp[l],l+1 # choose the one on the left
            else: A[n],r = tmp[r],r+1 # choose the one on the right

def solve(N, H, Ta, Td):
    hippo = list(map(int, input().split()))
    mergesort(hippo, 0, len(hippo))
    pasan = []
    time = 0
    cont = 0
    while(len(hippo) != 0):
        cont = 0
        pasan = []
        for num in range(len(hippo)-1, -1, -1):
            if cont + hippo[num] < H and len(pasan) < 2:
                pasan.append(hippo[num])
                cont += hippo[num]
                hippo.remove(hippo[num])
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

tmp = [ None for _ in range(10) ]
main()
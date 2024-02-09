from sys import stdin

def binarysearchleft(A, low, high, x):
    ans = 0
    if low+1 == high:
        if(A[low] == x):
            ans = 1
    else:
        mid = low + ((high-low)>>1)
        if(A[mid] == x):
            ans = ((high - mid)) + binarysearchleft(A, low, mid, x)
        else:
            ans = binarysearchleft(A, mid, high, x)
    
    return ans

def binarysearchright(A, low, high, x):
    ans = 0
    if low+1 == high:
        if(A[high] == x):
            ans = 1
    else:
        mid = low + ((high-low)>>1)
        if(A[mid] == x):
            ans = ((mid - low)) + binarysearchright(A, mid, high, x)
        else:
            ans = binarysearchright(A, low, mid, x)
    
    return ans

def solve(tam, val):
    ans = 0
    mid = 0 + (((len(val) - 1) - 0)>>1)
    if(tam > 2):
        if(tam % 2 != 0):   
            ans += binarysearchleft(val, 0, mid, val[mid])
            ans += binarysearchright(val, mid, len(val) - 1, val[mid])
            print(f"{val[mid]} {ans + 1} 1")
        else:
            ans += 1 + binarysearchleft(val, 0, mid, val[mid])
            ans += 1 + binarysearchright(val, mid + 1, len(val) - 1, val[mid + 1])
            print(f"{val[mid]} {ans} {val[mid + 1] - val[mid] + 1}")
        
    else:
        if(tam == 1):
            print(f"{val[mid]} 1 1")
        else:
            print(f"{val[mid]} 2 {val[mid + 1] - val[mid] + 1}")

def main():
    tam = stdin.readline().strip()
    while(tam != ""):
        v = []
        for _ in range(int(tam)):
            v.append(int(stdin.readline()))
        v.sort()
        solve(int(tam), v)
        tam = stdin.readline().strip()

main()
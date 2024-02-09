from sys import stdin

def solve(tam, val):
    ans = 0
    mid = 0 + (((len(val) - 1) - 0)>>1)
    if(tam > 2):
        if(tam % 2 != 0):
            for i in range(tam):
                if(val[i] == val[mid]):
                    ans+=1
            print(f"{val[mid]} {ans} 1")
        else:
            for i in range(tam):
                if(val[i] == val[mid] or val[i] == val[mid + 1]):
                    ans+=1
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
        
#print(1 + binarysearch([5, 5], 0, 1, 5))
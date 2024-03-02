"""def power(x, y):
    ans = 0
    temp = 0
    if(y == 0):
        ans = 1
    else:
        print(int(y / 2))
        temp = power(x, int(y / 2))
        print("d", temp)
        if(y % 2 == 0):
            ans = temp * temp
        else:
            ans = x * temp * temp
    
    return ans

print(power(3, 5))"""


"""def obtainFirst(A, low, hi, x):
    ans = 0
    if(low < hi):
        ans = 0
    elif(low+1 == hi):
        pass"""

def mergesort(A, low, hi):
    if low+1<hi:
        mid = low+((hi-low)>>1) # mid = (low+hi)//2
        mergesort(A, low, mid) # induction hypothesis on the first half
        mergesort(A, mid, hi) # induction hypothesis on the second half
        merge(A, low, mid, hi) # combine the two halves preserving the order
 
def merge(A, low, mid, hi):
    global tmp # a global array at least the size of A
    for i in range(low, hi):
        tmp[i] = A[i] # copy A[low..hi) to tmp[low..hi)
    l,r = low,mid
    for n in range(low, hi):
        if l==mid:
            A[n] = tmp[r]# only process the right half
            r  = r + 1
        elif r==hi: 
            A[n] = tmp[l]# only process the left half
            l = l + 1 
        else:
        # the first pending element of each half needs to be compared
            if tmp[l]>=tmp[r]:
                
                A[n] = tmp[l]
                l = l+1 # choose the one on the left
            else: 
                A[n] = tmp[r] # choose the one on the right
                r = r+1

tmp = [ None for _ in range(10) ]
A = [1, 2, 3, 4, 5, 6]
mergesort(A, 0, len(A))
#merge(A, 0, len(A)//2, len(A))
print(A)
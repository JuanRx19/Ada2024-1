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


def obtainFirst(A, low, hi, x):
    ans = 0
    if(low < hi):
        ans = 0
    elif(low+1 == hi):
        pass
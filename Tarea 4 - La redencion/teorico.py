from sys import stdin

def solve(A, interval):
  # A = [(s0, f0), (s1, f1), ..., (s(n-1), f(n - 1))]
  medianoche = True
  ans = 0
  i = 0
  lans = []
  while i != len(A):
    #print(f"{interval[1]} < {A[i][0]} and {interval[1]} < {A[i][1]}")
    if(A[i][0] > interval[1] and medianoche):
      ans += 1
      interval = A[i]
      lans.append(A[i])
    elif(not(medianoche) and interval[1] < A[i][0] and A[i][1] < mignightEnd[0] and A[i][0] - A[i][1] < 0):
      ans += 1
      interval = A[i]
      lans.append(A[i])
    if(A[i][0] - A[i][1] >= 0 and medianoche):
        medianoche = False
        mignightEnd = A[i]
    
    i += 1
  return lans

def phi(A, interval, medianoche, midnightEnd, i):
    ans = 0
    if(i == len(A)):
        ans = 0
    else:
        if(A[i][0] > interval[1] and medianoche):
            if(A[i][0] - A[i][1] >= 0):
                medianoche = False
                midnightEnd  = A[i]
            ans = 1 + phi(A, A[i], medianoche, midnightEnd, i+1)
        elif(not(medianoche) and interval[1] < A[i][0] and A[i][1] < midnightEnd[0] and A[i][0] - A[i][1] < 0):
           ans = 1 + phi(A, A[i], medianoche, midnightEnd, i+1)
        else:
           ans = phi(A, interval, medianoche, midnightEnd, i+1)
    return ans

def main():
    act = [(2, 1), (0, 4), (3, 23)]
    act1 = [(18, 6), (21, 4), (3, 14), (13, 19)]
    act2 = [(1,3),(4,20),(21,2)]
    act3 = [(16,20), (5,10), (12,11), (18, 6), (21,4), (3,14), (13, 19)]
    act4 = [(2, 2), (0, 4), (3, 23)]
    act.sort(key = lambda x: x[1])
    act1.sort(key = lambda x: x[1])
    act2.sort(key = lambda x: x[1])
    act3.sort(key = lambda x: x[1])
    act4.sort(key = lambda x: x[1])
    interval = (0, 0)
    print(solve(act, interval))
    print(phi(act, interval, True, interval, 0))
    print(solve(act1, interval))
    print(phi(act1, interval, True, interval, 0))
    print(solve(act2, interval))
    print(phi(act2, interval, True, interval, 0))
    print(solve(act3, interval))
    print(phi(act3, interval, True, interval, 0))
    print(solve(act4, interval))
    print(phi(act4, interval, True, interval, 0))

main()
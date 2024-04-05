def solve(A, interval, medianoche, midnightEnd, i):
    ans = 0
    if(i == len(A)):
        ans = 0
    else:
        if(A[i][0] > interval[1] and medianoche):
            if(A[i][0] - A[i][1] >= 0):
                medianoche = False
                midnightEnd  = A[i]
            ans = 1 + solve(A, A[i], medianoche, midnightEnd, i+1)
        elif(not(medianoche) and interval[1] < A[i][0] and A[i][1] < midnightEnd[0] and A[i][0] - A[i][1] < 0):
           ans = 1 + solve(A, A[i], medianoche, midnightEnd, i+1)
        else:
           ans = solve(A, interval, medianoche, midnightEnd, i+1)
    return ans
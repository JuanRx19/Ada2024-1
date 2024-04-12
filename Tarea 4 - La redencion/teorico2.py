
def tiempoDuracion(act):
  temp = []
  for a in act:
    if(a[0] > a[1]):
      time = a[1] - a[0] + 24
    else:
      time = a[1] - a[0]
    temp.append((a[0], a[1], time))
  return temp

def solve(A, interval):
  medianoche = True
  ans = 0
  i = 0
  lans = []
  while i != len(A):
    #print(f"{interval[1]} < {A[i][0]} and {interval[1]} < {A[i][1]}")
    if((A[i][0] >= interval[1] and A[i][1] <= interval[0]) and medianoche and A[i][0] - A[i][1] >= 0):
      ans += 1
      interval = A[i]
      medianoche = False
      lans.append((A[i][0], A[i][1]))
    elif((A[i][0] >= interval[1] or A[i][1] <= interval[0]) and medianoche and A[i][0] - A[i][1] < 0):
      ans += 1
      interval = A[i]
      lans.append((A[i][0], A[i][1]))
    elif(not(medianoche) and interval[1] <= A[i][0] and A[i][0] - A[i][1] < 0):
      ans += 1
      interval = A[i]
      lans.append((A[i][0], A[i][1]))

    i += 1
  
  return lans, ans


def main():
  act = [(2, 1), (0, 4), (3, 23)]
  act1 = [(18, 6), (21, 4), (3, 14), (13, 19)]
  act2 = [(1,3),(4,20),(21,2)]
  act3 = [(16,20), (5,10), (12,11), (18, 6), (21,4), (3,14), (13, 19)]
  act4 = [(2, 2), (0, 4), (3, 23)]
  act5 = [(13, 14), (15, 16), (23, 13)]
  act6 = [(17, 2), (2, 3), (18, 20), (20, 22)]
  act = tiempoDuracion(act)
  act1 = tiempoDuracion(act1)
  act2 = tiempoDuracion(act2)
  act3 = tiempoDuracion(act3)
  act4 = tiempoDuracion(act4)
  act5 = tiempoDuracion(act5)
  act6 = tiempoDuracion(act6)
  act.sort(key = lambda x: x[2])
  act1.sort(key = lambda x: x[2])
  act2.sort(key = lambda x: x[2])
  act3.sort(key = lambda x: x[2])
  act4.sort(key = lambda x: x[2])
  act5.sort(key = lambda x: x[2])
  act6.sort(key = lambda x: x[2])
  interval = (0, 0)
  #print(act)
  print(solve(act, interval))
  print(solve(act1, interval))
  print(solve(act3, interval))
  print(solve(act6, interval))
  
main()
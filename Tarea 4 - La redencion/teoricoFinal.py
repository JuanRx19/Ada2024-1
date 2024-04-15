def verificar(lans, schedule):
  #print(schedule)
  ans = True
  i = 0
  if(len(lans) == 0):
    ans = True
  else:
    while(i != len(lans) and ans):
      if(lans[i][1] >= 24 and lans[i][0] + schedule[1] >= lans[i][1]):
        ans = False
      elif((lans[i][0] >= schedule[1] and lans[i][0] > schedule[0]) or (lans[i][1] <= schedule[0] and lans[i][1] < schedule[1])):
        ans = True
      else:
        ans = False
      i+=1
  
  return ans

def verificarphi(lans, schedule, j):
  ans = None
  if(j == len(lans)):
    ans = True
  elif(lans[j][1] >= 24 and lans[j][0] + schedule[1] >= lans[j][1]):
    ans = False
  elif((lans[j][0] >= schedule[1] and lans[j][0] > schedule[0]) or (lans[j][1] <= schedule[0] and lans[j][1] < schedule[1])):
    ans = verificarphi(lans, schedule, j + 1)
  else:
    ans = False

  return ans

def phi(A, i, lans):
  ans = 0
  if(i == len(A)):
    ans = 0
  else:
    if(verificarphi(lans, A[i], 0)):
      lans.append(A[i])
      ans = 1 + phi(A, i + 1, lans)
    else:
      ans = phi(A, i + 1, lans)

  return ans

def tiempoDuracion(act):
  temp = []
  for a in act:
    time = a[1] - a[0]
    temp.append((a[0], a[1], time))
  return temp

def solve(A):
  lans = []
  ans = 0
  for schedule in A:
    if(verificar(lans, schedule)):
      ans+=1
      lans.append((schedule[0], schedule[1]))
  
  return lans, ans

def main():
  act = [(2, 25), (24, 28), (3, 23)]
  act1 = [(18, 30), (21, 28), (3, 14), (13, 19)]
  act2 = [(1, 3),(4, 20),(21, 26)]
  act3 = [(16, 20), (5, 10), (12, 35), (18, 30), (21, 28), (3,14), (13, 19)]
  act4 = [(2, 26), (24, 28), (3, 23)]
  act5 = [(13, 14), (15, 16), (23, 37)]
  act6 = [(17, 26), (2, 3), (18, 20), (20, 22)]
  act7 = [(4,27), (10,16), (21,4)]
  act = tiempoDuracion(act)
  act1 = tiempoDuracion(act1)
  act2 = tiempoDuracion(act2)
  act3 = tiempoDuracion(act3)
  act4 = tiempoDuracion(act4)
  act5 = tiempoDuracion(act5)
  act6 = tiempoDuracion(act6)
  act7 = tiempoDuracion(act7)
  act.sort(key = lambda x: x[2])
  act1.sort(key = lambda x: x[2])
  act2.sort(key = lambda x: x[2])
  act3.sort(key = lambda x: x[2])
  act4.sort(key = lambda x: x[2])
  act5.sort(key = lambda x: x[2])
  act6.sort(key = lambda x: x[2])
  act7.sort(key = lambda x: x[2])
  print(solve(act))
  print(phi(act, 0, []))
  print(solve(act1))
  print(phi(act1, 0, []))
  print(solve(act2))
  print(phi(act2, 0, []))
  print(solve(act3))
  print(phi(act3, 0, []))
  print(solve(act4))
  print(phi(act4, 0, []))
  print(solve(act5))
  print(phi(act5, 0, []))
  print(solve(act6))
  print(phi(act6, 0, []))
  print(solve(act7))
  print(phi(act7, 0, []))

main()
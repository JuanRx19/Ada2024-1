#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

def conflict(count, x, value):
  ans = None
  if(x == 1 and count + value <= 23):
    ans = True
  elif(x == 2 and count - value <= 23):
    ans = True
  elif(x == 3 and count * value <= 23):
    ans = True
  else:
    ans = False

  return ans

def solve(values, count, i, data):
  ans = None
  if(count == 23 and i == 5):
    #print(count, i)
    ans = True
  elif(i == 5):
    data+=1
    ans = False
  else:
    ans = False
    for x in range(1, 4):
      if(conflict(count, x, values[i])):
        if(x == 1):
          count += values[i]
        elif(x == 2):
          count -= values[i]
        else:
          count *= values[i]
        #print(values[value], x, count)
        ans, data = solve(values, count, i + 1, data)

  return ans, data

def verificar(values):
  return not(values[0] == 0 and values[1] == 0 and values[2] == 0 and values[3] == 0 and values[4] == 0)

def main():
  values = list(map(int, stdin.readline().split()))
  while(verificar(values)):
    print(solve(values, 0, 0, 0))
    values = list(map(int, stdin.readline().split()))
main()
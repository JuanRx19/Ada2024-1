#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

def permutation(values):
  ans = None
  i = len(values) - 2
  while(i >= 0 and values[i] >= values[i + 1]):
    i -= 1
  if(i == -1):
    ans = False
  else:
    j = i + 1
    while(j < len(values) and values[j] > values[i]):
      j += 1
    j -= 1
    values[i], values[j] = values[j], values[i]
    start = i + 1
    end = len(values) - 1
    while(start < end):
      temp = values[start]
      values[start] = values[end] 
      values[end] = temp
      start += 1
      end -= 1
    ans = True
  
  return ans

def conflict(count, value, x):
  if(x == 3 and (count % value != 0)):
    ans = False
  else:
    ans = True
  return ans

def solve(values, count, i):
  ans = None
  if(i == 0):
    ans = count - values[0] == 0
  else:
    ans = False
    x = 1
    while(not(ans) and x < 4):
      if(conflict(count, values[i], x)):
        if(x == 1):
          ans = solve(values, count - values[i], i - 1)
        elif(x == 2):
          ans = solve(values, count + values[i], i - 1)
        else:
          ans = solve(values, count // values[i], i - 1)
      x+=1

  return ans

def verificar(values):
  return not(values[0] == 0 and values[1] == 0 and values[2] == 0 and values[3] == 0 and values[4] == 0)

def main():
  ans = False
  values = list(map(int, stdin.readline().split()))
  while(verificar(values)):
    values.sort()
    ans = False
    ans = solve(values, 23, 4)
    while(not(ans) and permutation(values)):
      ans = solve(values, 23, 4)
    if(ans):
      print("Possible")
    else:
      print("Impossible")
    values = list(map(int, stdin.readline().split()))
    
main()
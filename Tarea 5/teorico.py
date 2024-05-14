def solve(X, T, i, data, ans):
  if(i == len(X) and T == 0):
    print(data)
    ans += 1
  elif(i == len(X) and T != 0):
    ans = 0
  else:
    ans = solve(X, T, i + 1, data, ans)
    if(X[i] <= T):
      data.append(X[i])
      ans += solve(X, T - X[i], i + 1, data, ans)
      data.pop()
  
  return ans

def solve2(X, T, i, data, ans):
  if(i == len(X) and T == 0):
    print(data)
    ans += 1
  elif(i == len(X) and T != 0):
    ans = 0
  else:
    data.append(X[i])
    ans = solve2(X, T - X[i], i + 1, data, ans)
    data.pop()
    ans += solve2(X, T, i + 1, data, ans)
  
  return ans

def solve3(X, W, T, MW, i, data, ans):
  global value
  global subconjunto
  if(i == len(X) and T == 0):
    if(MW > value):
      subconjunto = data.copy()
      #print(subconjunto)
    value = max(value, MW)
    #print(data, T == 0)
    ans += 1
  elif(i == len(X) and T != 0):
    ans = 0
  else:
    ans = solve3(X, W, T, MW, i + 1, data, ans)
    if(X[i] <= T):
      data.append((X[i], W[i]))
      ans += solve3(X, W, T - X[i], MW + W[i], i + 1, data, ans)
      data.pop()
  
  return ans

def solve4(X, W, MW, T, i, data, ans):
  global value
  global subconjunto
  if(i == len(X) and T == 0):
    if(MW > value):
      subconjunto = data.copy()
      #print(subconjunto)
    value = max(value, MW)
    #print(data, T == 0)
    ans += 1
  elif(i == len(X) and T != 0):
    ans = 0
  else:
    #print(i, len(X), MW, T,  T != 0)
    data.append((X[i], W[i]))
    ans = solve4(X, W, MW + W[i], T - X[i], i + 1, data, ans)
    data.pop()
    ans += solve4(X, W, MW, T, i + 1, data, ans)
  
  return ans

#X = [3,6,1,2,4,5,27,8,9,10]
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
T = 20
W = [1, 1, 1, 1, 1, 1, 1, 1, 50, 50]
#W = [4, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(solve(X, T, 0, [], 0))
#print(solve2(X, T, 0, [], 0))
global value
global subconjunto
value = -float('inf')
if(solve3(X, W, T, 0, 0, [], 0) != 0):
  print(value)
  print(subconjunto)
else:
  print(value)

if(solve4(X, W, 0, T, 0, [], 0) != 0):
  print(value)
  print(subconjunto)
else:
  print(value)
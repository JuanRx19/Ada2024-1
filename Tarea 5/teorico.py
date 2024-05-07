def solve(X, T, i, data, ans):
  if(i == len(X) and T == 0):
    print(data, T == 0)
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
    print(data, T == 0)
    ans += 1
  elif(i == len(X) and T != 0):
    ans = 0
  else:
    data.append(X[i])
    ans = solve2(X, T - X[i], i + 1, data, ans)
    data.pop()
    ans += solve2(X, T, i + 1, data, ans)
  
  return ans

def solve3(X, W, MW, T, i, data, ans):
  if(i == len(X) and T == 0 and MW >= 0):
    print(data, MW, T == 0 and MW >= 0)
    ans += 1
  elif(i == len(X) and T != 0):
    ans = 0
  else:
    ans = solve3(X, W, MW, T, i + 1, data, ans)
    if(X[i] <= T and W[i] <= MW):
      data.append((X[i], W[i]))
      ans += solve3(X, W, MW - W[i], T - X[i], i + 1, data, ans)
      data.pop()
  
  return ans

def solve4(X, W, MW, T, i, data, ans):
  if(i == len(X) and T == 0 and MW >= 0):
    print(data, MW, T == 0 and MW >= 0)
    ans += 1
  elif(i == len(X) and T != 0 or MW < 0):
    ans = 0
  else:
    #print(i, len(X), MW, T,  T != 0)
    data.append((X[i], W[i]))
    ans = solve4(X, W, MW - W[i], T - X[i], i + 1, data, ans)
    data.pop()
    ans += solve4(X, W, MW, T, i + 1, data, ans)
  
  return ans

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
T = 20
W = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
MW = 3
print(solve(X, T, 0, [], 0))
#print(solve2(X, T, 0, [], 0))
#print(solve3(X, W, MW, T, 0, [], 0))
#print(solve4(X, W, MW, T, 0, [], 0))

#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

def repostar(capacity, mpg, miles, value):
  #print("Millas ", miles)
  newcost = ((capacity - (miles / mpg)) * value) / 100
  newmiles = ((capacity - (miles / mpg)) * mpg) + miles

  return newcost, newmiles

def solve(capacity, mpg, cost, stations, miles, pivot, i):
  global bestcost, C
  if(miles > C - pivot):
    bestcost = min(bestcost, cost)
  else: 
    if(miles - (stations[i+1][0] - stations[i][0]) - (stations[i][0] - pivot) < 0):
      #print("Entra: ", miles, miles - ((stations[i + 1][0] - stations[i][0]) + (stations[i][0] - pivot)), i)
      newcost, newmiles = repostar(capacity, mpg, miles - (stations[i][0] - pivot), stations[i][1])
      #print(newcost + 2, newmiles)
      solve(capacity, mpg, cost + newcost + 2, stations, newmiles, stations[i][0], i + 1)
    elif(miles / mpg > capacity / 2):
      solve(capacity, mpg, cost, stations, miles - (stations[i][0] - pivot), stations[i][0], i + 1)
    else:
      newcost, newmiles = repostar(capacity, mpg, miles - (stations[i][0] - pivot), stations[i][1])
      solve(capacity, mpg, cost + newcost + 2, stations, newmiles, stations[i][0], i + 1)
      solve(capacity, mpg, cost, stations, miles - (stations[i][0] - pivot), stations[i][0], i + 1)

def main():
  global bestcost, C
  C = float(stdin.readline())
  set = 1
  while(C != -1):
    stations = []
    bestcost = float('inf')
    capacity, mpg, cost, countstations = map(float, stdin.readline().split())
    for _ in range(int(countstations)):
      data = stdin.readline().split()
      stations.append((float(data[0]), float(data[1])))
    stations.append((C, 0))
    print(f"Data Set #{set}")
    solve(capacity, mpg, cost, stations, capacity * mpg, 0, 0)
    print(f"minimum cost = ${bestcost:.2f}")
    C = float(stdin.readline())
    set+=1

main()
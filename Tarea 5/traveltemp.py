def repostar2(capacity, miles, mpg, value):
  return round((((capacity - miles) / mpg) * value) / 100, 2) + 2

def solve2(capacity, mpg, cost, stations, miles, pivot, i, data):
  global bestcost, C
  if(miles > C - pivot):
    #print(miles, C, pivot, i)
    bestcost = min(bestcost, cost)
  else:
    if(miles - (stations[i+1][0] - stations[i][0]) - (stations[i][0] - pivot) < 0):
      data.append(("No alcanza a la proxima, solo siguiente", round(miles - (stations[i][0] - pivot), 2)))
      solve2(capacity, mpg, cost + repostar2(capacity, miles - (stations[i][0] - pivot), mpg, stations[i][1]), stations, capacity, stations[i][0], i + 1, data)
    elif(miles - stations[i][0] > capacity / 2):
      data.append(("Siguiente y proxima", round(miles - stations[i][0], 2), miles - (stations[i+1][0] - stations[i][0]) - (stations[i][0] - pivot)))
      solve2(capacity, mpg, cost, stations, round(miles - stations[i][0], 2), stations[i][0], i + 1, data)
      data.pop()
    else:
      data.append(("Repostar", round(miles - stations[i][0], 2)))
      solve2(capacity, mpg, cost + repostar2(capacity, round(miles - (stations[i][0] - pivot), 2), mpg, stations[i][1]), stations, capacity, stations[i][0], i + 1, data)
      data.pop()
      data.append(("No repostar", round(miles - stations[i][0], 2)))
      solve2(capacity, mpg, cost, stations, round(miles - stations[i][0], 2), stations[i][0], i + 1, data)
      data.pop()
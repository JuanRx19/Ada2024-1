#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

def binarytovalue(binary):
  count = 0
  potencia = 2
  for bit in binary:
    if(bit == '1'):
      count+= 1 << potencia
    potencia-=1

  return count

def automata(value):
    potencia = 7
    data = [0] * 8
    #print(data)
    while(potencia != -1):
        op = 1 << potencia
        if(op <= value):
          value -= op
          data[potencia] = '1'
        else:
          data[potencia] = '0'
        potencia-=1
    return data

def getbits(prev):
  temp = []
  temp.append(prev[len(prev) - 2])
  temp.append(prev[len(prev) - 1])
  temp.append(prev[0])

  return "".join(temp)

def conflict(rules, bits, value):
  ans = None

  if(rules[binarytovalue(bits)] == value):
    ans = True
  else:
    ans = False
  
  return ans

def solve(rules, tam, cadena, i, prev):
  ans = None
  if(i == tam):
    ver1 = [prev[len(prev)-1], prev[0], prev[1]]
    ver2 = [prev[0], prev[1], prev[2]]
    #print("Entra")
    if(conflict(rules, "".join(ver1), cadena[0]) and conflict(rules, "".join(ver2), cadena[1])):
      #print(prev)
      ans = True
    else:
      ans = False
  else:
    ans = False
    for bit in range(2):
      if(bit == 0):
        prev.append('0')
      else:
        prev.append('1')
      if(i < 2):
        ans = solve(rules, tam, cadena, i + 1, prev)
      elif(i >= 2 and conflict(rules, getbits(prev), cadena[i])):
        ans = solve(rules, tam, cadena, i + 1, prev)
      prev.pop()
  
  return ans

def main():
  line = stdin.readline().strip()
  while(line != ""):
    rules, tam, cadena = line.split()
    if(solve(automata(int(rules)), int(tam), list(cadena), 0, [])):
      print("REACHABLE")
    else:
      print("GARDEN OF EDEN")
    line = stdin.readline().strip()

#print(getbits('110'))
#print(automata(121))
#print(binarytovalue('101'))
main()
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
  temp.append(prev[len(prev) - 3])
  temp.append(prev[len(prev) - 2])
  temp.append(prev[len(prev) - 1])

  return "".join(temp)

def conflict(rules, bits, value, prev):
  ans = None
  #print(prev,rules[binarytovalue(bits)], value)
  if(rules[binarytovalue(bits)] == value):
    ans = True
  else:
    ans = False
  
  return ans
  
def solve(rules, tam, cadena, i, prev, id):
  ans = None
  if(i == tam):
    #ans = True
    #print(prev)
    ver1 = "".join([prev[len(prev)-1], prev[0], prev[1]])
    ver2 = "".join([prev[len(prev)-2], prev[len(prev)-1], prev[0]])
    if(conflict(rules, ver1, cadena[0], prev) and conflict(rules, ver2, cadena[len(prev)-1], prev)):
      #print("Entra ", prev)
      ans = True
    else:
      ans = False
  else:
    ans = False
    bit = 0
    while(not(ans) and bit < 2):
      if(bit == 0):
        prev.append('0')
      else:
        prev.append('1')
      if(i < 2):
        ans = solve(rules, tam, cadena, i + 1, prev, id)
      elif(i >= 2 and conflict(rules, getbits(prev), cadena[i-1], prev)):
        ans = solve(rules, tam, cadena, i + 1, prev, id)
      prev.pop()
      bit+=1
  
  return ans

def main():
  line = stdin.readline().strip()
  while(line != ""):
    rules, tam, cadena = line.split()
    if(solve(automata(int(rules)), int(tam), list(cadena), 0, [], int(rules))):
      print("REACHABLE")
    else:
      print("GARDEN OF EDEN")
    line = stdin.readline().strip()

#print(getbits('110'))
#print(automata(204))
#print(binarytovalue('101'))
main()
#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

def generate_rules(automata):
  pass

def automata(value):
    potencia = 7
    data = []
    while(potencia != -1):
        op = 1 << potencia
        if(op <= value):
          value -= op
          data.append("1")
        else:
          data.append("0")
        potencia-=1
    return data

def conflict():
  pass

def solve(rules, tam, cadena, i, prev):
  ans = None
  if(i == tam):
    ans = True
  else:
    ans = False
    for i in range(2):
      prev.append(i)
      if(i >= 2 and conflict()):
        ans = solve(rules, tam, cadena, i + 1, prev)
      prev.pop()

def main():
  line = stdin.readline().strip()
  while(line != ""):
    rules, tam, cadena = line.split()
    if(solve(automata(int(rules)), int(tam), list(cadena), 0, [])):
      print("REACHABLE")
    else:
      print("GARDEN OF EDEN")
    line = stdin.readline().strip()

print(automata(133))
#main()
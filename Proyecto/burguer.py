#Juan Miguel Rojas Mejía
#8963761

#Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali
#me comprometo a seguir los más altos estándares de integridad académica.

from sys import stdin

INF = 100005

def solve(l, i, intervalo, N, mem):
  """
  Minima cantidad de movimientos para concinar el
  lado l de la hamburguesa n - l minutos en i intervalos.

  Parametros: l --> Lado de la hamburguesa
              i --> el intervalo en el que me encuentro

  """

  if((l, i) in mem):
    ans = mem[(l, i)]
  else:
    if(l == N):
      ans = 0
    elif(i == len(intervalo) or l > N):
      ans = INF
    else:
      ans = solve(l, i + 1, intervalo, N, mem)
      li, ls = intervalo[i][0], intervalo[i][1] + 1
      for x in range(li, ls):
        ans = min(ans, solve(x - l, i + 1, intervalo, N, mem) + 1)
        if(x != ls-1): #No es correcto hacer 2 movimientos en un mismo minuto, si x es 10 y el ls es 10 no tiene sentido hacer 2 movimientos
          ans = min(ans, solve(l + ((ls-1) - x), i + 1, intervalo, N, mem) + 2)
    mem[(l, i)] = ans
  return ans

def solvedcc(l, i, intervalo, N, mem):
  if(l == N):
    ans = 0
  elif(i == len(intervalo) or l > N):
    ans = INF
  else:
    ans = solve(l, i + 1, intervalo, N, mem)
    li, ls = intervalo[i][0], intervalo[i][1] + 1
    for x in range(li, ls):
      ans = min(ans, solve(x - l, i + 1, intervalo, N, mem) + 1)
      if(x != ls-1):
        ans = min(ans, solve(l + ((ls-1) - x), i + 1, intervalo, N, mem) + 2)
  return ans

def main():
  """
  Esta función recibe los valores correspondientes a la entrada
  y los convierte en las variables, donde N es el primer valor de la primera lina
  y K el segundo valor de la primera linea, los siguientes valores son los intervalos
  los cuales se acumulan en intervalo.
  """
  C = int(stdin.readline())
  while(C > 0):
    intervalo = []
    N, K = map(int, stdin.readline().split())
    for _ in range(K):
      l0, l1 = map(int, stdin.readline().split())
      intervalo.append((l0, l1))
    #ans = solve(0, 0, 0, intervalo, 0, 0, N, 0, {})
    #ans = solve(0, 0, intervalo, 0, 0, N, {})
    ans = solve(0, 0, intervalo, N, {})
    if(ans != INF):
      print("Perfect burger!")
      print(ans)
    else:
      print("Another bland and poorly cooked burger!")
    C-=1

main()
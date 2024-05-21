#Juan Miguel Rojas Mejía
#8963761

#Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali
#me comprometo a seguir los más altos estándares de integridad académica.

from sys import stdin

INF = 100005

def convertir(interval, i, j):
  """
  Esta función define el paso siguiente a dar entre los intervalos, si el limite inferior es igual al
  superior, entonces debo pasar al siguiente intervalo. Por ejemplo, si tengo (4, 4) significa que no tengo mas valores
  para buscar dentro del intervalo (4, 4), por lo que avanzo al siguiente intervalo.
  
  Parametros: interval --> tupla con el limite inferior y superior.
              i --> el intervalo en el que se encuentra.
              j --> el valor a sumar al limite inferior.
  
  Retorna: La suma del limite inferior + j, el intervalo y el valor a sumar en la siguiente recurrencia.
  """
  value = (interval[0] + j)
  if((interval[0] + j) != interval[1]):
    j += 1
  else:
    j = 0
    i += 1
  return value, i, j

def solve(l0, l1, intervalo, i, j, N, mem):
  if((l0, l1, i) in mem):
    ans = mem[(l0, l1, i)]
  else:
    if(l0 == N):
      if(l1 != N):
        ans = 1
      else:
        ans = 0
    elif(i == len(intervalo) or l0 > N or l1 > N):
      ans = INF
    else:
      value, i, j = convertir(intervalo[i], i, j)
      ans = min(solve(l1, l0 + (value - (l1 + l0)), intervalo, i, j, N, mem) + 1,
                solve(l0 + (value - (l1 + l0)), l1, intervalo, i, j, N, mem))
    mem[(l0, l1, i)] = ans

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
    ans = solve(0, 0, intervalo, 0, 0, N, {})
    if(ans != INF):
      print("Perfect burger!")
      print(ans)
    else:
      print("Another bland and poorly cooked burger!")
    C-=1

main()
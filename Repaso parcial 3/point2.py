def dec(x):
  return x in palabras

def solve(cadena, n, low, hi, mem):
  if((n, low, hi) in mem):
    print("Entra")
    ans = mem[(n, low, hi)]
  else:
    if(n-1 == 0 and dec(cadena[low:len(cadena)])):
      ans = True
    elif(hi == len(cadena)):
      ans = False
    else:
      ans = solve(cadena, n, low, hi+1, mem)
      if(dec(cadena[low:hi])):
        ans = ans or solve(cadena, n-1, hi, hi+1, mem)
    mem[(n, low, hi)] = ans

  return ans

palabras = {"agua", "pozo", "mariajose", "cabina", "castro", "sarmi", "adaen5", "gane", "a"}
cadena = "aguapozocabinamariajosecastrosarmiganeadaen5a"

#print(solve(cadena, 9, 0, 1, {}))


import math

def n_log_n(microseg):
    n = 1
    flag = 0
    while flag == 0:
        tiempo = n * math.log(n)
        if tiempo > microseg:
            flag = 1
        n += 1
    return n

def n_factorial(microseg):
    n = 1
    flag = 0
    while flag == 0:
        tiempo = n * math.factorial(n)
        if tiempo > microseg:
            flag = 1
        n += 1
    return n

microseg = 2592*10**9
print(f"El tamaño máximo n para {microseg} microsegundos es aproximadamente {n_log_n(microseg)}")
print(f"El tamaño máximo n para {microseg} microsegundos es aproximadamente {n_factorial(microseg)}")
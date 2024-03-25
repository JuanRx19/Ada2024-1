def calc(s):
    pila_signos = []
    pila_signos.append(1)
    suma = 0
    operacion = 1
    for caracter in s:
        if caracter == "x":
            suma += operacion
        elif caracter == "+":
            operacion = pila_signos[-1]
        elif caracter == "-":
            operacion = -pila_signos[-1]
        elif caracter == "(":
            pila_signos.append(operacion)
        elif caracter == ")":
            pila_signos.pop()
    return suma

def solve():
    s = input()
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    cnt = (n + calc(s)) // 2
    for i in range(cnt):
        ans += a[i]
    for i in range(cnt, n):
        ans -= a[i]
    print(ans)

def main():
    C = int(input())
    while(C != 0):
        solve()
        C -= 1
main()
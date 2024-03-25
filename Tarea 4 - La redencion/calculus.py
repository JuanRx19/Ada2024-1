#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

def getX(ops):
    stack = [0]
    cantN = 0
    signo = 0
    for letra in ops:
        if(letra == 'x' and signo == 1):
            cantN += 1
        elif(letra == '-'):
            if(stack[-1] == 1):
                signo = 0
            else:
                signo = 1
        elif(letra == '+'):
            if(stack[-1] == 1):
                signo = 1
            else:
                signo = 0
        elif(letra == '('):
            stack.append(signo)
        elif(letra == ')'):
            stack.pop()
    return cantN

def solve(ops, X, val):
    val.sort()
    cant = getX(ops)
    ans = 0
    for i in range(X):
        if(i <= cant-1):
            ans -= val[i]
        else:
            ans += val[i]
    return ans

def main():
    C = int(stdin.readline())
    while(C != 0):
        ops = stdin.readline()
        X = int(stdin.readline())
        val = list(map(int, stdin.readline().split()))
        print(solve(ops, X, val))
        C -= 1
main()

"""op = '10 + (4 - (5 - 1))'
pila = [1, 2, 3, 4, 5]
print(len(pila))
print(pila.pop())
print(len(pila))
print(op)
print(eval(op))
print(7 - 3 + 9 + 6 + (9 - 1 + 9))
print(- 1 + (- 3 + 6 + 7)+ 9 + 9 + 9)"""
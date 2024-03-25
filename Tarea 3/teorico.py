from sys import stdin

def phi(n, s, x, I, mem, X, F):
    if((n, s) in mem):
        ans = mem[(n, s)]
    else:
        if(n == I):
            ans = x
        else:
            ans = max(phi(n + 1, 0, x + min(X[n], F[s]), I, mem, X, F), phi(n + 1, s + 1,x, I, mem, X, F))
    
    return ans

#phi()

def concat(x, C):
    pass

def phi(n, x, C, word, mem):
    if((n, x) in mem):
        ans = mem[(n, x)]
    else:
        if(n == 0):
            ans = False
        elif(x == word):
            ans = True
        else:
            ans = phi(n-1, concat(x, C[n-1]), C, word, mem) or phi(n-1, x, C, word, mem)
    
    return ans

def IsWord(word):
    words = {"ARTIST", "OIL", "ART", "IS", "TOIL"}
    return word in words

def phi2(left, right, word, mem):
    if (left , right) in mem:
        ans = mem [(left, right)]
    else:
        if right == len(word):  
            if(IsWord(word[left:right])):
                ans = 1
            else:
                ans = 0
        else:
            ans = phi2(left, right+1, word, mem)
            if IsWord(word[left:right]):
                ans = 1 + ans + phi2(right, right+1, word, mem)
        mem[(left , right)] = ans

    return ans

"""def phi2(left, right, word, mem):
    if (left , right) in mem:
        ans = mem [(left, right)]
    else:
        if(right == len(word)):
            ans = 0
        else:
            if IsWord(word[left:right]):
                ans =  1 + 
        mem[(left , right)] = ans

    return ans"""
print(phi2(0, 1, "ARTISTOIL", {}))

def phi3(A, B, C, mem):
    ans = False
    if (A, B, C) in mem:
        ans = mem[(A, B, C)]
    else:
        if len(A) == 0 and len(B) == 0 and len(C) == 0:
            ans = True
        elif(len(A) != 0 and C[0] == A[0]):
            ans = phi3(A[1:], B, C[1:], mem)
        elif(len(B) != 0 and C[0] == B[0]):
            ans = phi3(A, B[1:], C[1:], mem)
        
        mem[(A, B, C)] = ans
    return ans

def phi4(A, B, C, contA, contB, mem):
    ans = False
    if (A, B, C) in mem:
        ans = mem[(A, B, C)]
    else:
        if(contA == 3 or contB == 3):
            ans = False
        elif len(A) == 0 and len(B) == 0 and len(C) == 0:
            ans = True
        elif(len(A) != 0 and C[0] == A[0]):
            ans = phi4(A[1:], B, C[1:], contA + 1, 0, mem)
        elif(len(B) != 0 and C[0] == B[0]):
            ans = phi4(A, B[1:], C[1:], 0, contB + 1, mem)
        
        mem[(A, B, C)] = ans
    return ans

# Ejemplo de uso
X = "PROGRAMMING"
Y = "DYNAMIC"
Z1 = "PRDOYGNARAMMMIICNG"
Z2 = "PRODYGNARAMMMIICNG"

print(f"Z1 es una 'shuffle' de X e Y: {phi3(X, Y, Z1, {})}")
print(f"Z1 es una 'smooth shuffle' de X e Y: {phi4(X, Y, Z1, 0, 0, {})}")

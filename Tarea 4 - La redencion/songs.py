#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

def corregirDatos(C):
    limite = len(C)-2
    datos = []

    for i in range(0, limite, 3):
        datos.append([int(C[i]), int(C[i+1]) / float(C[i+2])])
    
    return datos, int(C[len(C)-1])

def solve(C):
    songs, indice = corregirDatos(C)
    songs.sort(key = lambda x: x[1])
    #print(songs)
    return songs[indice-1][0]
def main():
    C = stdin.readline()
    while(C != "\n"):
        datos = stdin.readline()
        print(solve(list(map(float, datos.split()))))
        C = stdin.readline()

main()
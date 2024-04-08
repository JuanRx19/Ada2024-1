#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

def obtenerDatos(C):
    matriz = []
    datos = list(map(float, stdin.readline().split()))
    while(len(datos) != 1):
        for i in range(0, len(datos)-1, 3):
            matriz.append([datos[i], datos[i+1], datos[i+2]])
        datos = list(map(float, stdin.readline().split()))

    songSelect = int(datos[0])
    return matriz, songSelect

def solve(songSelect, matriz):
    songs = []
    for i in range(len(matriz)):
        songs.append((matriz[i][0], matriz[i][1]/matriz[i][2]))
    songs.sort(key = lambda x: x[1])

    return int(songs[songSelect-1][0])

def main():
    C = stdin.readline().strip()
    matriz = []
    while(C != ""):
        C = int(C)
        matriz, songSelect = obtenerDatos(C)
        print(solve(songSelect, matriz))
        C = stdin.readline().strip()

main()
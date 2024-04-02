#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <cstring>
#define inf 0x3f3f3f3f;
using namespace std;
#define MAX 100

int padre[ MAX ];

void MakeSet( int n ){
    for( int i = 1 ; i <= n ; ++i ) padre[ i ] = i;
}

int Find( int x ){
    return ( x == padre[ x ] ) ? x : padre[ x ] = Find( padre[ x ] );
}

void Union( int x , int y ){
    padre[ Find( x ) ] = Find( y );
}

bool sameComponent( int x , int y ){
    if( Find( x ) == Find( y ) ) return true;
    return false;
}

int V , E;

struct Edge{
    int origen;
    int destino;
    int peso;
    Edge(){}
    bool operator<( const Edge &e ) const {
        return peso < e.peso;
    }
}arista[ MAX ];
Edge MST[ MAX ];

int Kruskal(){
    int start = 0;
    int ans = inf;
    bool flag = true;
    while (flag)
    {
        int origen , destino , peso;
        int total = 0;
        int numAristas = 0;

        MakeSet( V );
        sort( arista , arista + E );

        for( int i = start ; i < E ; ++i ){
            origen = arista[ i ].origen;
            destino = arista[ i ].destino;
            peso = arista[ i ].peso;

            if( !sameComponent( origen , destino ) ){
                total += peso;
                MST[ numAristas++ ] = arista[ i ];
                Union( origen , destino );
            }
        }
        if(V - 1 != numAristas){
            flag = false;
        }else{
            ans = min(ans, MST[numAristas-1].peso - MST[0].peso);
        }
        start++;
    }
    
    return ans;
}

int main(){
    freopen("spanin.txt", "r", stdin);
    freopen("spanout.txt", "w", stdout);
    int infinito = inf;
    int ans = -1;
    int start = 0;
    while (cin >> V >> E, V != 0)
    {
        for( int i = 0 ; i < E ; i++){
            cin >> arista[i].origen >> arista[i].destino >> arista[i].peso;
        }

        ans = Kruskal();
        if(ans == infinito){
            cout << -1 << endl;
        }else{
            cout << ans << endl;
        }
    }
    return 0;
}
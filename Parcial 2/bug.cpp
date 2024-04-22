#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
using namespace std;
#define MAX 1000001

vector<int> p(MAX), rango(MAX);

struct Arista{
    int origen;
    int destino;
    int peso;
};

bool cmpPeso(const Arista& a, const Arista& b){
    return a.peso < b.peso;
}

void makeSet(int v){
    p[v] = v;
    rango[v] = 0;
}

int findSet(int v){
    int ans = 0;
    if(v == p[v]){
        ans = v;
    }else{
        p[v] = findSet(p[v]);
        ans = p[v];
    }
    return ans;
}

void unionSet(int u, int v){
    u = findSet(u);
    v = findSet(v);
    if(u != v){
        if(rango[u] < rango[v]){
            u, v = v, u;
        }
        p[v] = u;
        if(rango[u] == rango[v]){
            rango[u]++;
        }
    }
}

int Kruskal(int n, vector<Arista>& aristas, int receiver){
    for (int i = 1; i < n + 1; i++) makeSet(i);
    int numAristas = 0;
    int it = 0;
    sort(aristas.begin(), aristas.end(), cmpPeso);
    vector<Arista> mst(receiver);

    while(it != n && numAristas != receiver)
    {
        if(findSet(aristas[it].origen) != findSet(aristas[it].destino)){
            unionSet(aristas[it].origen, aristas[it].destino);
            //cout << aristas[i].origen << " " << aristas[i].destino << endl;
            //cout << findSet(aristas[i].origen) << " " << findSet(aristas[i].destino) << endl;
            mst[numAristas] = aristas[it];
            numAristas++;
        }
        it++;
        
    }
    
    return mst[receiver-1].peso;
}

int dist(pair<int, int>& A, pair<int, int>& B){
    long long valueA1 = (B.first - A.first);
    long long valueA2 = (B.first - A.first);
    long long valueB1 = (B.second - A.second);
    long long valueB2 = (B.second - A.second);
    long long valueA = valueA1 * valueA2;
    long long valueB = valueB1 * valueB2;
    long long sum = valueA + valueB;
    return ceil(sqrt(sum));
}

int main(){
  //freopen("bugin.txt", "r", stdin);
  //freopen("bugout.txt", "w", stdout);
  int C, receiver, X, Y;
  cin >> C;
  while (C--)
  {
    vector<pair<int, int>> sensors;
    vector<Arista> aristas;
    cin >> receiver;
    cin >> X;
    while(X != -1){
        cin >> Y;
        sensors.push_back(make_pair(X, Y));
        cin >> X;
    }
    for (int i = 1; i < sensors.size() + 1; i++)
    {
        for (int j = i; j < sensors.size() + 1; j++)
        {
            if(i != j){
                Arista vertice;
                vertice.origen = i;
                vertice.destino = j;
                vertice.peso = dist(sensors[i-1], sensors[j-1]);
                aristas.push_back(vertice);
            }
        }
    }
    cout << Kruskal(aristas.size(), aristas, sensors.size() - receiver) << endl;
  }
  
  
  return 0;
}
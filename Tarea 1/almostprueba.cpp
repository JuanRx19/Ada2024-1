#include <iostream>
#include <map>
#include <vector>
#include <string>
using namespace std;

int find(int p, map<int, vector<int>> d){
    int ans = 0;
    if(d[p][0] == p){
        ans = p;
    }else{
        ans = find(d[p][0], d);
    }
    return ans;
}

void Union(int p, int q, map<int, vector<int>> d){
    int padre = find(d[p][0], d);
    int hijo = find(d[q][0], d);
    if(padre != hijo){
        d[q][0] = padre;
        d[hijo][0] = padre;
        d[padre][1] += d[hijo][1];
        d[padre][2] += d[hijo][2];
    }
}

void move(int p, int q, map<int, vector<int>> d){
    int ans = 0;
    int padre = find(d[p][0], d);
    int hijo = find(d[q][0], d);
    if(padre != hijo){
        d[p][0] = hijo;
        d[hijo][1] += p;
        d[padre][1] -= p;
        d[hijo][2] += 1;
        d[padre][2] -= 1;
    }
}

void solve(int n, int m){
    map<int, vector<int>> d;
    int opc, v1, v2, ans = 0;
    for (int num = 1; num < n+1; num++)
    {
        d[num] = {n+num};
    }

    for (int num2 = n+1; num2 <= n*2; num2++)
    {
        d[num2] = {num2, num2-n, 1};
    }

    for (int op = 0; op < m; op++)
    {
        cin >> opc;
        if(opc == 1){
            cin >> v1 >> v2;
            Union(v1, v2, d);
        }else if(opc == 2){
            cin >> v1 >> v2;
            move(v1, v2, d);
        }else if(opc == 3){
            cin >> v1;
            ans = find(v1, d);
            cout << d[ans][2] << " " << d[ans][1] << endl;
        }
    }
}
int main(){
    int n, m;
    while(cin>>n>>m){
        solve(n, m);
    }
}

//Prueba
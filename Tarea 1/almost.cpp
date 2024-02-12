#include <iostream>
#include <map>
#include <vector>
using namespace std;
map<int, vector<int>> d;

int find(int p){
    int ans = 0;
    if(d[p][0] == p){
        ans = p;
    }else{
        ans = find(d[p][0]);
    }
    return ans;
}

void Union(int p, int q){
    int padre = find(d[p][0]);
    int hijo = find(d[q][0]);
    if(padre != hijo){
        d[q][0] = padre;
        d[hijo][0] = padre;
        d[padre][1] += d[hijo][1];
        d[padre][2] += d[hijo][2];
    }
}

void move(int p, int q){
    int ans = 0;
    int padre = find(d[p][0]);
    int hijo = find(d[q][0]);
    if(padre != hijo){
        d[p][0] = hijo;
        d[hijo][1] += p;
        d[padre][1] -= p;
        d[hijo][2] += 1;
        d[padre][2] -= 1;
    }
}

void solve(int n, int m){
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
        scanf("%d", &opc);
        if(opc == 1){
            scanf("%d%d", &v1, &v2);
            Union(v1, v2);
        }else if(opc == 2){
            scanf("%d%d", &v1, &v2);
            move(v1, v2);
        }else if(opc == 3){
            scanf("%d", &v1);
            ans = find(v1);
            printf("%d %d\n", d[ans][2], d[ans][1]);
        }
    }
}
int main(){
    int n, m = 0;
    map<int, vector<int>> d;
    while(scanf("%d%d", &n, &m) != EOF){
        solve(n, m);
    }
}
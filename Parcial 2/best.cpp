#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
using namespace std;
int INF = 1e9;
int mem[105][5005];
int solve(int n, int x, vector<int>& stockholders, int coalitions){
  int ans = 0;
  if(mem[n][coalitions] != -1){
    ans = mem[n][coalitions];
  }else{
    if(n == 0 && coalitions <= 5000){
      ans = INF;
    }else if(coalitions > 5000){
      ans = coalitions;
    }else if(n == x){
      ans = solve(n-1, x, stockholders, coalitions);
    }else{
      ans = min(solve(n-1, x, stockholders, coalitions + stockholders[n-1]), solve(n-1, x, stockholders, coalitions));
    }
  }

  return ans;
}

int main(){
  freopen("bestin.txt", "r", stdin);
  freopen("bestout.txt", "w", stdout);
  int n, x, a, b, ans;
  while (cin >> n >> x, n != 0 && x != 0)
  {
    vector<int> stockholders(n);
    for (int i = 0; i < n; i++)
    {
      scanf("%d.%d", &a, &b);
      stockholders[i] = a * 100 + b;
    }
    
    if(stockholders[x-1] > 5000){
      cout << "100.00" << endl;
    }else{
      memset(mem, -1, sizeof(mem));
      ans = solve(n, x, stockholders, stockholders[x-1]);
      ans = (stockholders[x-1] / ans) * 100;
      cout << stockholders[x-1] << endl;
      printf("%.2lf\n", ans);
    }

  }
  
  return 0;
}
#include <iostream>
#include <map>
#include <vector>
#include <tuple>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <limits>
#define ini vector<int>
int dp[105][2505];
#define INF -2147483648;
using namespace std;

int solve(ini A, int n, int x)
{
    int ans = 0;

    if (dp[n][x] != -1)
    {
        ans = dp[n][x];
    }
    else{
        if(n == 0){
            ans = INF;
        }else if(x <= 0){
            ans = x;
        }else{
            ans = max(solve(A, n-1, x - (A[n-1])), solve(A, n-1, x));
        }
        dp[n][x] = ans;
    }
    return ans;
}
int main()
{
    int C, calories, tam = 0;
    cin >> C;
    while (C != 0)
    {
        memset(dp, -1, sizeof(dp));
        cin >> calories;
        cin >> tam;
        ini A;
        for (int i = 0; i < tam; i++)
        {
            cin >> A[i];
        }

        printf("%d", calories + (solve(A, tam, calories) * -1));
        C--;
    }
}
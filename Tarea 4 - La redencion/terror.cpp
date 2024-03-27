#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(int N, int K, vector<int>& X, vector<int>& Y) {
    int ans = 0;
    for (int i = 0; i < N; i++) 
        Y[i] = Y[i] - X[i];
    sort(Y.begin(), Y.end());

    for (int j = 0; j < N; j++) {
        if (Y[j] < 0 && K != 0) {
            K--;
        } else {
            ans += Y[j];
        }
    }
    
    return ans;
}

int main() {
    //ifstream cin("terrorin.txt");
    //ofstream cout("terrorout.txt");

    int C, N, K, ans;
    cin >> C;
    int iter = 0;
    while (C--) {
        cin >> N >> K;
        vector<int> X(N);
        vector<int> Y(N);
        for (int i = 0; i < N; i++) cin >> X[i]; 
        for (int j = 0; j < N; j++) cin >> Y[j];
        ans = solve(N, K, X, Y);
        if (ans <= 0) {
            cout << "Case " << iter + 1 << ": No Profit" << endl;
        } else {
            cout << "Case " << iter + 1 << ": " << ans << endl;
        }
        iter++;
    }

    //cin.close();
    //cout.close();

    return 0;
}

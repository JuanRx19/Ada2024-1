#include <iostream>
using namespace std;

string solve(int n, int d){
    string ans = "";
    if(n == d){
        ans = "";
    }
    else{
        if(n > d){
            n = n - d;
            ans = "R" + solve(n, d);
        }
        else{
            d = d - n;
            ans = "L" + solve(n, d);
        }
    }
    return ans;
}

int main(){
    int n, d = 0;
    cin >> n, d;
    while (n != 1 || d != 1)
    {
        cout << solve(n, d);
    }
}
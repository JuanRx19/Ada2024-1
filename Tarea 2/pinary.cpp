#include <iostream>
#include <vector>
#include <algorithm>
#define ini vector<vector<int>>
using namespace std;

ini init(ini A, int tam){
    int ant = 1;
    int act = 2;
    int val = 0;
    int pinary = 10;
    for (int i = 0; i < tam; i++)
    {
        val = ant + act;
        ant = act;
        act = val;
        pinary *= 10;
        A.push_back({val, pinary});
    }

    return A;
}

int binarysearch(ini A, int low, int high, int x){
    int ans = 0;
    int mid = 0;
    if(low+1 == high){
        ans = A[low][0];   
    }else{
        mid = low + ((high-low)>>1);
        if(A[mid][0] == x){
            ans = A[mid][0];
        }else if(A[mid][0] < x){
            ans = binarysearch(A,  mid, high, x);
        }else{
            ans = binarysearch(A, low, mid, x);
        }
    }

    return ans;
}

int solve(ini A, int n){
    int ans = 0;
    int nivel = binarysearch(A, 0, A.size() - 1, n);
    printf("%d", nivel);
   /* if(nivel == n){
        ans = nivel[1]
    }else{
        ans += nivel[1] + solve(A, n - nivel[0]);
    }
    return ans*/
}

int main(){
    ini A;
    int T = 0;
    int n = 0;
    A = {{1, 1}, {2, 10}};
    A = init(A, 37);
    cin >> T;
    for (int i = 0; i < T; i++){
        cin >> n;
        printf("%d", solve(A, n));
    }
        
}
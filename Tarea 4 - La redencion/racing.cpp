#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;

void convert(vector<int>& tianJi, vector<int>& king, deque<int>& tianQueue, deque<int>& kingQueue, int N){
    for(int i = 0; i < N; i++) tianQueue.push_back(tianJi[i]);
    for(int i = 0; i < N; i++) kingQueue.push_back(king[i]);
}

int solve(vector<int>& tianJi, vector<int>& king, int N){
    int ans = 0;
    deque<int> tianQueue;
    deque<int> kingQueue;
    convert(tianJi, king, tianQueue, kingQueue, N);
    while(N--){
        if(tianQueue.back() > kingQueue.back()){
            ans+=200;
            tianQueue.pop_back();
            kingQueue.pop_back();
        }else if(tianQueue.back() < kingQueue.back()){
            ans-=200;
            kingQueue.pop_back();
            tianQueue.pop_front();
        }else{
            if(tianQueue.front() > kingQueue.front()){
                ans+=200;
                tianQueue.pop_front();
                kingQueue.pop_front();
            }else if(kingQueue.back() != tianQueue.front()){
                ans-=200;
                kingQueue.pop_back();
                tianQueue.pop_front();
            }
        }
    }
   
   return ans;
}

int main(){
    //freopen("racingin.txt", "r", stdin);
    //freopen("racingout.txt", "w", stdout);
    int N;
    cin >> N;
    while(N != 0){
        vector<int> tianJi(N);
        vector<int> king(N);
        for(int i = 0; i < N; i++) cin >> tianJi[i];
        for(int i = 0; i < N; i++) cin >> king[i];
        sort(tianJi.begin(), tianJi.end());
        sort(king.begin(), king.end());
        cout << solve(tianJi, king, N) << endl;
        cin >> N;
    }
    return 0;
}
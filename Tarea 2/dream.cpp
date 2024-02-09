#include <iostream>
#include <vector>
#include <algorithm>
#define ini vector<int>
using namespace std;

int binarysearchleft(ini &val, int low, int high, int x){
    int ans = 0;
    int mid = 0;
    if(low+1 == high){
        if(val[low] == x){
            ans = 1;
        }
    }else{
        mid = low + ((high-low)>>1);
        if(val[mid] == x){
            ans = ((high - mid)) + binarysearchleft(val, low, mid, x);
        }
        else{
            ans = binarysearchleft(val, mid, high, x);
        }
    }
    return ans;
}

int binarysearchright(ini &val, int low, int high, int x){
    int ans = 0;
    int mid = 0;
    if(low+1 == high){
        if(val[high] == x){
            ans = 1;
        }
    }
    else{
        mid = low + ((high-low)>>1);
        if(val[mid] == x){
            ans = ((mid - low)) + binarysearchright(val, mid, high, x);
        }
        else{
            ans = binarysearchright(val, low, mid, x);
        }
    }
    return ans;
}

void solve(int T){
    ini val;
    int num = 0;
    for (int i = 0; i < T; i++)
    {
        scanf("%d", &num);
        val.push_back(num);
    }
    sort(val.begin(), val.end());
    int ans = 0;
    int mid = 0 + (((T - 1) - 0)>>1);
    if(T > 2){
        if(T % 2 != 0){
            ans += binarysearchleft(val, 0, mid, val[mid]);
            ans += binarysearchright(val, mid, T - 1, val[mid]);
            printf("%d %d 1\n", val[mid], ans + 1);
        }
        else{
            ans += 1 + binarysearchleft(val, 0, mid, val[mid]);
            ans += 1 + binarysearchright(val, mid + 1, T - 1, val[mid + 1]);
            printf("%d %d %d\n", val[mid], ans, val[mid + 1] - val[mid] + 1);
        }
    }  
    else{
        if(T == 1){
            printf("%d %d %d\n", val[mid], 1, 1);
        }else{
            printf("%d 2 %d\n", val[mid], val[mid + 1] - val[mid] + 1);
        }
    }
}

int main(){
    int T;
    while(cin >> T){
        solve(T);
    }
}
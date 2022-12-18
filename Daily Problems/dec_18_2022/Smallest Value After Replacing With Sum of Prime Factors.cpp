#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int pf(int n){
        int ans = 0;
        while(n%2 == 0){
            ans += 2;
            n = n/2;
        }
        for(int i=3;i<=sqrt(n);i+=2){
            while(n%i == 0){
                ans += i;
                n = n/i;
            }
        }
        if(n>2) ans += n;
        return ans;
    }
    int smallestValue(int n) {
        while(true){
            int prev = n;
            n = pf(n);
            if(n==prev) break;  // prime no. found
        }
        return n;
    }
};
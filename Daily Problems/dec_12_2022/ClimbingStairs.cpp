#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    int fun(int n, vector<int>& dp){
        if(n<0) return 0;
        if(n==1 || n==0) return 1;
        if(dp[n]!=0) return dp[n];
        return dp[n] = fun(n-1,dp) + fun(n-2,dp);
    }
    int climbStairs(int n) {
        vector<int> dp(n+1);
        return fun(n,dp);
    }
};
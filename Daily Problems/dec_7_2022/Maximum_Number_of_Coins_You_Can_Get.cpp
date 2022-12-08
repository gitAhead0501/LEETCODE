#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxCoins(vector<int>& piles) {
        int n = piles.size();
        sort(piles.begin(),piles.end());
        int x = n/3,sm=0;
        for(int i=x;i<n-1;i+=2) sm += piles[i];
        return sm;
    }
};
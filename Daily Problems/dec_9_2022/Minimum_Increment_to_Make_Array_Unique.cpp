#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int prev=0,ans=0;
        for(auto n:nums){
            ans += max(prev-n,0);
            prev = max(prev,n)+1;
        }
        return ans;
    }
};

// TC: O(n*logn)

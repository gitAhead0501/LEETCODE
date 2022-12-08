#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(begin(nums),end(nums));
        int mx = 0;
        int n = nums.size();
        for(int i=0;i<n;i++){
            mx = max(mx, nums[i]+nums[n-i-1]);
        }
        return mx;
    }
};
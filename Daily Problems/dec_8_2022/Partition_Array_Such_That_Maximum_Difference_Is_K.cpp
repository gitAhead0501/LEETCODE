#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        sort(begin(nums),end(nums));
        int count = 1;
        int start = nums[0];
        for(int i=0;i<nums.size();i++){
            if(nums[i] > start+k){
                start = nums[i];
                count++;
            }
        }
        return count;
    }
};
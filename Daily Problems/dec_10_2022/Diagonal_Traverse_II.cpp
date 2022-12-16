#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& nums) {        
        vector<vector<int>> pre_final;
        for(int i=0;i<nums.size();i++){
            for(int j=0;j<nums[i].size();j++){
                if(pre_final.size()<=(i+j)) pre_final.push_back({nums[i][j]});
                else pre_final[i+j].emplace_back(nums[i][j]);
            }
        }
        vector<int> final;
        for(int i=0;i<pre_final.size();i++){
            for(int j=pre_final[i].size()-1;j>=0;j--){
                final.emplace_back(pre_final[i][j]);
            }
        }
        return final;
    }
};
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        int n = nums.size(), m = l.size();
        vector<bool>ans;
        for(int i=0;i<m;i++){
            vector<int> temp;
            for(int j=l[i];j<=r[i];j++){
                temp.emplace_back(nums[j]);
            }
            sort(begin(temp),end(temp));
            if(temp.size()==1){
                ans.emplace_back(true);
                continue;
            }
            bool ok = true;
            int d = temp[1] - temp[0];
            for (int k=2;k<temp.size();k++){
                if (temp[k] - temp[k-1] != d){
                    ok = false; break;
                }
            }
            (ok == true ? ans.emplace_back(true) : ans.emplace_back(false));
        }
        return ans;
    }
};
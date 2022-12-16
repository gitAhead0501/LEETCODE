#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        // sort(begin(intervals),end(intervals));
        unordered_map<int,int> mp;
        int n = intervals.size();
        vector<int> vec;
        for(int i=0;i<n;i++){
            vec.emplace_back(intervals[i][0]);
            mp[intervals[i][0]] = i;
        }
        vector<int> ans;
        sort(begin(vec),end(vec));
        for(auto it:intervals){
            int x = it[1];
            int val = lower_bound(begin(vec),end(vec),x) - begin(vec);
            if(val==vec.size())  ans.emplace_back(-1);
            else ans.emplace_back(mp[vec[val]]);
            // else cout << val << " " << vec[val] << " " << mp[vec[val]] << endl;
        }
        return ans;
    }
};

// Time Complexity
/*

O(n*logn)  -  sorting
O(n*logn)  -  traversing in intervals and using lower_bound

// Space Complexity : O(n) for map and O(n) for returned vector


*/
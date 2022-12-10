#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        vector<vector<int>> ans; unordered_map<int,int> mp;
        vector<int> hash_vec(int(1e5+10));
        for(auto it:matches){ hash_vec[it[1]]++; mp[it[1]]++; }
        vector<int> a,b;
        for(auto it:matches){ if(hash_vec[it[0]]==0){ a.emplace_back(it[0]); hash_vec[it[0]]++; } }
        for(auto it:mp){ if(it.second==1) b.emplace_back(it.first); }
        sort(begin(a),end(a)); sort(begin(b),end(b));
        ans.emplace_back(a); ans.emplace_back(b);
        return ans;      
    }
};
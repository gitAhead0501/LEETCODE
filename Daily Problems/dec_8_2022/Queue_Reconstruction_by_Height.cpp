#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        int n = people.size();
        sort(people.begin(), people.end(), [](vector<int>&a, vector<int>&b){ 
            if(a[0]==b[0]) return a[1] < b[1];
            return a[0]>b[0];
         });
        for(auto it:people){
            cout<<it[0]<<" "<<it[1]<<endl;
        }
        vector<vector<int>> ans;
        for(auto it:people){
            ans.insert(begin(ans)+it[1],it);
        }
        return ans;
    }
};

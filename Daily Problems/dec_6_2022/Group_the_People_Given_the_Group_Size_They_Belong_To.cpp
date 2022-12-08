#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        unordered_map<int,vector<int>> mp;
        int n = groupSizes.size();
        for(int i=0;i<n;i++){
            mp[groupSizes[i]].push_back(i);
        }
        vector<vector<int>> vec;
        for(auto it:mp){
            if(it.second.size() > it.first){
                vector<int> temp;
                int k=1;
                for(int i=0;i<it.second.size();i++){
                    if(k==it.first){
                        k=1;
                        temp.push_back(it.second[i]);
                        vec.push_back(temp);
                        temp.clear();
                    }
                    else{
                        temp.push_back(it.second[i]);
                        k++;
                    }
                }
            }
            else{
                vec.push_back(it.second);
            }
        }
        return vec;
    }
};
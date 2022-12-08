#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
        vector<int> ans;
        for(int i=0;i<queries.size();i++){
            int insiders=0;
            for(int j=0;j<points.size();j++){
                float dist = sqrt(pow(queries[i][0]-points[j][0] , 2) + pow(queries[i][1]-points[j][1] , 2));
                if(dist<=queries[i][2])
                    insiders++;
            }
            ans.push_back(insiders);
        }
        return ans;
    }
};
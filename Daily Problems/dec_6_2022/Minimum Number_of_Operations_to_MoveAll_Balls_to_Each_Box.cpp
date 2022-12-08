#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    vector<int> minOperations(string boxes) {
        int leftOnes=0, leftCost=0, rightOnes=0, rightCost=0,n=boxes.size();
        vector<int> ans(n);
        for(int i=1;i<n;i++){
            if(boxes[i-1]=='1') leftOnes++;
            leftCost += leftOnes;
            ans[i] = leftCost;
        }
        for(int i=n-2;i>=0;i--){
            if(boxes[i+1]=='1') rightOnes++;
            rightCost += rightOnes;
            ans[i] += rightCost;
        }
        return ans;
    }
};
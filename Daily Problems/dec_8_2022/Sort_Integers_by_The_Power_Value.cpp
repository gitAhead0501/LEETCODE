#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
	int compute(int i){
		if(i==1) return 0;
		if(i&1){
			return 1 + compute(i*3+1);
		}
		return 1 + compute(i/2);
	}
    int getKth(int lo, int hi, int k) {
        vector<pair<int,int>> vec;
    	for(int i=lo;i<=hi;i++){
            vec.push_back({compute(i),i});
        }
        sort(begin(vec),end(vec));
        return vec[k-1].second;
    }
};
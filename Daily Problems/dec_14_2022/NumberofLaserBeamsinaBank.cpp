#include<bits/stdc++.h>
using namespace std;


#define all(x) begin(x), end(x)
class Solution {
public:
    int char_count_string(char c, string s){ return count(all(s),c); }
    int numberOfBeams(vector<string>& bank) {
        int n=bank.size(), count = 0, lastOne=0;
        for(int i=0;i<n;i++){
            int ccs = char_count_string('1',bank[i]);
            if(ccs!=0){
                count += ccs*lastOne;
                lastOne = ccs;
            }
        }
        return count;
    }
};
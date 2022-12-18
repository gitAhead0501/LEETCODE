#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int similarPairs(vector<string>& words) {
        unordered_map<string,int> mp;
        int count = 0;
        for(int i=0;i<words.size();i++){
            string t = "";
            unordered_set<char> st;
            for(int j=0;j<words[i].size();j++){
                if(st.find(words[i][j])!=st.end()) continue;
                else{
                    t += words[i][j];
                    st.insert(words[i][j]);
                }
            }
            
            sort(begin(t),end(t));
            words[i] = t;
        }   
        for(int i=0;i<words.size()-1;i++){
            for(int j=i+1;j<words.size();j++){
                if(words[i]==words[j]) count++;
            }
        }
        return count;
    }
};
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<long long> st;
        for(auto t:tokens){
            if(t.size()>1 || isdigit(t[0])) st.push(stoi(t));
            else{
                auto b = st.top(); st.pop();
                auto a = st.top(); st.pop();
                if(t=="+") a = (a+b);
                else if(t=="*") a = (long long)(a*b);
                else if(t=="-") a = (a-b);
                else if(t=="/") a = (a/b);
                st.push(a);
            }
        }
        return st.top();
    }
};
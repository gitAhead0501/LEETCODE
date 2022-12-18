#include<bits/stdc++.h>
using namespace std;

class MyQueue {
public:
    stack<int> st1, st2;
    MyQueue() {
        
    }
    
    void push(int x) {
        st1.push(x);
        st2.push(x);
    }
    
    int pop() {
        vector<int> temp;
        while(!st2.empty()){
            temp.emplace_back(st2.top());
            st2.pop();
        }
        int n = temp.size();
        for(int i=n-2;i>=0;i--) st2.push(temp[i]);
        return temp[n-1];
    }
    
    int peek() {
        vector<int> temp;
        while(!st2.empty()){
            temp.emplace_back(st2.top());
            st2.pop();
        }
        int n = temp.size();
        for(int i=n-1;i>=0;i--) st2.push(temp[i]);
        return temp[n-1];
    }
    
    bool empty() {
        return st2.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
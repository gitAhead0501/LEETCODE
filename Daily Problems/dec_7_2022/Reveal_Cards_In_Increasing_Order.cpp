#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        sort(rbegin(deck),rend(deck));
        deque<int> dq;
        dq.push_back(deck[0]);
        for(int i=1;i<deck.size();i++){
            dq.push_front(dq.back());
            dq.pop_back();
            dq.push_front(deck[i]);
        }
        vector<int> vec;
        while(!dq.empty()){
            vec.emplace_back(dq.front());
            dq.pop_front();
        }
        return vec;
    }
};
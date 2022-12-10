#include<bits/stdc++.h>
using namespace std;


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> dfs(vector<int>& vec, TreeNode* root){
        stack<TreeNode*> st;
        TreeNode* curr = root;
        while(curr!=NULL || !st.empty()){
            while(curr!=NULL){
                st.push(curr);
                curr = curr->left;
            }
            curr = st.top();
            st.pop();
            if(curr->left==NULL && curr->right==NULL) vec.emplace_back(curr->val);
            curr = curr->right;
        }
        // for(auto v:vec) cout<<v<<" ";
        // cout<<endl;
        return vec;
    }
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> vec;
        vector<int> a = dfs(vec,root1);
        vec.clear();
        vector<int> b = dfs(vec,root2);
        return a==b;
    }
};
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
    vector<int> treeValuesInorder(vector<int>& vec, TreeNode* root){
        stack<TreeNode*> st;
        TreeNode* curr = root;
        while(curr!=NULL || !st.empty()){
            while(curr!=NULL){
                st.push(curr);
                curr = curr->left;
            }
            curr = st.top();
            st.pop();
            vec.emplace_back(curr->val);
            curr = curr->right;
        }
        return vec;
    }
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        vector<int> vec;
        vector<int> a = treeValuesInorder(vec,root1);
        vector<int> b = treeValuesInorder(vec,root2);
        sort(begin(vec),end(vec));
        return vec;
    }
};
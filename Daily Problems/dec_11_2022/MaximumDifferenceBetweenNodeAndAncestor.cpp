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
    int fun(int currMin, int currMax, TreeNode* root){
        if(root==NULL) return currMax-currMin;
        currMin = min(currMin,root->val);
        currMax = max(currMax,root->val);
        int left = fun(currMin,currMax,root->left);
        int right = fun(currMin,currMax,root->right);
        return max(left,right);
        
    }
    int maxAncestorDiff(TreeNode* root) {
        return fun(root->val,root->val,root);
    }
};
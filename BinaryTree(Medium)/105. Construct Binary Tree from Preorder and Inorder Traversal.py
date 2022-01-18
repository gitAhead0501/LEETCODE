"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Constraints:
A) 1 <= preorder.length <= 3000
B) inorder.length == preorder.length
C) -3000 <= preorder[i], inorder[i] <= 3000
D) preorder and inorder consist of unique values.
E) Each value of inorder also appears in preorder.
F) preorder is guaranteed to be the preorder traversal of the tree.
G) inorder is guaranteed to be the inorder traversal of the tree.

Approach: We are given preorder so the first element of preorder array will be the root of the tree, find it's index in inorder array. The left part of the array with this index will be the inorder for left child of the tree and right part will be the right child of the tree

"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {}
        for i,x in enumerate(inorder):
            inorder_index_map[x] = i
        
        preorder_index = 0
            
        def buildingTree(left,right):
            nonlocal preorder_index
            if left>right:
                return None
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            preorder_index += 1
            root.left = buildingTree(left,inorder_index_map[root_value]-1)
            root.right = buildingTree(inorder_index_map[root_value]+1,right)
            return root
        
        return buildingTree(0,len(preorder)-1)
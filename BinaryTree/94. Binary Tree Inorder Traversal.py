"""
94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Approach : Just do the inorder traversal and return

"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        return inorder(root)
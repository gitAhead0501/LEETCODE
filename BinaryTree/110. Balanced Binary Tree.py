"""
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
A binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Constraints:
A) The number of nodes in the tree is in the range [0, 5000].
B) -104 <= Node.val <= 104

Approach: Do DFS, and recursively check from bottom if abs diff between height of left subtree and right subtree is > 1
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        flag = 1
        def height(root):
            nonlocal flag
            if flag == 0:
                return False
            if not root:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            if abs(lh-rh) > 1:
                flag = 0
            return max(lh,rh)+1
        height(root)
        return flag
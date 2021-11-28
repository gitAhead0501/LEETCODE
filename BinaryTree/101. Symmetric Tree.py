"""
101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Constraints:
A) The number of nodes in the tree is in the range [1, 1000].
B) -100 <= Node.val <= 100

Approach : Recursively check for equal nodes in both left and right subtrees
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val == right.val:
                lh = dfs(left.left,right.right)
                rh = dfs(left.right,right.left)
                return lh and rh
            return False
        return dfs(root.left,root.right)
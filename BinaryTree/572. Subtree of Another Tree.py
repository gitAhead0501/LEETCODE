"""
572. Subtree of Another Tree
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-10**4 <= root.val <= 10**4
-10**4 <= subRoot.val <= 10**4


Approach: Create a dfs function for main function for searching the subroot in the root tree
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self,node1,node2):
            if not node1 and not node2:
                return True
            if (not node1 and node2) or (not node2 and node1):
                return False
            if node1.val != node2.val:
                return False
            return self.dfs(node1.left,node2.left) and self.dfs(node1.right,node2.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.dfs(root,subRoot):
            return True
        lh = False
        rh = False
        if root.left:
            lh = self.isSubtree(root.left,subRoot)
        if root.right:
            rh = self.isSubtree(root.right,subRoot)
        return lh or rh
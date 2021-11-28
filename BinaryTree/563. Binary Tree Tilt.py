"""
563. Binary Tree Tilt
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if there the node does not have a right child.

Constraints:
A) The number of nodes in the tree is in the range [0, 104].
B) -1000 <= Node.val <= 1000


Approach:
If there is no left child and right return 0 i.e. if node is None then return 0
So, we calculate left and right tilt absolute differences and recursively return the tilt from left side right and node's value

"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tilt = 0
        def dfs(node):
            if not node:
                return 0
            lh = dfs(node.left)
            rh = dfs(node.right)
            self.tilt += abs(lh-rh)
            return lh + rh + node.val
        dfs(root)
        return self.tilt
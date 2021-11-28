"""
226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

Constraints:
A) The number of nodes in the tree is in the range [0, 100].
B) -100 <= Node.val <= 100

Aprroach: Just swap the left node and right node and recursively call for left and right subtrees
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
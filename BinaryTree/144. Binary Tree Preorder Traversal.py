"""
144. Binary Tree Preorder TraversalGiven the root of a binary tree, return the preorder traversal of its nodes' values.

Constraints:
A) The number of nodes in the tree is in the range [0, 100].
B) -100 <= Node.val <= 100

Approach : Just return the preorder traversal
"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
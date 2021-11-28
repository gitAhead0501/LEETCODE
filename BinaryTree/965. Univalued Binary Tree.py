"""
965. Univalued Binary Tree
A binary tree is uni-valued if every node in the tree has the same value.
Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

Constraints:
A) The number of nodes in the tree is in the range [1, 100].
B) 0 <= Node.val < 100

Approach 1: Recursively check if the root.val is different than any of the node's values and return True or False accordingly
Approach 2: Store each node's value and check the length of set of all values in node

Follow Up : If the following program contains more than 1 approaches, consider commenting the others while using one method
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1)
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def helper(root,val):
            if not root:
                return True
            if root.val != val:
                return False
            return helper(root.left,val) and helper(root.right,val)
        return helper(root,root.val)

# 2)
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        return len(set(inorder(root))) == 1
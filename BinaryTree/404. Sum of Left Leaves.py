"""
404. Sum of Left Leaves
Given the root of a binary tree, return the sum of all left leaves.

Constraints:
A) The number of nodes in the tree is in the range [1, 1000].
B) -1000 <= Node.val <= 1000

Approach: Only add left leaves i.e. node's whose left exist and whose left's left and left's right are None

"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
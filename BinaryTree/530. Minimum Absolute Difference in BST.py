"""
530. Minimum Absolute Difference in BST
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Constraints:
A) The number of nodes in the tree is in the range [2, 10**4].
B) 0 <= Node.val <= 10**5

Approach:
Do Inorder Traversal : which is sorted of BST : Run a loop and find min consecutive difference and return the min result

"""

# Definition for a binary tree node.
from typing import Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        ans = dfs(root)
        res = math.inf
        for i in range(len(ans)-1):
            if abs(ans[i]-ans[i+1]) <= res:
                res = abs(ans[i]-ans[i+1])
        return res
"""
671. Second Minimum Node In a Binary Tree
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.


Constraints:
A) The number of nodes in the tree is in the range [1, 25].
B) 1 <= Node.val <= 231 - 1
C) root.val == min(root.left.val, root.right.val) for each internal node of the tree.


Approach1: Store all the nodes value and return sorted distinct value i.e. at index 1 if the length is > 1 else -1
Approach2: Compare the nodes values and store only the 2nd minimum node value
"""

# Definition for a binary tree node.
from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1)
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        ans = sorted(set(dfs(root)))
        if len(ans) > 1:
            return ans[1]
        return -1

# 2)
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.ans = math.inf
        min1 = root.val

        def dfs(node):
            nonlocal min1
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.ans if self.ans < math.inf else -1
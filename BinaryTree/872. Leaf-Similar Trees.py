"""
872. Leaf-Similar Trees
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

#                                           3
#                                    5            1
#                                 6     2      9     8
#                                     7   4


For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Approach 1: Do DFS and storing in list the leaf's value and then for both trees compare the final leaf sequence
Approach 2: DO DFS and rather storing , yield values(using yield function) and directly compare
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        def dfs(root,arr):
            if not root:
                return
            if not root.left and not root.right:
                arr += [root.val]
            if root.left:
                dfs(root.left,arr)
            if root.right:
                dfs(root.right,arr)
        dfs(root1,arr1)
        dfs(root2,arr2)
        return arr1 == arr2


# 2)
class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))
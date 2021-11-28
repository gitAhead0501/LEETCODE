"""
993. Cousins in Binary Tree
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.


Constraints:

The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.


Approach: Define a function with node, parent, depth and value : For both x and y check if depth is same and parent aren't same
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node, par, dep, val):
            if not node: return
            if node.val == val: return dep, par
            return dfs(node.left, node, dep + 1, val) or dfs(node.right, node, dep + 1, val)
        
        dep_x, par_x = dfs(root, None, 0, x)
        dep_y, par_y = dfs(root, None, 0, y)

        return dep_x == dep_y and par_x != par_y
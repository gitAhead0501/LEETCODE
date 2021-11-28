"""
Level : Easy

1469. Find All The Lonely Nodes
In a binary tree, a lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.
Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. Return the list in any order.

Constraints:
A) The number of nodes in the tree is in the range [1, 1000].
B) Each node’s value is between [1, 10^6].

Approach: Make a list of the nodes whose parents have only one child
If root's left is none but not right , then add root's left
Similarly, if root's right is none but not left, then add root's right
Do this recursively for left and right subtrees
"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def dfs(root):
            if root:
                if not root.left and root.right:
                    self.res.append(root.right)
                if not root.right and root.left:
                    self.res.append(root.left)
                if root.left:
                    dfs(root.left)
                if root.right:
                    dfs(root.right)
        dfs(root)
        return self.res
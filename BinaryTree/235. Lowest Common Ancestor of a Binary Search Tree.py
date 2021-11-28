"""
235. Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Constraints:
A) The number of nodes in the tree is in the range [2, 105].
B) -109 <= Node.val <= 109
C) All Node.val are unique.
D) p != q
E) p and q will exist in the BST.

Approach:
CASE 1: p and q are on opposite sides, then return root (as it is the LCA (lowest common ancestor) ).
CASE 2: p and q are on left sides, then recursively check case 1 and case, case 2 and case 3 for the left subtree.
CASE 3: p and q are on right sides, then recursively check case 1 and case, case 2 and case 3 for the right subtree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
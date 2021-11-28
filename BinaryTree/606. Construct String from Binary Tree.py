"""
606. Construct String from Binary Tree
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.
Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

Constraints:
A) The number of nodes in the tree is in the range [1, 104].
B) -1000 <= Node.val <= 1000

Approach 1: Using Recursion
We need to do preorder traversal and put braces in appropriate positions.
For every node encountered, the following cases are possible:
# NOTE : IN PREORDER TRAVERSAL : LEFT CHILD IS PREFERED OVER RIGHT CHILD
CASE 1: If both left and right child do not exist, we need to do nothing just add string type casted node value
CASE 2: Left child exists but not right child, we need to add str(node's value) and put braces between recursive calling function for left child
CASE 3: Both left and right child exist, adding node's val and put braces between recursive calling function for both left and right child
CASE 4: Obvious case : If node itself doesn't exist just simply return an empty string. ("")

Approach 2: Using Stack
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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        if not root.left and not root.right:
            return str(root.val)
        if not root.right:
            return str(root.val) + "(" + self.tree2str(root.left) + ")"
        return str(root.val) + "(" + self.tree2str(root.left) + ")(" + self.tree2str(root.right) + ")"
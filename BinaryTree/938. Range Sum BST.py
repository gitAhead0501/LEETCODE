'''
Level : Easy

938. Range Sum BST
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Constraints:
A) The number of nodes in the tree is in the range [1, 2 * 104].
B) 1 <= Node.val <= 105
C) 1 <= low <= high <= 105
D) All Node.val are unique.


Approach : Direct Recursion of the question's function  OR make a recursive function and then evaluate
consider base case: if root is none , return 0
if the node value is inclusive in the range [low,high] then add it to the result
recursively call for left subtree and right subtree
compute the final result from subtrees and return
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        if low <= root.val <= high:
            return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
        else:
            return self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
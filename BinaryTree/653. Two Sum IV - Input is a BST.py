"""
653. Two Sum IV - Input is a BST
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

Constraints:
A) The number of nodes in the tree is in the range [1, 104].
B) -104 <= Node.val <= 104
C) root is guaranteed to be a valid binary search tree.
D) -105 <= k <= 105


Approach: Create an hash table and store diff of k and node's value and then check if that diff is available in Tree or not
Here, the 2nd method is wrong and won't work due to duplicacy of search function. It counts itself if the difference is same as the node's val
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.h = {}
        def dfs(node):
            if not node:
                return False
            if (node.val) in self.h:
                return True
            self.h[k-node.val] = 0
            return dfs(node.left) or dfs(node.right)
        return dfs(root)

'''
HERE, THE bsearch function returns True if there is only root node and the diff of root's value and k is same as node's val.
If corrected, then it gives the same wrong answer if this thing occurs again in subtrees.
        def bsearch(node,v):
            if not node:
                return False
            if v == node.val:
                return True
            if v<node.val:
                return bsearch(node.left,v)
            return bsearch(node.right,v)
        def dfs(node):
            if not node:
                return False
# if k-node.val != node.val:
#   res = bsearch(node,k-node.val)
# same problems occurs in subtreees  if this snippet  is included in the main program
            res = bsearch(node,k-node.val)
            if res:
                return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
'''
"""
100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Constraints:
A) The number of nodes in both trees is in the range [0, 100].
B) -104 <= Node.val <= 10**4

Approach: Just check every node and compare in both trees simultaneously and return False wherever they do not match
Methods: BFS and Recursion

"""

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p,q):
            if not p and not q:
                return True
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        dq = deque([(p,q)])
        while dq:
            p,q = dq.popleft()
            if not check(p,q):
                return False
            if p:
                dq.append((p.left,q.left))
                dq.append((p.right,q.right))
        return True
'''
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
'''
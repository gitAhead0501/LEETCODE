"""
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Constraints:
A) The number of nodes in the tree is in the range [0, 105].
B) -1000 <= Node.val <= 1000


Approach: Do BFS, and return depth when the nearest node to root has both left and right child None.
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dq = deque([root])
        depth = 0
        while dq:
            depth += 1
            n = len(dq)
            while n:
                node = dq.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                n-=1
        return -1
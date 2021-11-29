"""
1302. Deepest Leaves Sum
Given the root of a binary tree, return the sum of values of its deepest leaves.

Constraints:
A) The number of nodes in the tree is in the range [1, 104].
B) 1 <= Node.val <= 100


Approach1: DFS : And check if the depth of the tree is same as height of the tree and add those node's values
Approach2: BFS : For every level, determine the sum of its node's value and return the last overwritten sum

"""


from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1)
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def height(root):
            if not root:
                return 0
            return max(height(root.left),height(root.right)) + 1
        
        def dfs(root,depth):
            if not root:
                return
            if depth == max_depth:
                self.total += root.val
            depth += 1
            dfs(root.left,depth)
            dfs(root.right,depth)
            
        self.total = 0
        max_depth = height(root)
        dfs(root,1)
        return self.total


# 2)
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dq = deque([])
        dq.append(root)
        while dq:
            sum = 0
            n = len(dq)
            for i in range(n):
                node = dq.popleft()
                sum += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return sum

"""
637. Average of Levels in Binary Tree
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
Answers within 10^(-5) of the actual answer will be accepted.

Constraints:
A) The number of nodes in the tree is in the range [1, 10**4].
B) -2**31 <= Node.val <= 2**31 - 1

Approach 1: Do BFS , at each level add all the node's val and take their avg by dividing the no. of nodes in that level
Approach 2: Do DFS, make a defaultdict for storing levelSum and levelCount and then computing the average
"""

from collections import defaultdict, deque
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1)
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def dfs(node,level):
            nonlocal levelSum, levelCount
            if node:
                levelSum[level] += node.val
                levelCount[level] += 1
                dfs(node.left,level+1)
                dfs(node.right,level+1)
        levelSum = defaultdict(lambda : 0)
        levelCount = defaultdict(lambda : 0)
        dfs(root,0)
        return [ levelSum[level]/levelCount[level] for level in levelSum ]


# 2)
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return
        q = deque([root])
        res = []
        while q:
            lvlsum = 0
            lvlnodes = len(q)
            n = lvlnodes
            while n:
                node = q.popleft()
                lvlsum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                n -=1
            res.append(lvlsum/lvlnodes)
        return res
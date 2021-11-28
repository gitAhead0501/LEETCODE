"""
501. Find Mode in Binary Search Tree
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


Constraints:
A) The number of nodes in the tree is in the range [1, 104].
B) -105 <= Node.val <= 105

Approach: Use hashtable to store the most frequent occured item and return it
"""

from collections import Counter
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        ans = dfs(root)
        if ans:
            hmap = Counter(ans)
            max_ = max(hmap.values())
            return [k for k,v in hmap.items() if max_==v]
        return ans
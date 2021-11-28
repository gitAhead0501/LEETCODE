"""

257. Binary Tree Paths
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

Constraints:
A) The number of nodes in the tree is in the range [1, 100].
B) -100 <= Node.val <= 100

Approach: Traverse from root to leaf and append each node's value in path to a list
Modify it as per given condition given via converting it into string and return the string
"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root,path,res):
            path.append(root.val)
            if not root.left and not root.right:
                res.append([item for item in path])
            if root.left: helper(root.left, path, res)
            if root.right: helper(root.right, path, res)
            path.pop()
            return
        path, res = [],[]
        helper(root,path,res)
#       print(res)
        for i in range(len(res)):
            ans = ""
            for j in range(len(res[i])-1):
                ans += str(res[i][j]) + "->"
            ans += str(res[i][len(res[i])-1])
            res[i] = ans
        return res
"""
1022. Sum of Root To Leaf Binary Numbers
You are given the root of a binary tree where each node has a value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.

Constraints:
A) The number of nodes in the tree is in the range [1, 1000].
B) Node.val is 0 or 1.

Approach 1: Using Bit Manipulation
Approach 2: Traverse from root to leaf and add every node's value in the path to a local string ans and at leaf convert it into decimal and store it. A function is need to convert binary to decimal

"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2)
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

# BINARY TO DECIMAL CONVERSION FUNCTION

        def binaryToDecimal(binary):
            binary1 = binary
            decimal, i, n = 0, 0, 0
            while(binary != 0):
                dec = binary % 10
                decimal = decimal + dec * pow(2, i)
                binary = binary//10
                i += 1
            return decimal

        res = []
        def dfs(root,add):
            nonlocal res
            add += str(root.val)
            if not root.left and not root.right:
                ans = binaryToDecimal(int(add))
                res.append(ans)
                return
            if root.left:
                dfs(root.left,add)
            if root.right:
                dfs(root.right,add)
        dfs(root,"")
        return sum(res)
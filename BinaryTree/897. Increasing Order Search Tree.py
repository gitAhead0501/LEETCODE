"""
897. Increasing Order Search Tree
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

Constraints:
A) The number of nodes in the given tree will be in the range [1, 100].
B) 0 <= Node.val <= 1000

Approach:
1) Do inorder and yield values from this function and create a new tree with them
2) Do inorder and link the new Tree in function itself
3) Do inorder and store the values in stack and form a new tree by popping

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1)
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right

# 2)
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                if node.left:
                    inorder(node.left)
                node.left = None
                self.curr.right = node
                self.curr = node
                inorder(node.right)
        ans = self.curr = TreeNode(None)
        inorder(root)
        return ans.right

# 3)
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.stack = []
        def inorder(node):
            if node:
                if node.left:
                    inorder(node.left)
                self.stack.append(node.val)
                if inorder.right:
                    inorder(node.right)

        ans = cur = TreeNode(None)
        for each in self.stack:
            cur.right = TreeNode(each)
            cur = cur.right
        return ans.right
"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Constraints:
A) 1 <= inorder.length <= 3000
B) postorder.length == inorder.length
C) -3000 <= inorder[i], postorder[i] <= 3000
D) inorder and postorder consist of unique values.
E) Each value of postorder also appears in inorder.
F) inorder is guaranteed to be the inorder traversal of the tree.
G) postorder is guaranteed to be the postorder traversal of the tree.

Approach: We are given postorder so the last element of postorder array will be the root of the tree, find it's index in inorder array. The left part of the array with this index will be the inorder for left child of the tree and right part will be the right child of the tree

"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.postIdx = len(postorder)-1
        def build(inStart, inEnd):
            if inStart > inEnd: return None
            root = TreeNode(postorder[self.postIdx])
            self.postIdx -= 1
            root.right = build(inorder.index(root.val)+1, inEnd)
            root.left  = build(inStart, inorder.index(root.val)-1)
            return root
        return build(0, len(inorder)-1)
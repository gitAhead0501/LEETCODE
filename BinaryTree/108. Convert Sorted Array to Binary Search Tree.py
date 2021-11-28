"""
108. Convert Sorted Array to Binary Search Tree
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Constraints:
A) 1 <= nums.length <= 104
B) -104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.


Approach: Mid of the array is always the root node in each subtree following the main root.
Recursively create a tree with node as mid of array and call left and right of mid of the array
"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l,r):
            if l>r:
                return None
            mid = l + (r-l)//2
            root = TreeNode(nums[mid])
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)
            return root
        return dfs(0,len(nums)-1)
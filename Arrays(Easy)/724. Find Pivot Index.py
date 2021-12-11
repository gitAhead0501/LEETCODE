"""
724. Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Constraints:
A) 1 <= nums.length <= 104
B) -1000 <= nums[i] <= 1000

Approach: Check prefix sum of left side and right side of an index

"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pf = 0
        total = sum(nums)
        for i,x in enumerate(nums):
            if pf == total - pf - x:
                return i
            pf += x
        return -1
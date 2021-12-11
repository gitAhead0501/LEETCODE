"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Constraints:
A) 1 <= nums.length <= 10^5
B)-10^4 <= nums[i] <= 10^4

Approach: Find max of each prefix sum and return maximum of it

"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        res = nums[0]
        for i in nums[1:]:
            curr_max = max(i,curr_max+i)
            res = max(res,curr_max)
        return res
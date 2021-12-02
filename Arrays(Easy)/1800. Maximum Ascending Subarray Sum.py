"""
1800. Maximum Ascending Subarray Sum

Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi < numsi+1. Note that a subarray of size 1 is ascending.

Constraints:
A) 1 <= nums.length <= 100
B) 1 <= nums[i] <= 100


Approach: Find ascending prefix sum (max)

"""

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if not i or nums[i-1]>=nums[i]:
                val = 0
            val += nums[i]
            ans = max(ans,val)
        return ans
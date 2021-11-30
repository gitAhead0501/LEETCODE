"""
2057. Smallest Index With Equal Value
Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if such index does not exist.

x mod y denotes the remainder when x is divided by y.

Constraints:
A) 1 <= nums.length <= 100
B) 0 <= nums[i] <= 9

Approach: Just follow the problem statement

"""

from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i%10 == nums[i]:
                return i
        return -1
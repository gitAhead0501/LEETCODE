"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Constraints:
A) 1 <= nums.length <= 3 * 10^4
B) -3 * 10^4 <= nums[i] <= 3 * 10^4
C) Each element in the array appears twice except for one element which appears only once.

Approach1: Take xor of all elements
Approach2: Bit Manipulation

"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        z = nums[0]
        for each in nums[1:]:
            z^= each
        return z
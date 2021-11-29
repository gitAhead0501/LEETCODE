"""
1920. Build Array from Permutation
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

A) Constraints:
B) 1 <= nums.length <= 1000
C) 0 <= nums[i] < nums.length
D) The elements in nums are distinct.

Approach: Just return a list with values nums[nums[index]]

"""

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [ nums[nums[i]] for i in range(len(nums))]
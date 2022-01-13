"""
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

Constraints:
A) 1 <= n <= 104
B) nums.length == 2 * n
C) -10^4 <= nums[i] <= 10^4

Approach: sort the array and return the sum of even indexed array values as for them the sum is gonna be maximized

"""

from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[i] for i in range(0,len(nums),2))
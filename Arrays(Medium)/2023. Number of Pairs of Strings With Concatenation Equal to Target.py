"""
2023. Number of Pairs of Strings With Concatenation Equal to Target

Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.

Constraints:
A) 2 <= nums.length <= 100
B) 1 <= nums[i].length <= 100
C) 2 <= target.length <= 100
D) nums[i] and target consist of digits.
E) nums[i] and target do not have leading zeros.

Approach1: Naive approach : Two for loops and check where a+b == target and count

"""

from typing import List


# 1)
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i] + nums[j] == target:
                        count += 1
        return count
"""
1480. Running Sum of 1d Array
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Constraints:
A) 1 <= nums.length <= 1000
B) -10^6 <= nums[i] <= 10^6

Approach1: Naive approach , create an array and add sum to it from index 0 to current index
Approach2: return [ prefix sum directly ]
"""

from typing import List
from itertools import accumulate

# 1)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(len(nums)):
            a.append(sum(nums[:i+1]))
        return a


# 2)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [ sum(nums[:i+1]) for i in range(len(nums))]
    

# 3)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))
"""
1413. Minimum Value to Get Positive Step by Step Sum

Given an array of integers nums, you start with an initial positive value startValue.
In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Constraints:
A) 1 <= nums.length <= 100
B) -100 <= nums[i] <= 100

Approach: Find min prefix sum : return min if +ive else return with +1 to it
Methods:
1) For loop and comparison
2) accumulate for prefix sum

"""

import math
from itertools import accumulate
from typing import List

# 1)
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        p = math.inf
        for i in range(len(nums)):
            p = min(p,sum(nums[:i+1]))
        if p<0:
            return abs(p)+1
        else:
            return 1


# 2)
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return max(1,1-min(accumulate(nums)))
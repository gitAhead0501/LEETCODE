"""
1848. Minimum Distance to the Target Element

Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.

Return abs(i - start).

It is guaranteed that target exists in nums.

Constraints:
A) 1 <= nums.length <= 1000
B) 1 <= nums[i] <= 104
C) 0 <= start < nums.length
D) target is in nums.

Approach: Brute Force : Find the minimum value of abs(i-start) while traversing the array
Methods:
1) For loop
2) Enumeration

"""

import math
from typing import List

# 1)
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        mn = math.inf
        for i in range(len(nums)):
            if nums[i]==target:
                mn = min(mn,abs(i-start))
        return mn


# 2)
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        return min(abs(i-start) for i,v in enumerate(nums) if v==target)
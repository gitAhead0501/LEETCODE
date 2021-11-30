"""
1979. Find Greatest Common Divisor of Array
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

Constraints:
A) 2 <= nums.length <= 1000
B) 1 <= nums[i] <= 1000

Approach: Naive

"""

import math
from typing import List
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return math.gcd(max(nums),min(nums))
"""
2016. Maximum Difference Between Increasing Elements

Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1

Constraints:
A) n == nums.length
B) 2 <= n <= 1000
C) 1 <= nums[i] <= 10^9

Approach: Find maximum difference between increasing elements : maintain a prefix variable for smallest number

"""

import math
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        prefix = math.inf
        for i,x in enumerate(nums):
            if i and x>prefix:
                ans = max(ans,x-prefix)
            prefix = min(x,prefix)
        return ans
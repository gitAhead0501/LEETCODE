"""
1512. Number of Good Pairs
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.


Constraints:
A) 1 <= nums.length <= 100
B) 1 <= nums[i] <= 100

Approach: Count the occurence of distinct items, and sum up

"""

import collections
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        ans = 0
        for v in cnt.values():
            if v>1:
                ans += sum(range(1,v))
        return ans
# OR
# ONE LINER
        return sum(sum(range(1, v)) for v in collections.Counter(nums).values() if v > 1)
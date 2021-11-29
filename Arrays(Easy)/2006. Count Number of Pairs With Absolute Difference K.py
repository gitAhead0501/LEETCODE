"""
2006. Count Number of Pairs With Absolute Difference K
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.

Constraints:
A) 1 <= nums.length <= 200
B) 1 <= nums[i] <= 100
C) 1 <= k <= 99

Approach1: Brute Force
Approach2: create a hash table/counter and take values of n and n+k in counter keys if n+k in keys : counter takes 0
We can also use defaultdict instead of dict as defaultdict gives access to set default value

"""

from typing import List
from collections import Counter

# 1) BRUTE FORCE
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j]) == k:
                    count += 1
        return count


# 2) COUNTER METHOD
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        return sum(cnt[n]*cnt[n+k] for n in cnt.keys())

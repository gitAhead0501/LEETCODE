"""
1005. Maximize Sum Of Array After K Negations

Given an integer array nums and an integer k, modify the array in the following way:

choose an index i and replace nums[i] with -nums[i].
You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.

Constraints:
A) 1 <= nums.length <= 10^4
B) -100 <= nums[i] <= 100
C) 1 <= k <= 10^4

Approach: Iterate while k>0 and negate the minimum value in the index and return the sum of the final array

"""

from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        while k>0:
            mn = min(nums)
            idx = nums.index(mn)
            nums[idx] = -nums[idx]
            k-=1
        return sum(nums)
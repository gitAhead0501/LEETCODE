"""
485. Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Constraints:
A) 1 <= nums.length <= 105
B) nums[i] is either 0 or 1

Approach: For each element check the no of consecutive 1's and find the max of them

"""

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for each in nums:
            if each:
                count += 1
            else:
                count = 0
            ans = max(ans,count)
        return ans
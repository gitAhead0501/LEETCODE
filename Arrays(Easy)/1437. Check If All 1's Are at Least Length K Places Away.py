"""
1437. Check If All 1's Are at Least Length K Places Away
Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

Constraints:
A) 1 <= nums.length <= 105
B) 0 <= k <= nums.length
C) nums[i] is 0 or 1

Approach: Record the indices of 1's and check if their difference is less than k or not
# BIT MANIPULATION

"""
import math
from typing import List

# 1) TC : O(n) , SC : O(n)
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = [i for i in range(len(nums)) if nums[i]]
        for i in range(len(last)-1):
            if last[i+1]-last[i]<k+1:
                return False
        return True



# 1) TC : O(n) , SC : O(1)
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        j = -math.inf
        for i in range(len(nums)):
            if nums[i]:
                if i-j-1<k:
                    return False
                j=i
        return True
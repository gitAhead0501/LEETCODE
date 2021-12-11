"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Constraints:
A) 2 <= nums.length <= 104
B) -109 <= nums[i] <= 109
C) -109 <= target <= 109
D) Only one valid answer exists.

Approach: Brute or hashtable

"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in D:
                return [i, D[temp]]
            else:
                D[nums[i]] = i
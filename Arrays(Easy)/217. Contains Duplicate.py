"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Constraints:
A) 1 <= nums.length <= 10^5
B) -10^9 <= nums[i] <= 10^9

Approach: Simply check duplicates via hashtable or set or count 

"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
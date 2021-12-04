"""
448. Find All Numbers Disappeared in an Array
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Constraints:
A) n == nums.length
B) 1 <= n <= 10^5
C) 1 <= nums[i] <= n

Approach1: In place move the numbers to their correct indices and return the remaning numbers that r not in the original array
Approach2: return the set difference of range of numbers and set of array

"""

from typing import List


# 1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        return [i for i in range(1,len(nums)+1) if i!= nums[i-1]]


# 2) 
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list( set(range(1,len(nums)+1))-set(nums) )
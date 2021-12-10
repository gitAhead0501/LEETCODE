"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Constraints:
A) 1 <= nums.length <= 104
B) -104 < nums[i], target < 104
C) All the integers in nums are unique.
D) nums is sorted in ascending order.

Approach: Simple Binary Search

"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)
        while l<r:
            mid = l+(r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid
        return -1
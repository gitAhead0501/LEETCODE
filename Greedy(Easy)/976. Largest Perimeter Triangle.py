"""
976. Largest Perimeter Triangle

Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Constraints:
A) 3 <= nums.length <= 104
B) 1 <= nums[i] <= 106

Approach: Sort the array in reverse and return the sum where a+b>c from the end of the array

"""

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-3):
            if nums[i] > nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
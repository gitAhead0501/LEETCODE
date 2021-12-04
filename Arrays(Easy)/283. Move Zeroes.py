"""
283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Constraints:
A) 1 <= nums.length <= 104
B) -231 <= nums[i] <= 231 - 1

Approach: Maintain two pointers : i will be storing the index of last swapped value of 0 and non zero : j will be traversing the array

"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
        return nums # if said to return : else skip
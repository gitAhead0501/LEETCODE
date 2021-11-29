"""
1365. How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Constraints:
A) 2 <= nums.length <= 500
B) 0 <= nums[i] <= 100


Approch: Simply sort and check
"""

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        return [sorted_nums.index(num) for num in nums]
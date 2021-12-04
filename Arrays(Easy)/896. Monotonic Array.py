"""
896. Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Constraints:
A) 1 <= nums.length <= 10^5
B) -10^5 <= nums[i] <= 10^5

Approach1: use all to check the consistency of the monotonic property
Approach2: use boolean trick to check consistency
Approach3: use simple array checking of consistency

"""


from typing import List


# 1)
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return (all(nums[i]<= nums[i+1] for i in range(len(nums)-1))) or (all(nums[i] >=  nums[i+1] for i in range(len(nums)-1)))


# 2)
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = dec = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                inc = False
            if nums[i] < nums[i+1]:
                dec = False
        return inc or dec
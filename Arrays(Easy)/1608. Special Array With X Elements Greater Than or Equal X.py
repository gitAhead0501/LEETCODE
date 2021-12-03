"""
1608. Special Array With X Elements Greater Than or Equal X
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

Constraints:
A) 1 <= nums.length <= 100
B) 0 <= nums[i] <= 1000

Approach: Count no of elements greater than index in reverse sorted array : If idx < len(array) and idx & nums[i] are same then ans is -1
Searching can be done faster with Binary search
"""

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        j = 0
        while j<len(nums) and nums[j] > j:
            j+=1
        return -1 if j<len(nums) and j==nums[j] else j



# 2) Binary search
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if mid < nums[mid]:
                left = mid + 1
            else:
                right = mid       
        return -1 if left < len(nums) and left == nums[left] else left
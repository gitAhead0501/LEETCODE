"""
You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.

Constraints:
A) 1 <= nums.length <= 5000
B) 1 <= nums[i] <= 104

Approach: If higher index value is smaller than(or == ) lower index value then count the difference btw them + 1 and change the current index value to lower value + 1

"BRUTE FORCE WILL LEAD TO TLE i.e. inside for loop iterating while loop, while large idx value is greater than lower idx value"

"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                count += nums[i-1]-nums[i]+1
                nums[i] = nums[i-1] + 1
        return count
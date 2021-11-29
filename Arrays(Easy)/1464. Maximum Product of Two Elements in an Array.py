"""
1464. Maximum Product of Two Elements in an Array
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

Constraints:
A) 2 <= nums.length <= 500
B) 1 <= nums[i] <= 10^3

Approach1: Brute Find 1st and 2nd max value and return (nums[i]-1)*(nums[j]-1)
Approach2: Heapq (priority queues)

"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a,b = sorted(nums)[-1], sorted(nums)[-2]
        return (a-1)*(b-1)
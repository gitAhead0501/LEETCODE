"""
1403. Minimum Subsequence in Non-Increasing Order

Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence. 

If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 

Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.

Constraints:
A) 1 <= nums.length <= 500
B) 1 <= nums[i] <= 100

Approach1: Sort the array and in another array append popped value from the org array till sum(new arr)<= sum(org arr)
Approach2: Sort the array in reverse and return where the sum of subarray is greater than the rest subarray
same efficiency
"""

from typing import List


# 1)
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        while sum(res) <= sum(nums):
            res.append(nums.pop())
        return res


# 2)
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        for i in range(len(nums)):
            if sum(nums[:i+1]) > sum(nums[i+1:]):
                return nums[:i+1]
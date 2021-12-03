"""
1991. Find the Middle Index in Array

Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

Constraints:
A) 1 <= nums.length <= 100
B) -1000 <= nums[i] <= 1000

Approach1: Take leftsum as 0 and rightsum as sum(nums) : compare at each iteration leftsum and rightsum-nums[i] : [EFFICIENT]
Approach2: Use list slicing to check sum of subarray and right subarray

"""


from typing import List

# 1) TC : O(n)
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ls = 0
        rs = sum(nums)
        for i in range(len(nums)):
            if ls == rs-nums[i]:
                return i
            ls += nums[i]
            rs -= nums[i]
        return -1


# 2) TC : O(n*(k1+k2)) : where k1,k2 is the sum of subarrays varying at each iteration
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a = sum(nums[:i])
            b = sum(nums[i+1:])
            if a == b:
                return i
        return -1
"""
905. Sort Array By Parity
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Constraints:
A) 1 <= nums.length <= 5000
B) 0 <= nums[i] <= 5000

Approach1: In place : EFFICIENT : correct the order of even and odd numbers
Approach2: O(n) Space : creating a list and adding even numbers and then adding odd numbers

"""

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i]%2 > nums[j]%2:
                nums[i],nums[j] = nums[j],nums[i]
            if nums[i]%2==0:
                i+=1
            if nums[j]%2==1:
                j-=1
        return nums


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ls = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                ls.append(nums[i])
        for j in range(len(nums)):
            if nums[j] % 2 != 0:
                ls.append(nums[j])
        return ls
"""
977. Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Constraints:
A) 1 <= nums.length <= 10^4
B) -10^4 <= nums[i] <= 10^4
C) nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

Approach: Traverse from both the ends and store square of higher element and return the array

"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a,b = 0,len(nums)-1
        res = [0 for i in range(len(nums))]
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[a]) < abs(nums[b]):
                res[i] = nums[b]*nums[b]
                b-=1
            else:
                res[i] = nums[a]*nums[a]
                a+=1
        return res
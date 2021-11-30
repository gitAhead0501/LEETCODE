"""
852. Peak Index in a Mountain Array

Let's call an array arr a mountain if the following properties hold:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

Constraints:
A) 3 <= arr.length <= 104
B) 0 <= arr[i] <= 106
c) arr is guaranteed to be a mountain array.

Approach1: For loop : TIME COMPLEXITY : O(n)
Approach2 : Binary Search : TIME COMPLEXITY : O(logn)

"""

from typing import List

# 1) TC : O(n)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return i


# 2) TC : O(logn)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        while left < right:
            mid = left + (right-left)//2
            if arr[mid] < arr[mid+1]:
                left = mid+1
            else:
                right = mid
        return left
"""
1588. Sum of All Odd Length Subarrays
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.

Constraints:
A) 1 <= arr.length <= 100
B) 1 <= arr[i] <= 1000

Approach: Prefix sum problem
Methods:
1) Iterate over array and store result only when j-i is even i.e. odd length subarray sum
2) Iterate over array and store result of subarrays with j incrementing +2 times i.e. odd length subarray sum

"""

from typing import List


# 1)
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:        
        n, res = len(arr), 0
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += arr[j]
                if not (j-i) % 2:
                    res += sum
        return res


# 2)
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:  
        res = 0
        n = len(arr)
        for i in range(n):
            j = i
            while j<n:
                res += sum(arr[i:j+1])
                j+=2
        return res
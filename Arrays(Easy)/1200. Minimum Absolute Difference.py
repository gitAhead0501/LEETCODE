"""
1200. Minimum Absolute Difference

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr

Constraints:
A) 2 <= arr.length <= 10^5
B) -10^6 <= arr[i] <= 10^6

Approach: Find the minimum difference between any two numbers in the array and then return a list of pairs whose diff equals min_difff

"""

import math
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        min_diff = math.inf
        for i in range(len(arr)-1):
            min_diff = min(min_diff,arr[i+1]-arr[i])
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == min_diff:
                res.append([arr[i],arr[i+1]])
        return res
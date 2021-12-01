"""
1502. Can Make Arithmetic Progression From Sequence
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

Constraints:
A) 2 <= arr.length <= 1000
B) -10^6 <= arr[i] <= 10^6

Approach: Sort the array , find common difference of first two elements (abs diff) and check its consistency in the array
Methods:
1) Create a hashtable to store common diff of first two elements and every check if every diff is present in dict or not
2) Just check d equals common diff or not [EFFICIENT (obviously)]
"""

from typing import List

# 1)
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] != d:
                return False
        return True


# 2)
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] != d:
                return False
        return True
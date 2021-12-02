"""
1385. Find the Distance Value Between Two Arrays

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

Constraints:
A) 1 <= arr1.length, arr2.length <= 500
B) -1000 <= arr1[i], arr2[j] <= 1000
C) 0 <= d <= 100

Approach: Just check for every value in arr2 and arr1 if their difference is > d, count it

"""
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for val1 in arr1:
            if all(abs(val1-val2)>d for val2 in arr2):
                count += 1
        return count
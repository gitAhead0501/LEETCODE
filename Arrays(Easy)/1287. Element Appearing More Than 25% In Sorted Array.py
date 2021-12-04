"""
1287. Element Appearing More Than 25% In Sorted Array

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Constraints:
A) 1 <= arr.length <= 10^4
B) 0 <= arr[i] <= 10^5

Approach: idx which has same value as idx+n//4 is the answer

"""

from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr) // 4
        for i in range(len(arr)):
            if arr[i] == arr[i + n]:
                return arr[i]
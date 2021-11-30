"""
1356. Sort Integers by The Number of 1 Bits

Given an integer array arr. You have to sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the sorted array.

Constraints:
A) 1 <= arr.length <= 500
B) 0 <= arr[i] <= 10^4

Approach1: convert number to binary (using lib function 'bin'), find count and sort wrt count
Approach2: Using Bit manipulation

"""

from typing import List


# 1) Using Lib function : bin
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda x:(bin(x).count('1'),x))
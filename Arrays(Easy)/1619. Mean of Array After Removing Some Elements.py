"""
1619. Mean of Array After Removing Some Elements

Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.

Answers within 10-5 of the actual answer will be considered accepted.

Constraints:
A) 20 <= arr.length <= 1000
B) arr.length is a multiple of 20.
C) 0 <= arr[i] <= 10^5

Approach: Find the mutiple of len of arr and return sorted array excluding first k elements and last k elements
Methods : Multiply len by 0.05 or find k by dividing len(arr) by 20

"""

from typing import List


# 1)
class Solution:
    def trimMean(self, arr:List[int]) -> float:
        k = len(arr)//20
        return sum(sorted(arr)[k:-k]) /(18*k)


# 2)
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        lr = int((0.05)*n)
        arr.sort()
        ans = arr[lr:-lr]
        return sum(ans)/len(ans)
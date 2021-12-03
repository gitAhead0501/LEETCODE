"""
1394. Find Lucky Integer in an Array
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.

Constraints:
A) 1 <= arr.length <= 500
B) 1 <= arr[i] <= 500

Approach: Count and match the frequency of each element and return the largest

"""

from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        mx = -1
        for k,v in cnt.items():
            if v == k:
                mx = max(mx,k)
        return mx
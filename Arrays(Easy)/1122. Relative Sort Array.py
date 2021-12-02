"""
1122. Relative Sort Array
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

Constraints:
A) 1 <= arr1.length, arr2.length <= 1000
B) 0 <= arr1[i], arr2[i] <= 1000
C) All the elements of arr2 are distinct.
D) Each arr2[i] is in arr1.

Approach: create hashtable for arr1, store each value k times in res array where k is no of times each element of array 2 has occured in arr2 and pop it : add remaining elements in sorted manner with their respective frequencies

"""

from collections import Counter
from typing import Collection, List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        res = []
        for each in arr2:
            res += [each]*c.pop(each)
        return res + sorted(c.elements())
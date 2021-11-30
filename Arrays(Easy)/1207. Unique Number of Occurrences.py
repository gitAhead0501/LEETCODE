"""
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

Constraints:
A) 1 <= arr.length <= 1000
B) -1000 <= arr[i] <= 1000

Approach: Create a hashtable or Counter and check if the frequencies are distinct by comparing len of original and len of set of original

"""
from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h = {}
        for each in arr:
            if each not in h:
                h[each] = 1
            else:
                h[each] += 1
        return len(h.values()) == len(set(h.values()))


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h = Counter(arr)
        return len(h.values()) == len(set(h.values()))
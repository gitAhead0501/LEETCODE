"""
1460. Make Two Arrays Equal by Reversing Sub-arrays
Given two integer arrays of equal length target and arr.

In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

Return True if you can make arr equal to target, or False otherwise.

Constraints:
A) target.length == arr.length
B) 1 <= target.length <= 1000
C) 1 <= target[i] <= 1000
D) 1 <= arr[i] <= 1000


Approach1: Sort and check each element
Approach2: Check counter of both arrays
Approach3: Hashing Technique : Since the max length of arrays can be 1000 : We create an array of 1001 and increment by 1 for elements in one array and decrement by 1 for elements in another array : Then check if an element of hashing array is greater than 0 : [ EFFICIENT ]

"""
from collections import Counter
from typing import List

# 1) 
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        for i in range(len(target)):
            if target[i] != arr[i]:
                       return False
        return True

# 2)
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)


# 3) [EFFICIENT]
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hashing = [0]*1001
        for i in range(len(target)):
            hashing[target[i]] += 1
            hashing[arr[i]] -= 1

        for each in hashing:
            if each != 0:
                return False
        return True
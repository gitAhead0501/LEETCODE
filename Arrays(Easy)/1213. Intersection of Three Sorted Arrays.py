"""
1213. Intersection of Three Sorted Arrays
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

Constraints:
A) 1 <= arr1.length, arr2.length, arr3.length <= 1000
B) 1 <= arr1[i], arr2[i], arr3[i] <= 2000

Approach1: Use HashTable [TIME COMPLEXITY: O(n)]
Approach2: Brute checking in sorted arrays [TIME COMPLEXITY: O(n1+n2+n3)]

"""

from typing import List

# 1) 
class Solution:
    def countGoodTriplets(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> int:
        h = {}
        for i in range(len(arr1)):
            if arr1[i] not in h:
                h[arr1[i]] = 1
            else:
                h[arr1[i]] += 1
        for i in range(len(arr2)):
            if arr2[i] not in h:
                h[arr2[i]] = 1
            else:
                h[arr2[i]] += 1

        for i in range(len(arr3)):
            if arr3[i] not in h:
                h[arr3[i]] = 1
            else:
                h[arr3[i]] += 1
        return [k for k,v in h.items() if v==3]


# 2) 
class Solution:
    def countGoodTriplets(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> int:
        i,j,k = 0,0,0
        res = []
        while i<len(arr1) and j<len(arr2) and k<len(arr3):
            if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
                res.append(arr1[i])
                i+=1
                j+=1
                k+=1
            elif arr1[i] < arr2[j]:
                i+=1
            elif arr2[j] < arr3[k]:
                j+=1
            else:
                k+=1
        return res
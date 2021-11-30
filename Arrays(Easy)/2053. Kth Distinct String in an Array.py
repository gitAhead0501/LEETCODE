"""
2053. Kth Distinct String in an Array

A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

Constraints:
A) 1 <= k <= arr.length <= 1000
B) 1 <= arr[i].length <= 5
C) arr[i] consists of lowercase English letters.

Approach1: Create a hash table and store count and order of array, so as to return the kth distinct value 
Approach2: Count directly in the array
Approach3: Counter function and decrementing k [EFFICIENT]

"""

from typing import List


# 1)
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        h = {}
        for i in range(len(arr)):
            if arr[i] not in h:
                h[arr[i]] = 1
            else:
                h[arr[i]] += 1
        print(h)
        c = 1
        for key,v in h.items():
            if v==1:
                if c == k:
                    return key
                else:
                    c+=1
        return ""


# 2) 
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = []
        for each in arr:
                if arr.count(each) == 1:
                    res.append(each)
        if k > len(res):
            return ""
        return res[k-1]

# 3) 99% Faster
from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        for key in cnt:
            if cnt[key] == 1:
                k-=1
            if k==0:
                return key
        return ""
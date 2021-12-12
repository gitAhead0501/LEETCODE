"""
1338. Reduce Array Size to The Half

You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

Constraints:
A) 1 <= arr.length <= 105
B) arr.length is even.
C) 1 <= arr[i] <= 105

Approach: Count the frequency of each element and pop maximum freq and check if it is greater than half len of arr or not
Methods: 1) Using heapq 2) Using simple array sorting

"""

import heapq
from collections import Counter
from typing import List


# 1)
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        max_heap = []
        for i in cnt.values():
            max_heap.append(-1*i)
        heapq.heapify(max_heap)
        ans, removed = 0,0
        while removed<len(arr)//2:
            ans+=1
            removed += heapq.heappop(max_heap)
        return ans


# 2)
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        freq = sorted(cnt.values())
        ans,removed = 0,0
        while removed<len(arr)//2:
            removed += freq.pop()
            ans+=1
        return ans


# 3) TLE
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        freq = list(cnt.values())
        ans,removed = 0,0
        while removed<len(arr)//2:
            removed += freq.pop(freq.index(max(freq)))
            ans+=1
        return ans
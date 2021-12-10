"""
1539. Kth Missing Positive Number

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

Constraints:
A) 1 <= arr.length <= 1000
B) 1 <= arr[i] <= 1000
C) 1 <= k <= 1000
D) arr[i] < arr[j] for 1 <= i < j <= arr.length

Approach1: Use BS, if difference of value at an index and index is less than k that means ans i.e. kth missing +ive integer is right to that index else on the left side in the array
Approach2: Use set for checking if each number is in range of set or not, if not return kth number

"""

from typing import List

# 1) TC: O(logn)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0,len(arr)
        while left<right:
            mid = left + (right-left)//2
            if arr[mid]-mid-1<k:
                left = mid+1
            else:
                right = mid
        return left+k



# 2) TC: O(n)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)
        for i in range(1,k+len(arr)+1):
            if i not in arr_set: k-=1
            if k==0:
                return i
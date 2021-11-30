"""
1299. Replace Elements with Greatest Element on Right Side
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5

Approach1: Forward Traversal : TIME COMPLEXITY : O(n^2) : updating array with max value on its right subarray
Approach2: Backward Traversal : TIME COMPLEXITY : O(n)  : updating array with max value of (an integer and array element)

"""

from typing import List

# 1) TC : O(n^2)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = -1
        for i in range(len(arr)-1,-1,-1):
            mx, arr[i] = max(mx,arr[i])
            arr[i]  = mx
        return arr


# 2) TC : O(n)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-1):
            arr[i] = max(arr[i+1:])
        arr[n-1] = -1
        return arr
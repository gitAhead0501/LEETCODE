"""
1089. Duplicate Zeros

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Constraints:
A) 1 <= arr.length <= 104
B) 0 <= arr[i] <= 9

Approach: If 0 occurs, shift all the values to the right side

"""

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        i=0
        while(i<n-1):
            if not arr[i]:
                k=arr[i+1]
                for j in range(i+2,n):
                    temp=arr[j]
                    arr[j]=k
                    k=temp
                arr[i+1]=0
                i+=2
            else:
                i+=1

        # or use list slicing
        n=len(arr)
        i=0
        while(i<n-1):
            if arr[i]==0:
                arr[i+1:n] = arr[i:n-1]
                i += 2
            else:
                i += 1

# 2) MOST EFFICIENT
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        for i in reversed(range(len(arr))):
            if i + zeros < len(arr): 
                arr[i+zeros] = arr[i]
            if arr[i] == 0: 
                zeros -= 1
                if i + zeros < len(arr): 
                    arr[i+zeros] = 0
            print(arr)
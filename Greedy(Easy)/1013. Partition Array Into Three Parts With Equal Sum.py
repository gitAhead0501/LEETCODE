"""
1013. Partition Array Into Three Parts With Equal Sum

Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

Constraints:
A) 3 <= arr.length <= 5 * 104
B) -104 <= arr[i] <= 104

Approach: Find the sum of the array(ex: 3x) if it can be divided into 3 subarrays of equal sum than it's sum will be divisible by 3.  Also check if the prefixsum is equal to the avg reset prefix sum and count again, if count>=3 then return True

"""

from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False
        target = sum(arr)//3
        count = 0
        psum = 0
        for i in range(len(arr)):
            psum += arr[i]
            if psum == target:
                count+=1
                psum = 0
            if count == 3 and sum(arr)%3==0:
                return True
        return False
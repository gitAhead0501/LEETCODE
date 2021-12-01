"""
922. Sort Array By Parity II
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

Constraints:
A) 2 <= nums.length <= 2 * 104
B) nums.length is even.
C) Half of the integers in nums are even.
D) 0 <= nums[i] <= 1000

Approach1: Create an additional array and set odd at odd indices and even at even indices
Appraoch2: In place : swapping the elements at incorrect position

"""

from typing import List

# 1)
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        e = 0
        o = 1
        for n in nums:
            if n & 1:
                ans[o] = n
                o += 2
            else:
                ans[e] = n
                e += 2
        return ans


# 2) 
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j, n = 0, 1, len(nums)
        while j < n and i < n:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return nums

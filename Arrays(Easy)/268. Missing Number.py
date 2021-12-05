"""
268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Constraints:
A) n == nums.length
B) 1 <= n <= 104
C) 0 <= nums[i] <= n
D) All the numbers of nums are unique.

Approach1: set difference of range of 0 to n+1 and numbers in nums
Approach2: Bit Manipulation : using xor
Approach3: Sum of n natural numbers n - sum of array numbers

"""

from typing import List

# 1) TC : O(n^2) , SC : O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (set(range(len(nums)+1))-set(nums)).pop()


# 2) TC : O(n) , SC : O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in range(len(nums)):
            xor ^= (i+1)^nums[i]
        return xor


# 3) TC : O(n) , SC : O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n*(n+1)/2-sum(nums)
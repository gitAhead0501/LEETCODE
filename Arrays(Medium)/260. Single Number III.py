"""
260. Single Number III

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Constraints:
A) 2 <= nums.length <= 3 * 10^4
B) -2^31 <= nums[i] <= 2^31 - 1
C) Each integer in nums will appear twice, only two integers will appear once.

Approach1: Count the elements which occur only once : Hashtable
Approach2: Bit manipulation

"""

from collections import Counter
from typing import List

# 1)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        return [i for i in cnt.keys() if cnt[i]==1]
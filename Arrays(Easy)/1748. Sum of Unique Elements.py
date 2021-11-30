"""
1748. Sum of Unique Elements
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

Constraints:
A) 1 <= nums.length <= 100
B) 1 <= nums[i] <= 100

Approach: Create a hashtable and add keys for which value is 1

"""

from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        h = {}
        for each in nums:
            if each not in h:
                h[each] = 1
            else:
                h[each] += 1
        ans = 0
        for k,v in h.items():
            if v==1:
                ans += k
        return ans
"""
1913. Maximum Product Difference Between Two Pairs
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.

Constraints:
A) 4 <= nums.length <= 10^4
B) 1 <= nums[i] <= 10^4

Approach1: We can pop 2 max values and 2 min values to get MAXIMUM PRODUCT DIFFERENCE [[TIME COMPLEXITY : O(n)]] 
Approach2: We sort the list and take first two values and last two values [TIME COMPLEXITY : O(nlogn)]

"""

from typing import List

# 1)
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a = nums.pop(nums.index(max(nums)))
        b = nums.pop(nums.index(max(nums)))
        c = nums.pop(nums.index(min(nums)))
        d = nums.pop(nums.index(min(nums)))
        return a*b - c*d

# 2) 
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]*nums[-2]) - (nums[0]*nums[1])
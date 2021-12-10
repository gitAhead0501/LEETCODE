"""
697. Degree of an Array
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Constraints:
A) nums.length will be between 1 and 50,000.
B) nums[i] will be an integer between 0 and 49,999.

Approach: Store the left and right occurences of each element, find degree of array and return the minimum diff indices array with same degree

"""

from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x,0) + 1
            
        degree = max(count.values())
        ans = len(nums)
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x]-left[x]+1)
        
        return ans
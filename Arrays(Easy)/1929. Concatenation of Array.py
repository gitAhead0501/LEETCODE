"""
1929. Concatenation of Array
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Constraints:
A) n == nums.length
B) 1 <= n <= 1000
C)1 <= nums[i] <= 1000

Approach1: Create a array of 2n size and run a for loop and set as given in question
Approach2: return nums+nums or nums*2

"""


from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

'''
return nums*2

OR 

ans = [0]*2n
for i in range(len(nums)):
    ans[i] = nums[i]
    ans[i+n] = nums[i]
return ans
'''
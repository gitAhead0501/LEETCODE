"""
303. Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Constraints:
A) 1 <= nums.length <= 10^4
B) -10^5 <= nums[i] <= 10^5
C) 0 <= left <= right < nums.length
D) At most 10^4 calls will be made to sumRange.

Approach: In sumRange function, using iteration to return difference of two prefix sum's is very slow : so, define prefix array with values of prefix sum and in sumRange function return difference of right index value and left index value

"""

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for x in nums:
            self.prefix.append(self.prefix[-1]+x)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
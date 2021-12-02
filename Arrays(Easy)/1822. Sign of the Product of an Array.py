"""
1822. Sign of the Product of an Array

There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).

Constraints:
A) 1 <= nums.length <= 1000
B) -100 <= nums[i] <= 100

Approach: If element is 0 return : if element is -ive , multiply -1 : and return ans

"""

from typing import List

# 1)
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for i in nums:
            if i == 0:
                return 0
            if i<0:
                ans *= -1
        return ans


# 2) NAIVE APPROACH:
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for i in nums:
            ans *= i
        if ans == 0:
            return 0
        elif ans < 0:
            return -1
        else:
            return 1
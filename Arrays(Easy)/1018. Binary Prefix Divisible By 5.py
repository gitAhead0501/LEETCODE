"""
1018. Binary Prefix Divisible By 5

You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

Constraints:
A) 1 <= nums.length <= 10^5
B) nums[i] is 0 or 1.

Approach: convert binary string to decimal and return true if div by 5

"""

from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        nums = list(map(str,nums))
        res = []
        ans = ""
        for i in range(len(nums)):
            ans += nums[i]
            if int(ans,2)%5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res
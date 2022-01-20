"""
1877. Minimize Maximum Pair Sum in Array

The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

Each element of nums is in exactly one pair, and
The maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements.

Constraints:
A) n == nums.length
B) 2 <= n <= 10^5
C) n is even.
D) 1 <= nums[i] <= 10^5

Approach: Find the maximum value from extreme indices from both the end

"""

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0,len(nums)-1
        mx = 0
        while i<j:
            mx = max(mx,nums[i]+nums[j])
            i+=1
            j-=1
        return mx
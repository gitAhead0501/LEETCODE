"""
961. N-Repeated Element in Size 2N Array
You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

Constraints:
A) 2 <= n <= 5000
B) nums.length == 2 * n
C) 0 <= nums[i] <= 104
D) nums contains n + 1 unique elements and one of them is repeated exactly n times.

Approach: Check in hashtable if count is greater than 1 OR check in Counter if count equal n//2

"""

from collections import Counter
from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        cnt = Counter(nums)
        for k,v in cnt.items():
            if v == n:
                return k
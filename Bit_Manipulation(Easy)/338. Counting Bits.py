"""
338. Counting Bits
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Constraints:
1) 0 <= n <= 105

Approach: Create a dp and store 1+prev value in dp if integer is odd else store value stored in half of integer index in dp.

"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]
        for i in range(1,n+1):
            if i%2:
                dp.append(dp[i-1]+1)
            else:
                dp.append(dp[i//2])
        return dp
        
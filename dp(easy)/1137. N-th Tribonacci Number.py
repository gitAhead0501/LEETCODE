"""
1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Constraints:
A) 0 <= n <= 37
B) The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

Approach: Create dp and store previous 3 values in next index
Methods: create dp of only 3 values and append values to it and return last value or create dp of n length and change values in it

"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if not n:
            return 0
        dp = [0,1,1] + [0]*(n-2)
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[-1]

# or


class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        dp = [0,1,1]
        for i in range(3,n+1):
            dp.append(dp[i-1] + dp[i-2] + dp[i-3])
        return dp[-1]
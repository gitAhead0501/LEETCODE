"""
118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Constraints:
A) 1 <= numRows <= 30

Approach: Create a dp and store in it the sum of prefix values using 2 for loops. For each outer index i take upto ith index from the dp and store in another array and return it

"""


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [1]*(numRows)
        arr = [[1]]
        val = 1
        for i in range(1,numRows):
            for j in range(i-1,0,-1):
                dp[j] += dp[j-1]
            arr.append(dp[:i+1])
        return arr
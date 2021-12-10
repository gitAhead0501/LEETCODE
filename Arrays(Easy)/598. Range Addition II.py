"""
598. Range Addition II

You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.

Constraints:
A) 1 <= m, n <= 4 * 104
B) 0 <= ops.length <= 104
C) ops[i].length == 2
D) 1 <= ai <= m
E) 1 <= bi <= n

Approach: The min of row and col value to be incremented is the most incremented value: so we keep track of min of each ops in row and col

"""

from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for x,y in ops:
            m = min(m,x)
            n = min(n,y)
        return m*n
"""
1380. Lucky Numbers in a Matrix
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Constraints:
A) m == mat.length
B) n == mat[i].length
C) 1 <= n, m <= 50
D) 1 <= matrix[i][j] <= 105.
E) All elements in the matrix are distinct.

Approach1: Store min in each row and max in each column : return their common elements
Approach2: Find min in each row and find it's index and run a loop to find max value in that index of column and compare max and min

"""

import math
from typing import List

# 1) TIME COMPLEXITY : O(n^2) , SPACE : O(n) :  a little efficient than Approach 2
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mi = [min(row) for row in matrix]
        mx = [max(col) for col in zip(*matrix)]
        return [cell for i, row in enumerate(matrix) for j, cell in enumerate(row) if mi[i] == mx[j]]


# 2) TIME COMPLEXITY : O(n^2) , SPACE : O(n)
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        for i in range(m):
            mi = min(matrix[i])
            idx = matrix[i].index(mi)
            ma = -math.inf
            for j in range(m):
                ma = max(matrix[j][idx],ma)
            if mi == ma:
                res.append(mi)
        return res
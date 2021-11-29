"""
1572. Matrix Diagonal Sum
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

Constraints:
A) n == mat.length == mat[i].length
B) 1 <= n <= 100
C) 1 <= mat[i][j] <= 100

Approach:
For primary diagonal, add matrix if row and column are equal
For secondary diagonal, add matrix if row != column and row + column equals no of rows-1

"""

from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        sum = 0
        for i in range(rows):
            for j in range(cols):
                if i==j:
                    sum += mat[i][j]
                elif i!=j and i+j == rows-1:
                    sum += mat[i][j]
        return sum
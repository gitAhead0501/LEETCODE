"""
1582. Special Positions in a Binary Matrix

Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.

A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Constraints:
A) rows == mat.length
B) cols == mat[i].length
C) 1 <= rows, cols <= 100
D) mat[i][j] is 0 or 1.

Approach: Find 1 in each row, find that row's sum and the column sum(by creating a transpose of the matrix) : both should be 1

"""

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        matt = list(zip(*mat))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and sum(mat[i])==1 and sum(matt[j])==1:
                    count += 1
        return count
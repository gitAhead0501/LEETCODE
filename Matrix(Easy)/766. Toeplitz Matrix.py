"""
766. Toeplitz Matrix

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.


Constraints:
A) m == matrix.length
B) n == matrix[i].length
C) 1 <= m, n <= 20
D) 0 <= matrix[i][j] <= 99

Approach1: Check the consistency of two rows : i.e. their first cols-1 and last cols-1 element's sequence is equal or not
Appraoch2: Elements are in same diagonal if and only if their coordinates diff are same (abs diff) : store in hashtable these coordinates differences and check if another coordinate with same difference has same value as stored in hashtable or not

"""

from typing import List


# 1)
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows-1):
            if matrix[i][:cols-1] != matrix[i+1][1:cols]:
                return False
        return True


# 2)
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True
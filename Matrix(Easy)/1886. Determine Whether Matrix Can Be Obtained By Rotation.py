"""
1886. Determine Whether Matrix Can Be Obtained By Rotation
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

Constraints:
A) n == mat.length == target.length
B) n == mat[i].length == target[i].length
C) 1 <= n <= 10
D) mat[i][j] and target[i][j] are either 0 or 1.

Approach: Reverse the matrix rows and compare transpose of resulting matrix with target

"""

from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            mat = list(map(list,zip(*mat[::-1])))
        return False
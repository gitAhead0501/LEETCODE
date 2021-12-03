"""
566. Reshape the Matrix
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Constraints:
A) m == mat.length
B) n == mat[i].length
C) 1 <= m, n <= 100
D) -1000 <= mat[i][j] <= 1000
E) 1 <= r, c <= 300

Approach: Store values of grid in oneD array and iter through it and create result matrix
Methods: Generator or List

"""

from typing import List


# 1) List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        it = [x for row in mat for x in row]
        return [it[i*c:(i+1)*c] for i in range(r)]


# 2) Generator : Faster
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        it = (x for row in mat for x in row)
        return [next(it) for _ in range(c) for a in range(r)]
"""
1329. Sort the Matrix Diagonally

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

Constraints:
A) m == mat.length
B) n == mat[i].length
C) 1 <= m, n <= 100
D) 1 <= mat[i][j] <= 100

Approach: Create a hashtable to store all the same diagonal difference values : sort them back : and make changes in the original list (if permited)

"""

from typing import List


# 1)
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        h = {}
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                if i-j not in h:
                    h[i-j] = [mat[i][j]]
                else:
                    h[i-j] += [mat[i][j]]
        
        for i in h:
            h[i].sort(reverse=1)
        for i in range(m):
            for j in range(n):
                mat[i][j] = h[i-j].pop()
        return mat
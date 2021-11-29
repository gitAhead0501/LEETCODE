"""
1252. Cells with Odd Values in a Matrix
There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.

For each location indices[i], do both of the following:

Increment all the cells on row ri.
Increment all the cells on column ci.
Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.

 

Constraints:
A) 1 <= m, n <= 50
B) 1 <= indices.length <= 100
C) 0 <= ri < m
D) 0 <= ci < n


Approach: Create a matrix, increment according to given problem : return count of add values in the matrix
"""

from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [ [0 for j in range(n)] for i in range(m) ]
        for each in indices:
            for i in range(len(matrix[each[0]])):
                matrix[each[0]][i] += 1
            for i in range(m):
                matrix[i][each[1]] += 1
        count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]%2:
                    count += 1
        return count
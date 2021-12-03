"""
867. Transpose Matrix

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Constraints:
A) m == matrix.length
B) n == matrix[i].length
C) 1 <= m, n <= 1000
D) 1 <= m * n <= 10^5
E) -10^9 <= matrix[i][j] <= 10^9

Approach1: ONE LINER
Approach2: Copy directly : if u don't want to modify intial matrix : else change the matrix itself

"""

from typing import List

# 1) ONE LINER
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(map(list,zip(*matrix)))
        # or return zip(*matrix)


# 2) Initialize an array and copy elements into it : TC : O(r*c) : SC(same)
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r,c = len(matrix), len(matrix[0])
        ans = [[None]*r for _ in range(c)]
        for ro,row in enumerate(matrix):
            for co,val in enumerate(row):
                ans[co][ro] = val
        return ans
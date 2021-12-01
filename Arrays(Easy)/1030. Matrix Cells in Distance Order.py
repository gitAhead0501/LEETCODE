"""
1030. Matrix Cells in Distance Order
You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).

Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance. You may return the answer in any order that satisfies this condition.

The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.

Constraints:
A) 1 <= rows, cols <= 100
B) 0 <= rCenter < rows
C) 0 <= cCenter < cols

Approach: Create a matrix of rows * column : sort it with wrt to distance from rCentre and cCenter

"""

from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        def key_(point):
            x,y = point
            return abs(x-rCenter) + abs(y-cCenter)
        matrix = [[i,j] for i in range(rows) for j in range(cols)]
        return sorted(matrix, key= key_)
    
    #  ONE LINER
    #  return sorted([[i,j] for i in range(rows) for j in range(cols)] , key = lambda x: abs(x[0]-rCenter)+abs(x[1]-cCenter))
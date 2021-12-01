"""
883. Projection Area of 3D Shapes

You are given an n x n grid where we place some 1 x 1 x 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of the cell (i, j).

We view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3-dimensional figure to a 2-dimensional plane. We are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.

Constraints:
A) n == grid.length
B) n == grid[i].length
C) 1 <= n <= 50
D) <= grid[i][j] <= 50

Approach: For xy plane ,count when cubes present is not 0 : For xz plane, find max in row : For yz plane, find max in column
Methods:
1) For loops
2) Map function + for loop : Shorter code

"""

from typing import List

# 1)
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        # xy : count when cubes present is not 0
        # xz : maximum of row in matrix
        # yz : maximum of column in matrix
        ans = 0
        for each in grid:
            for i in each:
                if i!=0:
                    ans +=1
        for each in grid:
            ans += max(each)
        for each in list(zip(*grid)):
            ans += max(each)
        return ans


# 2)
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = sum(map(max,grid))
        ans += sum(map(max,zip(*grid)))
        ans += sum(v>0 for row in grid for v in row)
        return ans

# ONE LINER :
# return sum(map(max,grid)) + sum(map(max,zip(*grid))) + sum(v>0 for row in grid for v in row)
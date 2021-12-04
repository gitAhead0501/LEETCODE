"""
892. Surface Area of 3D Shapes
You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).

After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.

Return the total surface area of the resulting shapes.

Note: The bottom face of each shape counts toward its surface area.


Constraints:
A) n == grid.length
B) n == grid[i].length
C) 1 <= n <= 50
D) 0 <= grid[i][j] <= 50

Approach:
1) First we check if there is only one cell in matrix/grid or not.
2) If yes then just simply return 6 + 4(the value of cell - 1) : Because 1 cube has surface area of 6a^2 i.e. 6 here , everytime a new cube is added at the top of a cube surface area increases by 6-2=4units : as 2 units get glued
3) If no, then iterate each row and find the difference from the next cell in that row and check if the the cell is not first and last colunm of that row. If it is, then just take the abs difference otherwise add the grid value at that position as we have to cover back side of cells inbetween the first and last row.
4) Repeat this process with each column.
5) Finally calculate the top and bottom surfaces if cell is not empty.
6) Also, add the remaining surfaces of corner cells.

"""

from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == n == 1:
            return 6 + 4*(grid[0][0]-1)
        bt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    bt += 1
        bt = bt*2
        ans = 0
        for i in range(m):
            for j in range(n-1):
                if j==0:
                    ans += abs(grid[i][j]-grid[i][j+1])
                else:
                    if i==0 or i==m-1:
                        ans += abs(grid[i][j]-grid[i][j+1]) + grid[i][j]
                    else:
                        ans += abs(grid[i][j]-grid[i][j+1])
        for i in range(n):
            for j in range(m-1):
                if j==0:
                    ans += abs(grid[j][i]-grid[j+1][i])
                else:
                    if i == 0 or i==n-1:
                        ans += abs(grid[j][i]-grid[j+1][i]) + grid[j][i]
                    else:
                        ans += abs(grid[j][i]-grid[j+1][i])
        ans += 2*(grid[0][0]+ grid[0][n-1] + grid[m-1][0] + grid[m-1][n-1])
        ans += bt
        return ans
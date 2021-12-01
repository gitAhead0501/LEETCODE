"""
463. Island Perimeter
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Constraints:
A) row == grid.length
B) col == grid[i].length
C) 1 <= row, col <= 100
D) grid[i][j] is 0 or 1.
E) There is exactly one island in grid.

Approach: If land is found , increment ans by 4 : check for neighbours if i+1 and j+1 are land, decrement ans by 2 and 2

"""

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 4
                    if i+1<rows and grid[i+1][j] == 1:
                        count -=2
                    if j+1<cols and grid[i][j+1] == 1:
                        count -= 2
        return count
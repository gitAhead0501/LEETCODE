"""
807. Max Increase to Keep City Skyline

There is a city composed of n x n blocks, where each block contains a single building shaped like a vertical square prism. You are given a 0-indexed n x n integer matrix grid where grid[r][c] represents the height of the building located in the block at row r and column c.

A city's skyline is the the outer contour formed by all the building when viewing the side of the city from a distance. The skyline from each cardinal direction north, east, south, and west may be different.

We are allowed to increase the height of any number of buildings by any amount (the amount can be different per building). The height of a 0-height building can also be increased. However, increasing the height of a building should not affect the city's skyline from any cardinal direction.

Return the maximum total sum that the height of the buildings can be increased by without changing the city's skyline from any cardinal direction.

Constraints:
A) n == grid.length
B) n == grid[r].length
C) 2 <= n <= 50
D) 0 <= grid[r][c] <= 100

Approach: To not affect the skyline, we should increase the buildings upto max height of each row and max height of each col. Find the sum of effective increase in the heighting i.e. it should be increase or not, so for a building we will find the min of maxheight in its row and maxheight in its col and subtract the height of the present building.

"""

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]
        total = 0
        for r,row in enumerate(grid):
            for c,val in enumerate(row):
                total += min(row_maxes[r],col_maxes[c])-val
        return total


"""
1779. Find Nearest Point That Has the Same X or Y Coordinate
You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).

Constraints:
A) 1 <= points.length <= 10^4
B) points[i].length == 2
C) 1 <= x, y, ai, bi <= 10^4

Approach: Enumerate over the array, find the points with smallest Manhattan distance : find the minimum index of this distance

"""
import math
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        idx , smallest = -1, math.inf
        for i, (r,c) in enumerate(points):
            if (x-r)*(y-c)==0 and abs(x+y-r-c) < smallest:
                smallest = abs(x+y-r-c)
                idx = i
        return idx
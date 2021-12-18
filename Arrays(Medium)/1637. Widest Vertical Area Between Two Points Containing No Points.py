"""
1637. Widest Vertical Area Between Two Points Containing No Points

Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.

Constraints:
A) n == points.length
B) 2 <= n <= 10^5
C) points[i].length == 2
D) 0 <= xi, yi <= 10^9

Approach: Sort the points list and return the max difference from 1st index of each sublist

"""

from typing import List
import math


# 1)
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        mx = -math.inf
        for i in range(len(points)-1):
            mx = max(mx,points[i+1][0] -points[i][0])
        return mx

# 2)
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        vals = sorted(x for x, _ in points)
        return max(vals[i] - vals[i-1] for i in range(1, len(vals)))
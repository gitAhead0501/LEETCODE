"""
2078. Two Furthest Houses With Different ColorsThere are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

Return the maximum distance between two houses with different colors.

The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.

Constraints:
A) n == colors.length
B) 2 <= n <= 100
C) 0 <= colors[i] <= 100
Test data are generated such that at least two houses have different colors.

Approach: Find the distance between left most house of different color and right most house of diff color: from both sides find max of this distance

"""

from turtle import color
from typing import List

# 1)
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i,j = 0,len(colors)-1
        while colors[-1] == colors[i]:
            i+=1
        while colors[0] == colors[j]:
            j-=1
        return max(len(colors)-1-i,j)


# 2)
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        for i,x in enumerate(colors):
            if x!=colors[0]: ans = max(ans,i)
            if x!=colors[-1]: ans = max(ans,len(colors)-1-i)
        return ans

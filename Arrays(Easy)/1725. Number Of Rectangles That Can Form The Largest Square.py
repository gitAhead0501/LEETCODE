"""
1725. Number Of Rectangles That Can Form The Largest Square
You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.

You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.

Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.

Return the number of rectangles that can make a square with a side length of maxLen.


Constraints:
A) 1 <= rectangles.length <= 1000
B) rectangles[i].length == 2
C) 1 <= li, wi <= 109
D) li != wi

Approach: Find minimum of each rectangle i.e. min length and count it in each rectangles i.e. no of rectangles that can make a square
Methods:
Simultaneously, compute maxLen and curr_max
OR
Store in array and return equal lengths i.e. same values in array

"""

from collections import Counter
from typing import List
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxlen = -float("inf")
        count = 1
        for i in range(len(rectangles)):
            cur_max = min(rectangles[i])
            if cur_max > maxlen:
                maxlen = cur_max
                count = 1
            elif cur_max == maxlen:
                count+=1
        return count
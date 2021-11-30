"""
1051. Height Checker
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

Constraints:
A) 1 <= heights.length <= 100
B) 1 <= heights[i] <= 100


Approach: Just return the count where heights[i] != expected[i]
Methods:
1) For loop and compare index in both arrays simultaneously
2) Use zip and return index 0 not equals with 1

"""

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = list(zip(heights,sorted(heights)))
        c = 0
        for each in res:
            if each[0]!=each[1]:
                c+=1
        return c

"""
1893. Check if All the Integers in a Range Are Covered

You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.

Constraints:
A) 1 <= ranges.length <= 50
B) 1 <= starti <= endi <= 50
C)1 <= left <= right <= 50

Approach1: Store all the range values into a list and then convert into hashtable and check if every element in left to right is present in hastable or not
Approach2:

"""

from typing import List


# 1)
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ans = []
        for each in ranges:
            ans += list(range(each[0],each[1]+1))
        h = {k:0 for k in ans}
        ls = list(range(left,right+1))
        for each in ls:
            if each not in h:
                return False
        return True



# 2)
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        return all(any(l <= i <= r for l,r in ranges) for i in range(left,right+1))